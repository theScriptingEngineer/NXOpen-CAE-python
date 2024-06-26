# intellisense by theScriptingEngineer
# untested

# The code for EnvelopeResults is only available in NX version 1980, release 2021.2 onwards. For earlier NX versions, use PostProcessing.py

import math
import sys
import os
import NXOpen
import NXOpen.CAE
import NXOpen.Fields
from typing import List, cast, Tuple, Dict

the_session = NXOpen.Session.GetSession()
base_part: NXOpen.BasePart = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow

class PostInput:
    """A class for declaring inputs used in CombineResults"""
    _solution: str
    _subcase: int
    _iteration: int
    _resultType: str
    _identifier: str

    def __init__(self) -> None:
        """Parameterless constructor. Strings initialized to empty strings and integers to -1"""
        self._solution = ""
        self._subcase = -1
        self._iteration = -1
        self._resultType = ""
        self._identifier = ""
    
    def __init__(self, solution: str, subcase: int, iteration: int, resultType: str, identifier: str = ""):
        """Constructor"""
        self._solution = solution
        self._subcase = subcase
        self._iteration = iteration
        self._resultType = resultType
        self._identifier = identifier

    def __repr__(self) -> str:
        """String representation of a PostInput"""
        return "Solution: " + self._solution + " Subcase: " + str(self._subcase) + " Iteration: " + str(self._iteration) + " ResultType: " + self._resultType + " Identifier: " + self._identifier


def get_solution(solution_name: str) -> NXOpen.CAE.SimSolution:
    """This function returns the SimSolution object with the given name.

    Parameters
    ----------
    solution_name: str
        The name of the solution to return. Case insensitive.

    Returns
    -------
    NXOpen.CAE.SimSolution
        Returns a list of SolutionResult.
    """
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part) # explicit casting makes it clear
    sim_simulation: NXOpen.CAE.SimSimulation = sim_part.Simulation

    sim_solutions: List[NXOpen.CAE.SimSolution] = [item for item in sim_simulation.Solutions if item.Name.lower() == solution_name.lower()]
    if len(sim_solutions) == 0:
        return None
    
    return sim_solutions[0]


def load_results(post_inputs: List[PostInput], reference_type: str = "Structural") -> List[NXOpen.CAE.SolutionResult]:
    """Loads the results for the given list of PostInput and returns a list of SolutionResult.
    An exception is raised if the result does not exist (-> to check if CreateReferenceResult raises error or returns None)

    Parameters
    ----------
    post_inputs: List[PostInput]
        The result of each of the provided solutions is loaded.
    reference_type: str
        The type of SimResultReference eg. Structural. Defaults to structral

    Returns
    -------
    NXOpen.CAE.SolutionResult
        Returns a list of SolutionResult.
    """
    solution_results: List[NXOpen.CAE.SolutionResult] = [NXOpen.CAE.SolutionResult] * len(post_inputs)
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part)

    for i in range(len(post_inputs)):
        sim_solution: NXOpen.CAE.SimSolution = get_solution(post_inputs[i]._solution)
        sim_result_reference: NXOpen.CAE.SimResultReference = cast(NXOpen.CAE.SimResultReference, sim_solution.Find(reference_type))

        try:
            # SolutionResult[filename_solutionname]
            solution_results[i] = cast(NXOpen.CAE.SolutionResult, the_session.ResultManager.FindObject("SolutionResult[" + sys.Path.GetFileName(simPart.FullPath) + "_" + sim_solution.Name + "]"))
        except:
            solution_results[i] = the_session.ResultManager.CreateReferenceResult(sim_result_reference)

    return solution_results


def get_results_units(base_result_types: List[NXOpen.CAE.BaseResultType]) -> List[NXOpen.Unit]:
    """This funciton returns the unit of the first component in each resulttype.
       Note that the unit is taken from the SolutionResult and not the SimSolution!

    Parameters
    ----------
    base_result_types: List[NXOpen.CAE.BaseResultType]
        The list of baseresulttypes defining the result

    Returns
    -------
    NXOpen.Unit
        A list of unit for each resulttype
    """
    result_component_mapping = get_result_component_names()

    result_units: List[NXOpen.Unit] = [NXOpen.Unit] * len(base_result_types)
    for i in range(len(base_result_types)):
        components: List[NXOpen.CAE.Result.Component] = base_result_types[i].AskComponents()
        result_units[i] = base_result_types[i].AskDefaultUnitForComponent(components[1][0])

    return result_units


def get_result_types(post_inputs: List[PostInput], solution_results: List[NXOpen.CAE.SolutionResult]) -> List[NXOpen.CAE.BaseResultType]:
    """Helper function for CombineResults and GetResultParameters.
    Returns the ResultTypes specified in PostInputs

    Parameters
    ----------
    postInputs: List[PostInput]
        The input as an array of PostInput.
    solutionResults: List[NXOpen.CAE.SolutionResult]
        The already loaded results to search through for the results.

    Returns
    -------
    List[NXOpen.CAE.BaseResultType]
        Returns the result objects
    """
    result_types: List[NXOpen.CAE.BaseResultType] = [NXOpen.CAE.BaseResultType] * len(post_inputs)
    for i in range(len(post_inputs)):
        base_load_cases: List[NXOpen.CAE.BaseLoadcase] = solution_results[i].GetLoadcases()
        loadCase: NXOpen.CAE.Loadcase = cast(NXOpen.CAE.Loadcase, base_load_cases[post_inputs[i]._subcase - 1]) # user starts counting at 1
        base_iterations: List[NXOpen.CAE.BaseIteration] = loadCase.GetIterations()
        iteration: NXOpen.CAE.Iteration = cast(NXOpen.CAE.Iteration, base_iterations[post_inputs[i]._iteration - 1]) # user starts counting at 1
        base_result_types: List[NXOpen.CAE.BaseResultType] = iteration.GetResultTypes()
        base_result_type: List[NXOpen.CAE.ResultType] = [item for item in base_result_types if item.Name.lower().strip() == post_inputs[i]._resultType.lower().strip()][0]
        result_types[i] = cast(NXOpen.CAE.ResultType, base_result_type)
    
    return result_types


def get_sim_result_reference(solution_name: str, reference_type: str = "Structural") -> NXOpen.CAE.SimResultReference:
    """Helper function for CombineResults and EnvelopeResults.
    Returns the SimResultReferece for the given solution

    Parameters
    ----------
    solution_name: str
        The solution for which to get the "structural" SimResultReference.
    reference_type: str
        The type of SimResultReference eg. Structural. Defaults to structral

    Returns
    -------
    NXOpen.CAE.SimResultReference
        Returns the "Structural" simresultreference.
    """
    simSolution: NXOpen.CAE.SimSolution = get_solution(solution_name)
    if simSolution == None:
        # solution with given name not found
        the_lw.WriteFullline("GetSimResultReference: Solution with name " + solution_name + " not found.")
        return None
    simResultReference: NXOpen.CAE.SimResultReference = cast(NXOpen.CAE.SimResultReference, simSolution.Find(reference_type))
    return simResultReference


def create_full_path(file_name: str, extension: str = ".unv") -> str:
    """This function takes a filename and adds the .unv extension and path of the part if not provided by the user.
    If the fileName contains an extension, this function leaves it untouched, othwerwise adds .unv as extension.
    If the fileName contains a path, this function leaves it untouched, otherwise adds the path of the BasePart as the path.
    Undefined behaviour if basePart has not yet been saved (eg FullPath not available)

    Parameters
    ----------
    file_name: str
        The filename with or without path and .unv extension.

    Returns
    -------
    str
        A string with .unv extension and path of the basePart if the fileName parameter did not include a path.
    """
    # check if an extension is included
    if os.path.splitext(file_name)[1] == "":
        file_name = file_name + extension

    # check if path is included in fileName, if not add path of the .sim file
    unv_file_path: str = os.path.dirname(file_name)
    if unv_file_path == "":
        # if the .sim file has never been saved, the next will give an error
        file_name = os.path.join(os.path.dirname(base_part.FullPath), file_name)

    return file_name


def check_post_input(post_inputs: List[PostInput]) -> None:
    """Check if the provided list of PostInput will not return an error when used in CombineResults.
    Identifiers are checked with separate function check_post_input_identifiers
    Raises exceptions which can be caught by the user.

    Parameters
    ----------
    post_inputs: List[PostInput]
        The array of PostInput to check.
    """
    for i in range(len(post_inputs)):
        # Does the solution exist?
        sim_solution: NXOpen.CAE.SimSolution = get_solution(post_inputs[i]._solution)
        if sim_solution == None:
            the_lw.WriteFullline("Error in input " + str(post_inputs[i]))
            the_lw.WriteFullline("Solution with name " + post_inputs[i]._solution + " not found.")   
            raise ValueError("Solution with name " + post_inputs[i]._solution + " not found")
        
        # Does the result exist?
        solution_result: List[NXOpen.CAE.SolutionResult] = []
        try:
            solution_result = load_results([post_inputs[i]])
        except:
            the_lw.WriteFullline("Error in input " + str(post_inputs[i]))
            the_lw.WriteFullline("No result for Solution with name " + post_inputs[i]._solution)   
            raise
        
        # Does the subcase exist?
        base_load_cases: List[NXOpen.CAE.BaseLoadcase] = solution_result[0].GetLoadcases()
        loadCase: NXOpen.CAE.Loadcase = None
        try:
            loadCase = cast(NXOpen.CAE.Loadcase, base_load_cases[post_inputs[i]._subcase - 1]) # user starts counting at 1
        except:
            the_lw.WriteFullline("Error in input " + str(post_inputs[i]))
            the_lw.WriteFullline("SubCase with number " + str(post_inputs[i]._subcase) + " not found in solution with name " + post_inputs[i]._solution)
            raise

        # Does the iteration exist?
        base_iterations: List[NXOpen.CAE.BaseIteration] = loadCase.GetIterations()
        iteration: NXOpen.CAE.Iteration = None
        try:
            iteration = cast(NXOpen.CAE.Iteration, base_iterations[post_inputs[i]._iteration - 1]) # user starts counting at 1
        except:
            the_lw.WriteFullline("Error in input " + str(post_inputs[i]))
            the_lw.WriteFullline("Iteration number " + str(post_inputs[i]._iteration) + "not found in SubCase with number " + str(post_inputs[i]._subcase) + " in solution with name " + post_inputs[i]._solution) 
            raise

        # Does the ResultType exist?
        base_result_types: List[NXOpen.CAE.BaseResultType] = iteration.GetResultTypes()
        base_result_type: List[NXOpen.CAE.BaseResultType] = [item for item in base_result_types if item.Name.lower().strip() == post_inputs[i]._resultType.lower().strip()]
        if len(base_result_type) == 0:
            # resulttype does not exist
            the_lw.WriteFullline("Error in input " + str(post_inputs[i]))
            the_lw.WriteFullline("ResultType " + post_inputs[i]._resultType + "not found in iteration number " + str(post_inputs[i]._iteration) + " in SubCase with number " + str(post_inputs[i]._subcase) + " in solution with name " + post_inputs[i]._solution)
            for result_type in base_result_types:
                the_lw.WriteFullline(result_type.UserName)
            raise ValueError("ResultType " + post_inputs[i]._resultType + "not found in iteration number " + str(post_inputs[i]._iteration) + " in SubCase with number " + str(post_inputs[i]._subcase) + " in solution with name " + post_inputs[i]._solution)


def check_post_input_identifiers(post_inputs: List[PostInput]) -> None:
    """This function verifies the identifiers in all post_inputs:
        Null or empty string.
        Reserved expression name.
        Use of an expression which already exists.

    Parameters
    ----------
    post_inputs: List[PostInput]
        The array of PostInput to check.
    """
    for i in range(len(post_inputs)):
        # is the identifier not null
        if post_inputs[i]._identifier == "":
            the_lw.WriteFullline("Error in input " + str(post_inputs[i]))
            the_lw.WriteFullline("No identifier provided for solution " + post_inputs[i]._solution + " SubCase " + str(post_inputs[i]._subcase) + " iteration " + str(post_inputs[i]._iteration) + " ResultType " + post_inputs[i]._resultType) 
            raise ValueError("No identifier provided for solution " + post_inputs[i]._solution + " SubCase " + str(post_inputs[i]._subcase) + " iteration " + str(post_inputs[i]._iteration) + " ResultType " + post_inputs[i]._resultType)

        # check for reserved expressions
        nx_reserved_expressions: List[str] = ["angle", "angular velocity", "axial", "contact pressure", "Corner ID", "depth", "dynamic viscosity", "edge_id", "element_id", "face_id", "fluid", "fluid temperature", "frequency", "gap distance", "heat flow rate", "iter_val", "length", "mass density", "mass flow rate", "node_id", "nx", "ny", "nz", "phi", "pressure", "radius", "result", "rotational speed", "solid", "solution", "specific heat", "step", "temperature", "temperature difference", "thermal capacitance", "thermal conductivity", "theta", "thickness", "time", "u", "v", "velocity", "volume flow rate", "w", "x", "y", "z"]
        check: List[str] = [item for item in nx_reserved_expressions if item.lower() == post_inputs[i]._identifier.lower()]
        if len(check) != 0:
            the_lw.WriteFullline("Error in input " + str(post_inputs[i]))
            the_lw.WriteFullline("Expression with name " + post_inputs[i]._identifier + " is a reserved expression in nx and cannot be used as an identifier.");  
            raise ValueError("Expression with name " + post_inputs[i]._identifier + " is a reserved expression in nx and cannot be used as an identifier.")

        # check if identifier is not already in use as an expression
        expressions: List[NXOpen.Expression] = [item for item in base_part.Expressions if item.Name.lower() == post_inputs[i]._identifier.lower()]
        if len(expressions) != 0:
            the_lw.WriteFullline("Error in input " + str(post_inputs[i]))
            the_lw.WriteFullline("Expression with name " + post_inputs[i]._identifier + " already exist in this part and cannot be used as an identifier.")
            raise ValueError("Expression with name " + post_inputs[i]._identifier + " already exist in this part and cannot be used as an identifier.")


def check_unv_file_name(unv_file_name: str) -> None:
    """This method loops through all solutions and all companion results in these solutions.
    It checks if the file name is not already in use by another companion result.
    And throws an error if so.

    Parameters
    ----------
    unv_file_name: str
        The file name to look for.
    """

    # Don't perform checks on the file itself in the file system!
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part)
    # loop through all solutions
    solutions: List[NXOpen.CAE.SimSolution] = sim_part.Simulation.Solutions.ToArray()
    for i in range(len(solutions)):
        sim_result_reference: NXOpen.CAE.SimResultReference = get_sim_result_reference(solutions[i].Name)
        # loop through each companion result
        companion_results: List[NXOpen.CAE.CompanionResult] = sim_result_reference.CompanionResults.ToArray()
        for j in range(len(companion_results)):
            # create the builder with the companion result, so can access the CompanionResultsFile
            companion_result_builder: NXOpen.CAE.CompanionResultBuilder = sim_result_reference.CompanionResults.CreateCompanionResultBuilder(companion_results[j])
            if (companion_result_builder.CompanionResultsFile.lower() == unv_file_name.lower()):
                # the file is the same, so throw exception
                raise ValueError("Companion results file name " + unv_file_name + " is already used by companion result " + companion_results[j].Name)


def get_full_result_names(post_inputs: List[PostInput], solution_results: List[NXOpen.CAE.SolutionResult]) -> List[str]:
    """This function returns a representation of the Results used in PostInputs.
    Note that the representation is taken from the SolutionResult and not the SimSolution!

    Parameters
    ----------
    post_inputs: List[PostInput]
        The list of PostInput defining the results.
    solution_results: List[NXOpen.CAE.SolutionResult]
        The solution results from which the representation is obtained.

    Returns
    -------
    List[str]
        List of string with each representation.
    """
    full_result_names: List[str] = [""] * len(post_inputs)
    for i in range(len(post_inputs)):
        full_result_names[i] = full_result_names[i] + solution_results[i].Name
        base_load_cases: List[NXOpen.CAE.BaseLoadcase] = solution_results[i].GetLoadcases()
        loadCase: NXOpen.CAE.Loadcase = cast(NXOpen.CAE.Loadcase, base_load_cases[post_inputs[i]._subcase - 1]) # user starts counting at 1
        full_result_names[i] = full_result_names[i] + "::" + loadCase.Name

        base_iterations: List[NXOpen.CAE.BaseIteration] = loadCase.GetIterations()
        iteration: NXOpen.CAE.Iteration = cast(NXOpen.CAE.Iteration, base_iterations[post_inputs[i]._iteration - 1]) # user starts counting at 1
        full_result_names[i] = full_result_names[i] + "::" + iteration.Name

        base_result_types: List[NXOpen.CAE.BaseResultType] = iteration.GetResultTypes()
        base_result_type: List[NXOpen.CAE.BaseResultType] = [item for item in base_result_types if item.Name.lower().strip() == post_inputs[i]._resultType.lower().strip()][0]
        resultType: NXOpen.CAE.ResultType = cast(NXOpen.CAE.ResultType, base_result_type)
        full_result_names[i] = full_result_names[i] + "::" + resultType.Name
    
    return full_result_names


def export_result(post_input: PostInput, unv_file_name: str, si_units: bool = False) -> None:
    """Export a single result to universal file."""
    if not isinstance(base_part, NXOpen.CAE.SimPart):
        the_lw.WriteFullline("ExportResult needs to start from a .sim file. Exiting")
        return
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part)

    post_input_list: List[PostInput] = [post_input]
    # check input and catch errors so that the user doesn't get a error pop-up in SC
    try:
        check_post_input(post_input_list)
    
    except ValueError as e:
        # internal raised exceptions are raised as valueError
        the_lw.WriteFullline("Did not execute ExportResult due to input error. Please check the previous messages.")
        # we still return the tehcnical message as an additional log
        the_lw.WriteFullline(str(e))
        return
    except:
        the_lw.WriteFullline("Did not execute ExportResult due to general error. Please check the previous messages.")
        # we still return the tehcnical message as an additional log
        the_lw.WriteFullline(str(e))
        return
    
    # Make sure the file is complete with path and extension
    unv_full_name: str = create_full_path(unv_file_name)

    # Load the results and store them in a list
    solution_results: List[NXOpen.CAE.SolutionResult] = load_results(post_input_list)

    # get all ResultType objects as defined in postInputs and store them in a list
    result_types: List[NXOpen.CAE.BaseResultType] = get_result_types(post_input_list, solution_results)
    
    # get all identifiers in postInputs and store them in a list, using list comprehension
    identifiers: List[str] = ["nxopenexportresult"]

    # get the full result names for user feedback. Do this before the try except block, otherwise the variable is no longer available
    full_result_names: List[str] = get_full_result_names(post_input_list, solution_results)

    # get the unit for each resultType from the result itself
    resultUnits: List[NXOpen.Unit]  = get_results_units(result_types)

    results_combination_builder = the_session.ResultManager.CreateResultsCombinationBuilder()
    results_combination_builder.SetResultTypes(result_types, identifiers, resultUnits)
    results_combination_builder.SetFormula("nxopenexportresult")
    results_combination_builder.SetOutputResultType(NXOpen.CAE.ResultsManipulationBuilder.OutputResultType.Full)
    results_combination_builder.SetIncludeModel(False)
    results_combination_builder.SetOutputQuantity(result_types[0].Quantity)
    results_combination_builder.SetOutputName(full_result_names[0])
    results_combination_builder.SetLoadcaseName(full_result_names[0])
    results_combination_builder.SetOutputFile(unv_full_name)
    results_combination_builder.SetIncompatibleResultsOption(NXOpen.CAE.ResultsCombinationBuilder.IncompatibleResults.Skip)
    results_combination_builder.SetNoDataOption(NXOpen.CAE.ResultsCombinationBuilder.NoData.Skip)
    results_combination_builder.SetEvaluationErrorOption(NXOpen.CAE.ResultsCombinationBuilder.EvaluationError.Skip)

    # The following 2 lines have no effect if SetIncludeModel is set to false
    # If SetIncludeModel is true these 2 lines adds dataset 164 to the .unv file
    # resultsCombinationBuilder.SetUnitsSystem(NXOpen.CAE.ResultsManipulationBuilder.UnitsSystem.FromResult)
    # resultsCombinationBuilder.SetUnitsSystemResult(solutionResults[0])

    if si_units:
        # in case you want to set a userdefined units system
        user_defined_unit_system: NXOpen.CAE.Result.ResultBasicUnit = NXOpen.CAE.Result.ResultBasicUnit()
        units: List[NXOpen.Unit] = sim_part.UnitCollection
        # # Prints a list of all available units
        # for item in units:
        #     the_lw.WriteFullline(item.TypeName)

        user_defined_unit_system.AngleUnit = [item for item in units if item.TypeName == "Radian"][0]
        user_defined_unit_system.LengthUnit = [item for item in units if item.TypeName == "Meter"][0]
        user_defined_unit_system.MassUnit = [item for item in units if item.TypeName == "Kilogram"][0]
        user_defined_unit_system.TemperatureUnit = [item for item in units if item.TypeName == "Celsius"][0]
        user_defined_unit_system.ThermalenergyUnit = [item for item in units if item.TypeName == "ThermalEnergy_Metric1"][0]
        user_defined_unit_system.TimeUnit = [item for item in units if item.TypeName == "Second"][0]
        results_combination_builder.SetUnitsSystem(NXOpen.CAE.ResultsManipulationBuilder.UnitsSystem.UserDefined)
        results_combination_builder.SetUserDefinedUnitsSystem(user_defined_unit_system)
        # if set to false, dataset 164 is not added and the results are ambiguos for external use
        results_combination_builder.SetIncludeModel(True)

    try:
        results_combination_builder.Commit()
        the_lw.WriteFullline("Exported result:")
        the_lw.WriteFullline(full_result_names[0])
                
    except Exception as e:
        the_lw.WriteFullline("Error in ExportResult:")
        the_lw.WriteFullline(str(e))
        raise

    finally:
        results_combination_builder.Destroy()

        expressions: List[NXOpen.Expression] = sim_part.Expressions
        for i in range(len(identifiers)):
            check: NXOpen.Expression = [item for item in expressions if item.Name.lower() == identifiers[i].lower()]
            if len(check) != 0:
                # expression found, thus deleting
                sim_part.Expressions.Delete(check[0])


def get_result_paramaters(result_types: List[NXOpen.CAE.BaseResultType], result_shell_section: NXOpen.CAE.Result.ShellSection, result_component: NXOpen.CAE.Result.Component, absolute: bool) -> List[NXOpen.CAE.ResultParameters]:
    result_parameter_list: List[NXOpen.CAE.ResultParameters] = [NXOpen.CAE.ResultParameters] * len(result_types)

    for i in range(len(result_parameter_list)):
        result_parameters: NXOpen.CAE.ResultParameters = the_session.ResultManager.CreateResultParameters()
        result_parameters.SetGenericResultType(result_types[i])
        result_parameters.SetShellSection(result_shell_section)
        result_parameters.SetResultComponent(result_component)
        result_parameters.SetSelectedResultCoordinateSystem(-1)
        result_parameters.MakeElementResult(False)

        # components: List[NXOpen.CAE.Result.Component] = resultTypes[i].AskComponents()
        result: Tuple[List[NXOpen.CAE.Result.Component], List[str]] = result_types[i].AskComponents()
        unit: NXOpen.Unit = result_types[i].AskDefaultUnitForComponent(result[0][0]) # [0] for the list of componentns and another [0] for the first componentn
        result_parameters.SetUnit(unit)

        result_parameters.SetAbsoluteValue(absolute)
        result_parameters.SetTensorComponentAbsoluteValue(NXOpen.CAE.Result.TensorDerivedAbsolute.DerivedComponent)

        result_parameter_list[i] = result_parameters
    
    return result_parameter_list


def get_result_component_names() -> Dict[int, str]:
    """
    Get the names of the available result components in order to give meaningful feedback

    Returns
    -------
    Dict[int, str]
       A dictionary with the int value and the string value of the result component 

    Notes
    -----
    Warning: this assumes that the enum is ordered according the values by the NXOpen developers!!
    Tested in SC2212

    """
    values = list(NXOpen.CAE.Result.Component.__dict__)
    mapping = {}
    for i in range(0, len(values)):
        # the_lw.WriteFullline(values[i] + ': ' + str(NXOpen.CAE.ResultsManipulationEnvelopeBuilder.Operation.ValueOf(i)))
        mapping[i] = values[i]
    
    # for key, value in mapping.items():
    #     the_lw.WriteFullline(str(key) + ': ' + value)
    return mapping


def main() :
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)
    
    if not type(base_part) is NXOpen.CAE.SimPart:
        the_lw.WriteFullline("This script needs to start from a .sim file. Exiting")
        return
    
    sim_solutions: List[NXOpen.CAE.SimSolution] = cast(NXOpen.CAE.SimPart, base_part).Simulation.Solutions


    for solution in sim_solutions:
        export_inputs: List[PostInput] = [PostInput("", -1, -1, "")] * solution.StepCount # declare the list with the correct length
        for i in range(len(export_inputs)):
            export_inputs[i] = PostInput(solution.Name, i + 1, 1, "Stress - Element-Nodal")
    
        for item in export_inputs:
            export_result(item, item._solution + "_" + str(item._subcase), True)
    

if __name__ == '__main__':
    main()
