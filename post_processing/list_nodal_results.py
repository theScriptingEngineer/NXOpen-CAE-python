import sys
import os
import math
import NXOpen
import NXOpen.UF
import NXOpen.CAE
from typing import List, cast, Tuple

the_session: NXOpen.Session = NXOpen.Session.GetSession()
base_part = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow

the_uf_session: NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()


class PostInput:
    """A class for declaring inputs used in CombineResults"""
    _solution: str
    _subcase: int
    _iteration: int
    _resultType: str
    _identifier: str

    def __init__(self) -> None: # type: ignore
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
        return None # type: ignore
    
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
            solution_results[i] = cast(NXOpen.CAE.SolutionResult, the_session.ResultManager.FindObject("SolutionResult[" + (os.path.basename(simPart.FullPath) + "_" + sim_solution.Name + "]")))
        except:
            solution_results[i] = the_session.ResultManager.CreateReferenceResult(sim_result_reference)

    return solution_results


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


def get_result_paramaters(result_types: List[NXOpen.CAE.BaseResultType], result_shell_section: NXOpen.CAE.Result.ShellSection, result_component: NXOpen.CAE.Result.Component, absolute: bool) -> List[NXOpen.CAE.ResultParameters]:
    result_parameter_list: List[NXOpen.CAE.ResultParameters] = [NXOpen.CAE.ResultParameters] * len(result_types)

    for i in range(len(result_parameter_list)):
        result_parameters: NXOpen.CAE.ResultParameters = the_session.ResultManager.CreateResultParameters()
        result_parameters.SetGenericResultType(result_types[i])
        result_parameters.SetShellSection(result_shell_section)
        result_parameters.SetResultComponent(result_component)
        # result_parameters.SetSelectedCoordinateSystem(NXOpen.CAE.Result.CoordinateSystem.None, -1)
        result_parameters.MakeElementResult(False)

        # components: List[NXOpen.CAE.Result.Component] = resultTypes[i].AskComponents()
        result: Tuple[List[NXOpen.CAE.Result.Component], List[str]] = result_types[i].AskComponents() # type: ignore
        unit: NXOpen.Unit = result_types[i].AskDefaultUnitForComponent(result_component)
        result_parameters.SetUnit(unit)

        result_parameters.SetAbsoluteValue(absolute)
        result_parameters.SetTensorComponentAbsoluteValue(NXOpen.CAE.Result.TensorDerivedAbsolute.DerivedComponent)

        result_parameter_list[i] = result_parameters
    
    return result_parameter_list


def list_nodal_values(solution_name: str, subcase: int, iteration: int, result_type: str, node_label: int) -> None:
    """Lists nodal values for a given 

    Parameters
    ----------
    solution_name: string
        The name of the solution
    subcase: int
        The subcase number. User starts counting at 1
    iteration: int
        The iteration number. User starts counting at 1
    result_type: str
        The name of the result type to ask results (eg. "Reaction Force - Nodal")
    node_label: int
        The label of the node to get the result for.
    """
    post_input = PostInput(solution_name, subcase, iteration, result_type)  # Assuming PostInput is available in Python
    post_input_array = [post_input]
    solution_results = load_results(post_input_array)
    result = solution_results[0]
    result_types = get_result_types(post_input_array, solution_results)
    result_parameters = get_result_paramaters(result_types, NXOpen.CAE.Result.ShellSection.Maximum, NXOpen.CAE.Result.Component.Magnitude, False)
    result_access = the_session.ResultManager.CreateResultAccess(result, result_parameters[0])
    node_index = solution_results[0].AskNodeIndex(node_label)
    nodal_data = result_access.AskNodalResultAllComponents(node_index)
    
    # Printing is hard coded as X Y Z Magnitude
    the_lw.WriteFullline(f"X:\t{nodal_data[0]}\tY:\t{nodal_data[1]}\tZ:\t{nodal_data[2]}\tMagnitude:\t{nodal_data[3]}")


def list_element_nodal_values(solution_name, subcase, iteration, result_type, element_label):
    # still needs implementing
    pass
    # post_input = PostInput(solution_name, subcase, iteration, result_type)  # Assuming PostInput is available in Python
    # post_input_array = [post_input]
    # solution_results = load_results(post_input_array)
    # result = solution_results[0]
    # result_types = get_result_types(post_input_array, solution_results)
    # result_parameters = get_result_paramaters(result_types, NXOpen.CAE.Result.ShellSection.Maximum, NXOpen.CAE.Result.Component.Axial, False)
    # result_access = the_session.ResultManager.CreateResultAccess(result, result_parameters[0])
    # element_index = solution_results[0].AskElementIndex(element_label)
    
    # element_nodal_data: List[float] = result_access.AskElementNodalResultAllComponents(element_index)

    # # Get the number of nodes and from that the number of components
    # # All values will be returned as a single dimensional array.
    # # The array can be addressed as index = node_index*numComponents + component_index
    # num_components = 6
    # node_indexes = int(len(element_nodal_data) / num_components)
    
    # header = "{0:13}{1:13}{2:13}{3:13}{4:13}{5:13}{6:13}".format("ID:", "Nxx:", "Myy:", "Mzz:", "Mxx:", "Qxy:", "Qxz:")
    
    # the_lw.WriteFullline(header)
    
    # for i in range(node_indexes):
    #     node_label = i # solution_results[0].AskNodeLabel(node_indexes[i])
    #     values = ["{0:#.#####E+00}".format(element_nodal_data[i * num_components + j]) for j in range(num_components)]
    #     line = "{0:13}{1:13}{2:13}{3:13}{4:13}{5:13}{6:13}".format(node_label, *values)
    #     the_lw.WriteFullline(line)


def main() :
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)
    
    node_label = 2296551
    list_nodal_values("Position0", 1, 1, "Reaction Force - Nodal", node_label)
    list_nodal_values("Position0", 1, 1, "Reaction Moment - Nodal", node_label)

if __name__ == '__main__':
    main()
