 # intellisense by theScriptingEngineer
 # untested

 # The code for EnvelopeResults has been depricated in NX version 1980, release 2021.2

import math
import sys
import os
import NXOpen
import NXOpen.CAE
import NXOpen.Fields
from typing import List, cast, Tuple

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
    
    def __init__(self, solution: str, subcase: int, iteration: int, resultType: str, identifier: str = ""):
        """Constructor"""
        self.Solution = solution
        self.Subcase = subcase
        self.Iteration = iteration
        self.ResultType = resultType
        self.Identifier = identifier

    def ToString(self) -> str:
        """String representation of a PostInput"""
        return "Solution: " + self.Solution + " Subcase: " + str(self.Subcase) + " Iteration: " + str(self.Iteration) + " ResultType: " + self.ResultType + " Identifier: " + self.Identifier


def GetSolution(solutionName: str) -> NXOpen.CAE.SimSolution:
    """This function returns the SimSolution object with the given name.

    Parameters
    ----------
    solutionName: str
        The name of the solution to return. Case insensitive.

    Returns
    -------
    NXOpen.CAE.SimSolution
        Returns a list of SolutionResult.
    """
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart) # explicit casting makes it clear
    simSimulation: NXOpen.CAE.SimSimulation = simPart.Simulation

    simSolution: List[NXOpen.CAE.SimSolution] = [item for item in simSimulation.Solutions if item.Name.lower() == solutionName.lower()]
    if len(simSolution) == 0:
        return None
    
    return simSolution[0]

def LoadResults(postInputs: List[PostInput], referenceType: str = "Structural") -> NXOpen.CAE.SolutionResult:
    """Loads the results for the given list of PostInput and returns a list of SolutionResult.
    An exception is raised if the result does not exist (-> to check if CreateReferenceResult raises error or returns None)

    Parameters
    ----------
    postInputs: List[PostInput]
        The result of each of the provided solutions is loaded.
    referenceType: str
        The type of SimResultReference eg. Structural. Defaults to structral

    Returns
    -------
    NXOpen.CAE.SolutionResult
        Returns a list of SolutionResult.
    """
    solutionResults: List[NXOpen.CAE.SolutionResult] = [NXOpen.CAE.SolutionResult] * len(postInputs)
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart)

    for i in range(len(postInputs)):
        simSolution: NXOpen.CAE.SimSolution = GetSolution(postInputs[i].Solution)
        simResultReference: NXOpen.CAE.SimResultReference = cast(NXOpen.CAE.SimResultReference, simSolution.Find(referenceType))

        try:
            # SolutionResult[filename_solutionname]
            solutionResults[i] = cast(NXOpen.CAE.SolutionResult, theSession.ResultManager.FindObject("SolutionResult[" + sys.Path.GetFileName(simPart.FullPath) + "_" + simSolution.Name + "]"))
        except:
            solutionResults[i] = theSession.ResultManager.CreateReferenceResult(simResultReference)

    return solutionResults


def GetResultUnits(baseResultTypes: List[NXOpen.CAE.BaseResultType]) -> List[NXOpen.Unit]:
    """Delete companion result with given name from the given solution.

    Parameters
    ----------
    solutionName: str
        The name of the solution the compnanionresult belongs to
    companionResultName: str
        The name of the compnanionresult to delete.
    referenceType: str
        The type of SimResultReference eg. Structural. Defaults to structral
    """

    resultUnits: List[NXOpen.Unit] = [NXOpen.Unit] * len(baseResultTypes)
    for i in range(len(baseResultTypes)):
        components: List[NXOpen.CAE.Result.Component] = baseResultTypes[i].AskComponents()
        resultUnits[i] = baseResultTypes[i].AskDefaultUnitForComponent(components[0])

    return resultUnits


def GetResultTypes(postInputs: List[PostInput], solutionResults: List[NXOpen.CAE.SolutionResult]) -> List[NXOpen.CAE.BaseResultType]:
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
    """Delete companion result with given name from the given solution.

    Parameters
    ----------
    solutionName: str
        The name of the solution the compnanionresult belongs to
    companionResultName: str
        The name of the compnanionresult to delete.
    referenceType: str
        The type of SimResultReference eg. Structural. Defaults to structral
    """
    simSolution: NXOpen.CAE.SimSolution = GetSolution(solutionName)
    simResultReference: NXOpen.CAE.SimResultReference = cast(NXOpen.CAE.SimResultReference, simSolution.Find(referenceType))
    companionResult: List[NXOpen.CAE.CompanionResult] = [item for item in simResultReference.CompanionResults if item.Name.lower() == companionResultName.lower()]
    if len(companionResult) != 0:
        # companion result exists, delete it
        simResultReference.CompanionResults.Delete(companionResult[0])


def GetSimResultReference(solutionName: str, referenceType: str = "Structural") -> NXOpen.CAE.SimResultReference:
    """Helper function for CombineResults and EnvelopeResults.
    Returns the SimResultReferece for the given solution

    Parameters
    ----------
    solutionName: str
        The solution for which to get the "structural" SimResultReference.
    referenceType: str
        The type of SimResultReference eg. Structural. Defaults to structral

    Returns
    -------
    NXOpen.CAE.SimResultReference
        Returns the "Structural" simresultreference.
    """
    simSolution: NXOpen.CAE.SimSolution = GetSolution(solutionName)
    if simSolution == None:
        # solution with given name not found
        theLW.WriteFullline("GetSimResultReference: Solution with name " + solutionName + " not found.")
        return None
    simResultReference: NXOpen.CAE.SimResultReference = cast(NXOpen.CAE.SimResultReference, simSolution.Find(referenceType))
    return simResultReference

def CreateFullPath(fileName: str) -> str:
    """This function takes a filename and adds the .unv extension and path of the part if not provided by the user.
    If the fileName contains an extension, this function leaves it untouched, othwerwise adds .unv as extension.
    If the fileName contains a path, this function leaves it untouched, otherwise adds the path of the BasePart as the path.
    Undefined behaviour if basePart has not yet been saved (eg FullPath not available)

    Parameters
    ----------
    fileName: str
        The filename with or without path and .unv extension.
    solutionResults: List[NXOpen.CAE.SolutionResult]
        The solution results from which the representation is obtained.

    Returns
    -------
    str
        A string with .unv extension and path of the basePart if the fileName parameter did not include a path.
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

    Parameters
    ----------
    postInputs: List[PostInput]
        The array of PostInput to check.
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
    """This function verifies the identifiers in all PostInputs:
        Null or empty string.
        Reserved expression name.
        Use of an expression which already exists.

    Parameters
    ----------
    postInputs: List[PostInput]
        The array of PostInput to check.
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


def CheckUnvFileName(unvFileName: str) -> None:
    """This method loops through all solutions and all companion results in these solutions.
    It checks if the file name is not already in use by another companion result.
    And throws an error if so.

    Parameters
    ----------
    unvFileName: str
        The file name to look for.
    """

    # Don't perform checks on the file itself in the file system!
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart)
    # loop through all solutions
    solutions: List[NXOpen.CAE.SimSolution] = simPart.Simulation.Solutions.ToArray()
    for i in range(len(solutions)):
        simResultReference: NXOpen.CAE.SimResultReference = GetSimResultReference(solutions[i].Name)
        # loop through each companion result
        companionResults: List[NXOpen.CAE.CompanionResult] = simResultReference.CompanionResults.ToArray()
        for j in range(len(companionResults)):
            # create the builder with the companion result, so can access the CompanionResultsFile
            companionResultBuilder: NXOpen.CAE.CompanionResultBuilder = simResultReference.CompanionResults.CreateCompanionResultBuilder(companionResults[j])
            if (companionResultBuilder.CompanionResultsFile.lower() == unvFileName.lower()):
                # the file is the same, so throw exception
                raise ValueError("Companion results file name " + unvFileName + " is already used by companion result " + companionResults[j].Name)


def GetFullResultNames(postInputs: List[PostInput], solutionResults: List[NXOpen.CAE.SolutionResult]) -> List[str]:
    """This function returns a representation of the Results used in PostInputs.
    Note that the representation is taken from the SolutionResult and not the SimSolution!

    Parameters
    ----------
    postInputs: List[PostInput]
        The list of PostInput defining the results.
    solutionResults: List[NXOpen.CAE.SolutionResult]
        The solution results from which the representation is obtained.

    Returns
    -------
    List[str]
        List of string with each representation.
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
            formula = formula.replace(postInputs[i].Identifier, fullResultNames[i])
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


def GetResultParamaters(resultTypes: List[NXOpen.CAE.BaseResultType], resultSection: NXOpen.CAE.Result.Section, resultComponent: NXOpen.CAE.Result.Component, absolute: bool) -> List[NXOpen.CAE.ResultParameters]:
    resultParameterList: List[NXOpen.CAE.ResultParameters] = [NXOpen.CAE.ResultParameters] * len(resultTypes)

    for i in range(len(resultParameterList)):
        resultParameters: NXOpen.CAE.ResultParameters = theSession.ResultManager.CreateResultParameters()
        resultParameters.SetGenericResultType(resultTypes[i])
        resultParameters.SetResultShellSection(resultSection)
        resultParameters.SetResultComponent(resultComponent)
        resultParameters.SetSelectedCoordinateSystem(NXOpen.CAE.Result.CoordinateSystem.None, -1)
        resultParameters.MakeElementResult(False)

        # components: List[NXOpen.CAE.Result.Component] = resultTypes[i].AskComponents()
        result: Tuple[List[NXOpen.CAE.Result.Component], List[str]] = resultTypes[i].AskComponents()
        unit: NXOpen.Unit = resultTypes[i].AskDefaultUnitForComponent(result[0][0]) # [0] for the list of componentns and another [0] for the first componentn
        resultParameters.SetUnit(unit)

        resultParameters.SetAbsoluteValue(absolute)
        resultParameters.SetTensorComponentAbsoluteValue(NXOpen.CAE.Result.TensorDerivedAbsolute.DerivedComponent)

        resultParameterList[i] = resultParameters
    
    return resultParameterList


def EnvelopeResults(postInputs: List[PostInput], companionResultName: str, unvFileName: str, envelopeOperation: NXOpen.CAE.ResultsEnvelopeBuilder.Operation, resultSection: NXOpen.CAE.Result.Section, resultComponent: NXOpen.CAE.Result.Component, absolute: bool, solutionName: str = "") -> None:
    if not isinstance(basePart, NXOpen.CAE.SimPart):
        theLW.WriteFullline("ExportResult needs to start from a .sim file. Exiting")
        return
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart)

    # check input and catch errors so that the user doesn't get a error pop-up in SC
    try:
        CheckPostInput(postInputs)
    
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


    # Select the solution to add the companion result to
    simResultReference: NXOpen.CAE.SimResultReference 
    if (GetSolution(solutionName) != None):
        # delete the companion result if it exists so we can create a new one with the same name (eg overwrite)
        DeleteCompanionResult(solutionName, companionResultName)
        # get the SimResultReference to add the companion result to.
        simResultReference = GetSimResultReference(solutionName)
    else:
        if (solutionName != ""):
            theLW.WriteFullline("Solution with name " + solutionName + " not found. Adding companion result to solution " + postInputs[0].Solution)
        
        # delete the companion result if it exists so we can create a new one with the same name (eg overwrite)
        DeleteCompanionResult(postInputs[0].Solution, companionResultName)

        # get the SimResultReference to add the companion result to. Now hard coded as the solution of the first PostInput
        simResultReference = GetSimResultReference(postInputs[0].Solution)

    # Make sure the file is complete with path and extension
    unvFullName: str = CreateFullPath(unvFileName)

    # Check if unvFullName is not already in use by another companion result
    # No risk of checking the file for this companion result as DeleteCompanionResult has already been called.
    try:
        CheckUnvFileName(unvFullName)
    except ValueError as e:
        # ChechUnvFileName throws an error with the message containing the filename and the companion result.
        theLW.WriteFullline(e)
        return
    
    # Load all results
    solutionResults: List[NXOpen.CAE.SolutionResult] = LoadResults(postInputs)

    # Get the requested results
    resultTypes: List[NXOpen.CAE.BaseResultType] = GetResultTypes(postInputs, solutionResults)

    # create an array of resultParameters with the inputs and settings from the user.
    resultParameters: List[NXOpen.CAE.ResultParameters] = GetResultParamaters(resultTypes, resultSection, resultComponent, absolute)

    resultsEnvelopeBuilder: NXOpen.CAE.ResultsEnvelopeBuilder = theSession.ResultManager.CreateResultsEnvelopeBuilder()
    resultsEnvelopeBuilder.SetResults(solutionResults, resultParameters)
    resultsEnvelopeBuilder.SetOperation(envelopeOperation)
    resultsEnvelopeBuilder.SetOutputResultType(NXOpen.CAE.ResultsManipulationBuilder.OutputResultType.Companion)
    resultsEnvelopeBuilder.SetIncludeModel(False)
    resultsEnvelopeBuilder.SetCompanionResultReference(simResultReference)
    resultsEnvelopeBuilder.SetCompanionResultName(companionResultName)
    resultsEnvelopeBuilder.SetAppendMethod(NXOpen.CAE.ResultsManipulationBuilder.ResultAppendMethod.CreateNewLoadCases)
    resultsEnvelopeBuilder.SetImportResult(True)
    resultsEnvelopeBuilder.SetOutputQuantity(resultTypes[0].Quantity)
    resultsEnvelopeBuilder.SetOutputName(str(envelopeOperation) + " " + str(resultTypes[0].Quantity) + " (" + str(resultComponent) + ")") # ("Maximum Stress(Von-Mises)")
    resultsEnvelopeBuilder.SetLoadcaseName(companionResultName)
    resultsEnvelopeBuilder.SetOutputFile(unvFullName)
    resultsEnvelopeBuilder.SetUnitsSystem(NXOpen.CAE.ResultsManipulationBuilder.UnitsSystem.FromResult)
    resultsEnvelopeBuilder.SetUnitsSystemResult(solutionResults[0])
    resultsEnvelopeBuilder.SetIncompatibleResultsOption(NXOpen.CAE.ResultsEnvelopeBuilder.IncompatibleResults.Skip)
    resultsEnvelopeBuilder.SetNoDataOption(NXOpen.CAE.ResultsEnvelopeBuilder.NoData.Skip)

    # get the full result names for user feedback. Do this before the try catch block, otherwise the variable is no longer available
    fullResultNames: List[str]  = GetFullResultNames(postInputs, solutionResults)

    try:
        resultsEnvelopeBuilder.Commit()

        # user feedback
        theLW.WriteFullline("Created an envelope for the following results for " + str(envelopeOperation) + " " + str(resultComponent))
        for i in range(len(postInputs)):
            theLW.WriteFullline(fullResultNames[i]);

        theLW.WriteFullline("Section location: " + str(resultSection))
        theLW.WriteFullline("Absolute: " + str(absolute))
    
    except ValueError as e:
        theLW.WriteFullline("Error in EnvelopeResults!")
        theLW.WriteFullline(e)
        raise e
    
    finally:
        resultsEnvelopeBuilder.Destroy()
        for i in range(len(resultParameters)):
            theSession.ResultManager.DeleteResultParameters(resultParameters[i])


def main() :
    theLW.Open()
    theLW.WriteFullline("Starting Main() in " + theSession.ExecutingJournal)
    
    combine1: PostInput = PostInput("Transverse", 1, 1, "Stress - Element-Nodal", "Stress1")
    combine2: PostInput = PostInput("Longitudinal", 1, 1, "Stress - Element-Nodal", "Stress2")

    postInputs: List[PostInput] = [combine1, combine2]
    CombineResults(postInputs, "Stress1 + Stress2", "sumLoadCase1", "sumLoadCase1")

    export: PostInput = PostInput("Longitudinal", 1, 1, "Displacement - Nodal")
    ExportResult(export, "exportedResult")
    ExportResult(export, "exportedResultSI", True) # exports in SI units

if __name__ == '__main__':
    main()
