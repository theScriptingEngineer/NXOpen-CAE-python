 # intellisense by theScriptingEngineer

import math
import sys
import os
import NXOpen
import NXOpen.CAE
import NXOpen.Fields
from typing import List, cast

theSession = NXOpen.Session.GetSession()
basePart: NXOpen.BasePart = theSession.Parts.BaseWork
theLW: NXOpen.ListingWindow = theSession.ListingWindow

class PostInput:
    """A class for declaring inputs used in CombineResults"""
    Solution: str
    Subcase: int
    Iteration: int
    ResultType: str
    Identifier: str

    def __init__(self) -> None:
        """Parameterless constructor. Strings initialized to empty strings and integers to -1"""
        self.Solution = ""
        self.Subcase = -1
        self.Iteration = -1
        self.ResultType = ""
        self.Identifier = ""
    
    def __init__(self, solution: str, subcase: int, iteration: int, resultType: str, identifier: str):
        """Constructor"""
        self.Solution = solution
        self.Subcase = subcase
        self.Iteration = iteration
        self.ResultType = resultType
        self.Identifier - identifier

    def ToString(self) -> str:
        """String representation of a PostInput"""
        return "Solution: " + self.Solution + " Subcase: " + str(self.Subcase) + " Iteration: " + str(self.Iteration) + " ResultType: " + self.ResultType + " Identifier: " + self.Identifier


def GetSolution(solutionName: str) -> NXOpen.CAE.SimSolution:
    """This function returns the SimSolution object with the given name.
    Returns None if not foune, so the user can check and act accordingly
    """
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart) # explicit casting makes it clear
    simSimulation: NXOpen.CAE.SimSimulation = simPart.Simulation

    simSolution: List[NXOpen.CAE.SimSolution] = [item for item in simSimulation.Solutions if item.Name.lower() == solutionName.lower()]
    if len(simSolution) == 0:
        return None
    
    return simSolution[0]

def LoadResults(postInputs: List[PostInput]) -> NXOpen.CAE.SolutionResult:
    """Loads the results for the given list of PostInput and returns a list of SolutionResult.
    An exception is raised if the result does not exist (-> to check if CreateReferenceResult raises error or returns None)
    """
    solutionResults: List[NXOpen.CAE.SolutionResult] = [NXOpen.CAE.SolutionResult] * len(postInputs)
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart)

    for i in range(len(postInputs)):
        simSolution: NXOpen.CAE.SimSolution = GetSolution(postInputs[i].Solution)
        simResultReference: NXOpen.CAE.SimResultReference = cast(NXOpen.CAE.SimResultReference, simSolution.Find("Structural"))

        try:
            # SolutionResult[filename_solutionname]
            solutionResults[i] = cast(NXOpen.CAE.SolutionResult, theSession.ResultManager.FindObject("SolutionResult[" + sys.Path.GetFileName(simPart.FullPath) + "_" + simSolution.Name + "]"))
        except:
            solutionResults[i] = theSession.ResultManager.CreateReferenceResult(simResultReference)

    return solutionResults


def GetResultTypes(postInputs: List[PostInput], solutionResults: List[NXOpen.CAE.SolutionResult]) -> List[NXOpen.CAE.BaseResultType]:
    """Obtain the ResultTypes from the results file"""
    resultTypes: List[NXOpen.CAE.BaseResultType] = [NXOpen.CAE.BaseResultType] * len(postInputs)
    for i in range(len(postInputs)):
        baseLoadCases: List[NXOpen.CAE.BaseLoadcase] = solutionResults[i].GetLoadcases()
        loadCase: NXOpen.CAE.Loadcase = cast(NXOpen.CAE.Loadcase, baseLoadCases[postInputs[i].Subcase - 1]) # user starts counting at 1
        baseIterations: List[NXOpen.CAE.BaseIteration] = loadCase.GetIterations()
        iteration: NXOpen.CAE.Iteration = cast(NXOpen.CAE.Iteration, baseIterations[postInputs[i] - 1]) # user starts counting at 1
        baseResultTypes: List[NXOpen.CAE.BaseResultType] = iteration.GetResultTypes()
        baseResultType: List[NXOpen.CAE.ResultType] = [item for item in baseResultTypes if item.Name.lower().strip() == postInputs[i].ResultType.lower().strip()][0]
        resultTypes[i] = cast(NXOpen.CAE.ResultType, baseResultType)
    
    return resultTypes


def DeleteCompanionResult(solutionName: str, companionResultName: str, referenceType: str = "Structural") -> None:
    """Delete a companion result with the given name in the given solution. Defaults to a structral result"""
    simSolution: NXOpen.CAE.SimSolution = GetSolution(solutionName)
    simResultReference: NXOpen.CAE.SimResultReference = cast(NXOpen.CAE.SimResultReference, simSolution.Find(referenceType))
    companionResult: List[NXOpen.CAE.CompanionResult] = [item for item in simResultReference.CompanionResults if item.Name.lower() == companionResultName.lower()]
    if len(companionResult) != 0:
        # companion result exists, delete it
        simResultReference.CompanionResults.Delete(companionResult[0])


def GetSimResultReference(solutionName: str, referenceType: str = "Structural") -> NXOpen.CAE.SimResultReference:
    """Get the SimResultReference for a given solution. Defualts to the Structural SimResultReference."""
    simSolution: NXOpen.CAE.SimSolution = GetSolution(solutionName)
    if simSolution == None:
        # solution with given name not found
        theLW.WriteFullline("GetSimResultReference: Solution with name " + solutionName + " not found.")
        return None
    simResultReference: NXOpen.CAE.SimResultReference = cast(NXOpen.CAE.SimResultReference, simSolution.Find(referenceType))
    return simResultReference

def CreateFullPath(fileName: str) -> str:
    """Checks if .unv extension if present and adds if not.
    Checks if path is present and adds path of basepart if not.
    Undefined behaviour if basePart has not yet been saved (eg FullPath not available)
    """
    # check if .unv is included in fileName
    if os.path.splitext(fileName)[1] != ".unv":
        fileName = fileName + ".unv"

    # check if path is included in fileName, if not add path of the .sim file
    unvFilePath: str = os.path.dirname(fileName)
    if unvFilePath == "":
        # if the .sim file has never been saved, the next will give an error
        fileName = os.path.join(os.path.dirname(basePart.FullPath), fileName)

    return fileName


def CheckPostInput(postInputs: List[PostInput]) -> None:
    """Check if the provided list of PostInput will not return an error when used in CombineResults.
    Identifiers are checked with separate function CheckPostInputIdentifiers
    Raises exceptions which can be caught by the user.
    """
    for i in range(len(postInputs)):
        # Does the solution exist?
        simSolution: NXOpen.CAE.SimSolution = GetSolution(postInputs[i].Solution)
        if simSolution == None:
            theLW.WriteFullline("Error in input " + postInputs[i].ToString())
            theLW.WriteFullline("Solution with name " + postInputs[i].Solution + " not found.")   
            raise ValueError("Solution with name " + postInputs[i].Solution + " not found")
        
        # Does the result exist?
        solutionResult: List[NXOpen.CAE.SolutionResult] = []
        try:
            solutionResult = LoadResults([postInputs[i]])
        except:
            theLW.WriteFullline("Error in input " + postInputs[i].ToString())
            theLW.WriteFullline("No result for Solution with name " + postInputs[i].Solution)   
            raise
        
        # Does the subcase exist?
        baseLoadCases: List[NXOpen.CAE.BaseLoadcase] = solutionResult[0].GetLoadcases()
        loadCase: NXOpen.CAE.Loadcase = None
        try:
            loadCase = cast(NXOpen.CAE.Loadcase, baseLoadCases[postInputs[i].Subcase - 1]) # user starts counting at 1
        except:
            theLW.WriteFullline("Error in input " + postInputs[i].ToString())
            theLW.WriteFullline("SubCase with number " + postInputs[i].Subcase.ToString() + " not found in solution with name " + postInputs[i].Solution)
            raise

        # Does the iteration exist?
        baseIterations: List[NXOpen.CAE.BaseIteration] = loadCase.GetIterations()
        iteration: NXOpen.CAE.Iteration = None
        try:
            iteration = cast(NXOpen.CAE.Iteration, baseIterations[postInputs[i].Iteration - 1]) # user starts counting at 1
        except:
            theLW.WriteFullline("Error in input " + postInputs[i].ToString())
            theLW.WriteFullline("Iteration number " + postInputs[i].Iteration.ToString() + "not found in SubCase with number " + postInputs[i].Subcase.ToString() + " in solution with name " + postInputs[i].Solution) 
            raise

        # Does the ResultType exist?
        baseResultTypes: List[NXOpen.CAE.BaseResultType] = iteration.GetResultTypes()
        baseResultType: List[NXOpen.CAE.BaseResultType] = [item for item in baseResultTypes if item.Name.lower().strip() == postInputs[i].ResultType.lower().strip]
        if len(baseResultType) == 0:
            # resulttype does not exist
            theLW.WriteFullline("Error in input " + postInputs[i].ToString())
            theLW.WriteFullline("ResultType " + postInputs[i].ResultType + "not found in iteration number " + postInputs[i].Iteration.ToString() + " in SubCase with number " + postInputs[i].Subcase.ToString() + " in solution with name " + postInputs[i].Solution)
            raise ValueError("ResultType " + postInputs[i].ResultType + "not found in iteration number " + postInputs[i].Iteration.ToString() + " in SubCase with number " + postInputs[i].Subcase.ToString() + " in solution with name " + postInputs[i].Solution)


def CheckPostInputIdentifiers(postInputs: List[PostInput]) -> None:
    """Check if the provided list of PostInput will not return an error with respect to the Identifier when used in CombineResults.
    Raises exceptions which can be caught by the user.
    """
    for i in range(len(postInputs)):
        # is the identifier not null
        if postInputs[i].Identifier == "":
            theLW.WriteFullline("Error in input " + postInputs[i].ToString())
            theLW.WriteFullline("No identifier provided for solution " + postInputs[i].Solution + " SubCase " + postInputs[i].Subcase.ToString() + " iteration " + postInputs[i].Iteration.ToString() + " ResultType " + postInputs[i].ResultType) 
            raise ValueError("No identifier provided for solution " + postInputs[i].Solution + " SubCase " + postInputs[i].Subcase.ToString() + " iteration " + postInputs[i].Iteration.ToString() + " ResultType " + postInputs[i].ResultType)

        # check for reserved expressions
        nxReservedExpressions: List[str] = ["angle", "angular velocity", "axial", "contact pressure", "Corner ID", "depth", "dynamic viscosity", "edge_id", "element_id", "face_id", "fluid", "fluid temperature", "frequency", "gap distance", "heat flow rate", "iter_val", "length", "mass density", "mass flow rate", "node_id", "nx", "ny", "nz", "phi", "pressure", "radius", "result", "rotational speed", "solid", "solution", "specific heat", "step", "temperature", "temperature difference", "thermal capacitance", "thermal conductivity", "theta", "thickness", "time", "u", "v", "velocity", "volume flow rate", "w", "x", "y", "z"]
        check: List[str] = [item for item in nxReservedExpressions if item.lower() == postInputs[i].Identifier.lower()]
        if len(check) != 0:
            theLW.WriteFullline("Error in input " + postInputs[i].ToString());
            theLW.WriteFullline("Expression with name " + postInputs[i].Identifier + " is a reserved expression in nx and cannot be used as an identifier.");  
            raise ValueError("Expression with name " + postInputs[i].Identifier + " is a reserved expression in nx and cannot be used as an identifier.")

        # check if identifier is not already in use as an expression
        expressions: List[NXOpen.Expression] = [item for item in basePart.Expressions if item.Name.lower() == postInputs[i].Identifier.lower()]
        if len(expressions) != 0:
            theLW.WriteFullline("Error in input " + postInputs[i].ToString())
            theLW.WriteFullline("Expression with name " + postInputs[i].Identifier + " already exist in this part and cannot be used as an identifier.")
            raise ValueError("Expression with name " + postInputs[i].Identifier + " already exist in this part and cannot be used as an identifier.")


def GetFullResultNames(postInputs: List[PostInput], solutionResults: List[NXOpen.CAE.SolutionResult]) -> List[str]:
    """Get a list of the Solution::Subcase::Iteration::ResultType for each PostInput.
    The names are obtained from the results file itself.
    """
    fullResultNames: List[str] = [str] * len(postInputs)
    for i in range(len(postInputs)):
        fullResultNames[i] = fullResultNames[i] + solutionResults[i].Name
        baseLoadCases: List[NXOpen.CAE.BaseLoadcase] = solutionResults[i].GetLoadcases()
        loadCase: NXOpen.CAE.Loadcase = cast(NXOpen.CAE.Loadcase, baseLoadCases[postInputs[i].Subcase - 1]) # user starts counting at 1
        fullResultNames[i] = fullResultNames[i] + "::" + loadCase.Name

        baseIterations: List[NXOpen.CAE.BaseIteration] = loadCase.GetIterations()
        iteration: NXOpen.CAE.Iteration = cast(NXOpen.CAE.Iteration, baseIterations[postInputs[i] - 1]) # user starts counting at 1
        fullResultNames[i] = fullResultNames[i] + "::" + iteration.Name

        baseResultTypes: List[NXOpen.CAE.BaseResultType] = iteration.GetResultTypes()
        baseResultType: List[NXOpen.CAE.BaseResultType] = [item for item in baseResultTypes if item.Name.lower().strip() == postInputs[i].ResultType.lower().strip()][0]
        resultType: NXOpen.CAE.ResultType = cast(NXOpen.CAE.ResultType, baseResultType)
        fullResultNames[i] = fullResultNames[i] + "::" + resultType.Name
    
    return fullResultNames


def CombineResults(postInputs: List[PostInput], formula: str, companionResultName: str, unvFileName: str, resultQuantity: NXOpen.CAE.Result.Quantity = NXOpen.CAE.Result.Quantity.Unknown, solutionName: str = "") -> None:
    """Combine results using the given list of PostInput and the settings in arguments."""
    if not isinstance(basePart, NXOpen.CAE.SimPart):
        theLW.WriteFullline("CombineResults needs to start from a .sim file. Exiting")
        return
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart)

    # check input and catch errors so that the user doesn't get a error pop-up in SC
    try:
        CheckPostInput(postInputs)
        CheckPostInputIdentifiers(postInputs)
    
    except ValueError as e:
        # internal raised exceptions are raised as valueError
        theLW.WriteFullline("Did not execute CombineResults due to input error. Please check the previous messages.")
        # we still return the tehcnical message as an additional log
        theLW.WriteFullline(e)
        return
    except:
        theLW.WriteFullline("Did not execute CombineResults due to general error. Please check the previous messages.")
        # we still return the tehcnical message as an additional log
        theLW.WriteFullline(e)
        return
    
    # Make sure the file is complete with path and extension
    unvFullName: str = CreateFullPath(unvFileName)

    # Select the solution to add the companion result to
    if GetSolution(solutionName) != None:
        # Delete the companion result if it exists and get the simresultreference
        DeleteCompanionResult(solutionName, companionResultName)
        # Get the SimResultReference to add the companion result to
        simResultReference: NXOpen.CAE.SimResultReference = GetSimResultReference(solutionName)
    else:
        if solutionName != "":
            # user provided solution but not found, adding to the first but give warning to user
            theLW.WriteFullline("Solution with name " + solutionName + " not found. Adding companion result to solution " + postInputs[0].Solution)
        
        # Delete the companion result if it exists and get the simresultreference to the first provided postInput
        DeleteCompanionResult(postInputs[0].Solution, companionResultName)
        # Get the SimResultReference to add the companion result to
        simResultReference: NXOpen.CAE.SimResultReference = GetSimResultReference(postInputs[0].Solution)

    # Load the results and store them in a list
    solutionResults: List[NXOpen.CAE.SolutionResult] = LoadResults(postInputs)

    # get all ResultType objects as defined in postInputs and store them in a list
    resultTypes: List[NXOpen.CAE.BaseResultType] = GetResultTypes(postInputs, solutionResults)
    
    # get all identifiers in postInputs and store them in a list, using list comprehension
    identifiers: List[str] = [item.Identifier for item in postInputs]

    resultsCombinationBuilder1 = theSession.ResultManager.CreateResultsCombinationBuilder()
    resultsCombinationBuilder1.SetResultTypes(resultTypes, identifiers)
    resultsCombinationBuilder1.SetFormula(formula)
    resultsCombinationBuilder1.SetOutputResultType(NXOpen.CAE.ResultsManipulationBuilder.OutputResultType.Companion)
    resultsCombinationBuilder1.SetIncludeModel(False)
    resultsCombinationBuilder1.SetCompanionResultReference(simResultReference)
    resultsCombinationBuilder1.SetCompanionIdentifier(companionResultName)
    resultsCombinationBuilder1.SetAppendMethod(NXOpen.CAE.ResultsManipulationBuilder.ResultAppendMethod.CreateNewLoadCases)
    resultsCombinationBuilder1.SetImportResult(True)
    resultsCombinationBuilder1.SetOutputQuantity(resultQuantity)
    resultsCombinationBuilder1.SetOutputName(companionResultName)
    resultsCombinationBuilder1.SetLoadcaseName(companionResultName)
    resultsCombinationBuilder1.SetOutputFile(unvFullName)
    resultsCombinationBuilder1.SetUnitsSystem(NXOpen.CAE.ResultsManipulationBuilder.UnitsSystem.NotSet)
    resultsCombinationBuilder1.SetIncompatibleResultsOption(NXOpen.CAE.ResultsCombinationBuilder.IncompatibleResults.Skip)
    resultsCombinationBuilder1.SetNoDataOption(NXOpen.CAE.ResultsCombinationBuilder.NoData.Skip)
    resultsCombinationBuilder1.SetEvaluationErrorOption(NXOpen.CAE.ResultsCombinationBuilder.EvaluationError.Skip)

    # get the full result names for user feedback. Do this before the try except block, otherwise the variable is no longer available
    fullResultNames: List[str] = GetFullResultNames(postInputs, solutionResults)
    try:
        resultsCombinationBuilder1.Commit()
        theLW.WriteFullline("Combine result:")
        theLW.WriteFullline("Formula: " + formula)
        theLW.WriteFullline("Used the following results:")

        for i in range(len(postInputs)):
            theLW.WriteFullline(postInputs[i].Identifier + ": " + fullResultNames[i])
        
        theLW.WriteFullline("Formula with results:")
        for i in range(len(postInputs)):
            formula = formula.Replace(postInputs[i].Identifier, fullResultNames[i])
        theLW.WriteFullline(formula)
                
    except Exception as e:
        theLW.WriteFullline("Error in CombineResults:")
        theLW.WriteFullline(e)
        raise

    finally:
        resultsCombinationBuilder1.Destroy()

        expressions: List[NXOpen.Expression] = simPart.Expressions
        for i in range(len(identifiers)):
            check: NXOpen.Expression = [item for item in expressions if item.Name.lower() == identifiers[i].lower()]
            if len(check) != 0:
                # expression found, thus deleting
                simPart.Expressions.Delete(check[0])


def GetResultUnits(baseResultTypes: List[NXOpen.CAE.BaseResultType]) -> List[NXOpen.Unit]:
    """Obtain the unit for each BaseResultType provided."""
    resultUnits: List[NXOpen.Unit] = [NXOpen.Unit] * len(baseResultTypes)
    for i in range(len(baseResultTypes)):
        components: List[NXOpen.CAE.ResultComponent] = baseResultTypes[i].AskComponents()
        resultUnits[i] = baseResultTypes[i].AskDefaultUnitForComponent(components[0])

    return resultUnits


def ExportResult(postInput: PostInput, unvFileName: str, sIUnits: bool = False) -> None:
    """Export a single result to universal file."""
    if not isinstance(basePart, NXOpen.CAE.SimPart):
        theLW.WriteFullline("ExportResult needs to start from a .sim file. Exiting")
        return
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart)

    postInputList: List[PostInput] = [postInput]
    # check input and catch errors so that the user doesn't get a error pop-up in SC
    try:
        CheckPostInput(postInputList)
    
    except ValueError as e:
        # internal raised exceptions are raised as valueError
        theLW.WriteFullline("Did not execute ExportResult due to input error. Please check the previous messages.")
        # we still return the tehcnical message as an additional log
        theLW.WriteFullline(e)
        return
    except:
        theLW.WriteFullline("Did not execute ExportResult due to general error. Please check the previous messages.")
        # we still return the tehcnical message as an additional log
        theLW.WriteFullline(e)
        return
    
    # Make sure the file is complete with path and extension
    unvFullName: str = CreateFullPath(unvFileName)

    # Load the results and store them in a list
    solutionResults: List[NXOpen.CAE.SolutionResult] = LoadResults(postInputList)

    # get all ResultType objects as defined in postInputs and store them in a list
    resultTypes: List[NXOpen.CAE.BaseResultType] = GetResultTypes(postInputList, solutionResults)
    
    # get all identifiers in postInputs and store them in a list, using list comprehension
    identifiers: List[str] = ["nxopenexportresult"]

    # get the full result names for user feedback. Do this before the try except block, otherwise the variable is no longer available
    fullResultNames: List[str] = GetFullResultNames(postInputList, solutionResults)

    # get the unit for each resultType from the result itself
    resultUnits: List[NXOpen.Unit]  = GetResultUnits(resultTypes)

    resultsCombinationBuilder = theSession.ResultManager.CreateResultsCombinationBuilder()
    resultsCombinationBuilder.SetResultTypes(resultTypes, identifiers, resultUnits)
    resultsCombinationBuilder.SetFormula("nxopenexportresult")
    resultsCombinationBuilder.SetOutputResultType(NXOpen.CAE.ResultsManipulationBuilder.OutputResultType.Full)
    resultsCombinationBuilder.SetIncludeModel(False)
    resultsCombinationBuilder.SetOutputQuantity(resultTypes[0].Quantity)
    resultsCombinationBuilder.SetOutputName(fullResultNames[0])
    resultsCombinationBuilder.SetLoadcaseName(fullResultNames[0])
    resultsCombinationBuilder.SetOutputFile(unvFullName)
    resultsCombinationBuilder.SetIncompatibleResultsOption(NXOpen.CAE.ResultsCombinationBuilder.IncompatibleResults.Skip)
    resultsCombinationBuilder.SetNoDataOption(NXOpen.CAE.ResultsCombinationBuilder.NoData.Skip)
    resultsCombinationBuilder.SetEvaluationErrorOption(NXOpen.CAE.ResultsCombinationBuilder.EvaluationError.Skip)

    # The following 2 lines have no effect if SetIncludeModel is set to false
    # If SetIncludeModel is true these 2 lines adds dataset 164 to the .unv file
    # resultsCombinationBuilder.SetUnitsSystem(NXOpen.CAE.ResultsManipulationBuilder.UnitsSystem.FromResult)
    # resultsCombinationBuilder.SetUnitsSystemResult(solutionResults[0])

    if sIUnits:
        # in case you want to set a userdefined units system
        userDefinedUnitSystem: NXOpen.CAE.Result.ResultBasicUnit = NXOpen.CAE.Result.ResultBasicUnit()
        units: List[NXOpen.Unit] = simPart.UnitCollection
        # Prints a list of all available units
        for item in units:
            theLW.WriteFullline(item.TypeName)
        
        userDefinedUnitSystem.AngleUnit = [item for item in units if item.TypeName == "Radian"]
        userDefinedUnitSystem.LengthUnit = [item for item in units if item.TypeName == "Meter"]
        userDefinedUnitSystem.MassUnit = [item for item in units if item.TypeName == "Kilogram"]
        userDefinedUnitSystem.TemperatureUnit = [item for item in units if item.TypeName == "Celcius"]
        userDefinedUnitSystem.ThermalenergyUnit = [item for item in units if item.TypeName == "ThermalEnergy_Metric1"]
        userDefinedUnitSystem.TimeUnit = [item for item in units if item.TypeName == "Second"]
        resultsCombinationBuilder.SetUnitsSystem(NXOpen.CAE.ResultsManipulationBuilder.UnitsSystem.UserDefined)
        resultsCombinationBuilder.SetUserDefinedUnitsSystem(userDefinedUnitSystem)
        # if set to false, dataset 164 is not added and the results are ambiguos for external use
        resultsCombinationBuilder.SetIncludeModel(True)

    try:
        resultsCombinationBuilder.Commit()
        theLW.WriteFullline("Exported result:")
        theLW.WriteFullline(fullResultNames[0])
                
    except Exception as e:
        theLW.WriteFullline("Error in ExportResult:")
        theLW.WriteFullline(e)
        raise

    finally:
        resultsCombinationBuilder.Destroy()

        expressions: List[NXOpen.Expression] = simPart.Expressions
        for i in range(len(identifiers)):
            check: NXOpen.Expression = [item for item in expressions if item.Name.lower() == identifiers[i].lower()]
            if len(check) != 0:
                # expression found, thus deleting
                simPart.Expressions.Delete(check[0])


def main() :
    theLW.Open()
    theLW.WriteFullline("Starting Main() in " + theSession.ExecutingJournal)
    
    combine1: PostInput = PostInput("Transverse", 1, 1, "[Stress][Element-Nodal]", "Stress1")
    combine2: PostInput = PostInput("Longitudinal", 1, 1, "[Stress][Element-Nodal]", "Stress1")

    postInputs: List[PostInput] = [combine1, combine2]
    CombineResults(postInputs)

    export: PostInput = PostInput("Longitudinal", 1, 1, "Displacement - Nodal")
    ExportResult(export, "exportedResult")
    ExportResult(export, "exportedResultSI", True) # exports in SI units

if __name__ == '__main__':
    main()
