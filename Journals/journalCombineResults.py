# Simcenter 3D 2023
# Journal created by Frederik on Thu Aug 25 08:07:38 2022 W. Europe Daylight Time
#
import math
import DSEDesignWorkflow
import DSEPlatform
import Join
import MoldCooling
import NXOpen
import NXOpen.CAE
import SafetyOpen
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay
    simSimulation1 = workSimPart.FindObject("Simulation")
    simSolution1 = simSimulation1.FindObject("Solution[Transverse]")
    simResultReference1 = simSolution1.Find("Structural")
    solutionResult1 = theSession.ResultManager.CreateReferenceResult(simResultReference1)
    
    simSolution2 = simSimulation1.FindObject("Solution[Longitudinal]")
    simResultReference2 = simSolution2.Find("Structural")
    solutionResult2 = theSession.ResultManager.CreateReferenceResult(simResultReference2)
    
    # ----------------------------------------------
    #   Menu: Tools->Results->Combination...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId1, "Results Combination Dialog")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Results Combination")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Results Combination")
    
    resultsCombinationBuilder1 = theSession.ResultManager.CreateResultsCombinationBuilder()
    
    types1 = [NXOpen.CAE.BaseResultType.Null] * 2 
    loadcase1 = solutionResult1.Find("Loadcase[1]")
    iteration1 = loadcase1.Find("Iteration[1]")
    resultType1 = iteration1.Find("ResultType[[Stress][Element-Nodal]]")
    types1[0] = resultType1
    loadcase2 = solutionResult2.Find("Loadcase[1]")
    iteration2 = loadcase2.Find("Iteration[1]")
    resultType2 = iteration2.Find("ResultType[[Stress][Element-Nodal]]")
    types1[1] = resultType2
    names1 = [None] * 2 
    names1[0] = "STRE"
    names1[1] = "STRE_1"
    units1 = [NXOpen.Unit.Null] * 2 
    unit1 = workSimPart.UnitCollection.FindObject("StressMilliNewtonPerSquareMilliMeter")
    units1[0] = unit1
    units1[1] = unit1
    resultsCombinationBuilder1.SetResultTypes(types1, names1, units1)
    
    resultsCombinationBuilder1.SetFormula("STRE + STRE_1")
    
    resultsCombinationBuilder1.SetOutputResultType(NXOpen.CAE.ResultsManipulationBuilder.OutputResultType.Companion)
    
    resultsCombinationBuilder1.SetIncludeModel(False)
    
    resultsCombinationBuilder1.SetCompanionResultReference(simResultReference1)
    
    resultsCombinationBuilder1.SetCompanionIdentifier("companionIdentifier")
    
    resultsCombinationBuilder1.SetAppendMethod(NXOpen.CAE.ResultsManipulationBuilder.ResultAppendMethod.CreateNewLoadCases)
    
    resultsCombinationBuilder1.SetImportResult(True)
    
    resultsCombinationBuilder1.SetOutputQuantity(NXOpen.CAE.Result.Quantity.Stress)
    
    resultsCombinationBuilder1.SetOutputName("outputName")
    
    resultsCombinationBuilder1.SetLoadcaseName("loadcaseName")
    
    resultsCombinationBuilder1.SetOutputFile("C:\\Users\\Frederik\\Documents\\SC2022\\Python\\pythonCombine.unv")
    
    resultsCombinationBuilder1.SetUnitsSystem(NXOpen.CAE.ResultsManipulationBuilder.UnitsSystem.FromResult)
    
    resultsCombinationBuilder1.SetUnitsSystemResult(solutionResult1)
    
    resultsCombinationBuilder1.SetIncompatibleResultsOption(NXOpen.CAE.ResultsCombinationBuilder.IncompatibleResults.Skip)
    
    resultsCombinationBuilder1.SetNoDataOption(NXOpen.CAE.ResultsCombinationBuilder.NoData.Skip)
    
    resultsCombinationBuilder1.SetEvaluationErrorOption(NXOpen.CAE.ResultsCombinationBuilder.EvaluationError.Skip)
    
    nXObject1 = resultsCombinationBuilder1.Commit()
    
    resultsCombinationBuilder1.Destroy()
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.SetUndoMarkName(markId1, "Results Combination")
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()