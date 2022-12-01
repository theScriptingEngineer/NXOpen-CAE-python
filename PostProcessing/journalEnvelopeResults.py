# Simcenter 3D 2023
# Journal created by Frederik on Thu Aug 25 08:09:57 2022 W. Europe Daylight Time
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
    # ----------------------------------------------
    #   Menu: Tools->Results->Envelope...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    resultsManipulationEnvelopeBuilder1 = theSession.ResultManager.CreateResultsManipulationEnvelopeBuilder()
    
    caePart1 = workSimPart
    selectElementsBuilder1 = caePart1.SelectElementMgr.CreateSelectElementsBuilder()
    
    resultsManipulationEnvelopeBuilder1.OutputFileSettings.OutputName = "Default Result OutputName"
    
    resultsManipulationEnvelopeBuilder1.ApproachOption = NXOpen.CAE.ResultsManipulationEnvelopeBuilder.Approach.ThroughLoadCasesandResults
    
    resultsManipulationEnvelopeBuilder1.OutputFileSettings.LoadCaseName = "Envelope Max Through 2 load cases"
    
    resultsManipulationEnvelopeBuilder1.OutputFileSettings.CompanionName = "Companion"
    
    resultsManipulationEnvelopeBuilder1.OutputFileSettings.NeedLoadImmediately = True
    
    resultsManipulationEnvelopeBuilder1.OutputFieldSettings.IndependentDomainForElementNodalResult = NXOpen.CAE.ResultsManipOutputFieldSettings.IndepDomainDefinitionOptions.ElementNodeID
    
    theSession.SetUndoMarkName(markId1, "Results Envelope Dialog")
    
    resultsManipulationEnvelopeBuilder1.OutputFileSettings.LoadCaseName = "Envelope Max Through 0 load cases"
    
    resultsManipulationEnvelopeBuilder1.OutputFileSettings.LoadCaseName = "Envelope Max Through 1 load cases"
    
    resultsManipulationEnvelopeBuilder1.OutputFileSettings.LoadCaseName = "Envelope Max Through 2 load cases"
    
    resultsManipulationEnvelopeBuilder1.OutputFileSettings.CompanionName = "CompanionIdentifier"
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Results Envelope")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Results Envelope")
    
    resultParameters1 = theSession.ResultManager.CreateResultParameters()
    
    resultParameters1.SetDBScaling(0)
    
    signalProcessingDBSettings1 = resultParameters1.GetDbSettings()
    
    resultManager1 = theSession.ResultManager
    solutionResult1 = resultManager1.FindObject("SolutionResult[hullModelNX12_fem1_sim1.sim_Transverse]")
    loadcase1 = solutionResult1.Find("Loadcase[1]")
    iteration1 = loadcase1.Find("Iteration[1]")
    resultType1 = iteration1.Find("ResultType[[Stress][Element-Nodal]]")
    resultParameters1.SetGenericResultType(resultType1)
    
    resultParameters1.SetBeamSection(NXOpen.CAE.Result.BeamSection.ValueOf(-1))
    
    resultParameters1.SetShellSection(NXOpen.CAE.Result.ShellSection.TrueMaximum)
    
    resultParameters1.SetResultComponent(NXOpen.CAE.Result.Component.VonMises)
    
    resultParameters1.SetCoordinateSystem(NXOpen.CAE.Result.CoordinateSystem.AbsoluteRectangular)
    
    resultParameters1.SetSelectedCoordinateSystem(NXOpen.CAE.Result.CoordinateSystemSource.NotSet, -1)
    
    resultParameters1.SetRotationAxisOfAbsoluteCyndricalCSYS(NXOpen.CAE.Post.AxisymetricAxis.NotSet)
    
    resultParameters1.SetBeamResultsInLocalCoordinateSystem(True)
    
    resultParameters1.SetShellResultsInProjectedCoordinateSystem(False)
    
    resultParameters1.MakeElementResult(False)
    
    resultParameters1.SetElementValueCriterion(NXOpen.CAE.Result.ElementValueCriterion.Average)
    
    resultParameters1.SetSpectrumScaling(NXOpen.CAE.SignalProcessingPlotData.ScalingType.Unknown)
    
    resultParameters1.SetAcousticWeighting(NXOpen.CAE.SignalProcessingPlotData.AcousticalWeighting.NotSet)
    
    average1 = NXOpen.CAE.Result.Averaging()
    
    average1.DoAveraging = False
    average1.AverageAcrossPropertyIds = True
    average1.AverageAcrossMaterialIds = True
    average1.AverageAcrossElementTypes = False
    average1.AverageAcrossFeatangle = True
    average1.AverageAcrossAnglevalue = 45.0
    average1.IncludeInternalElementContributions = True
    resultParameters1.SetAveragingCriteria(average1)
    
    resultParameters1.SetComputationType(NXOpen.CAE.Result.ComputationType.NotSet)
    
    resultParameters1.SetComputeOnVisible(False)
    
    resultParameters1.SetComplexCriterion(NXOpen.CAE.Result.Complex.Real)
    
    resultParameters1.SetPhaseAngle(0.0)
    
    resultParameters1.SetSectionPlyLayer(0, 0, 1)
    
    resultParameters1.SetPlyID(0)
    
    resultParameters1.SetPlyLocation(NXOpen.CAE.Result.PlyLocation.Middle)
    
    resultParameters1.SetScale(1.0)
    
    unit1 = workSimPart.UnitCollection.FindObject("StressNewtonPerSquareMilliMeter")
    resultParameters1.SetUnit(unit1)
    
    resultParameters1.SetAbsoluteValue(False)
    
    resultParameters1.SetTensorComponentAbsoluteValue(NXOpen.CAE.Result.TensorDerivedAbsolute.DerivedComponent)
    
    resultParameters1.SetCalculateBeamStrResults(False)
    
    resultParameters1.SetBeamFillets(False)
    
    resultParameters1.SetBeamFilletRadius(0.0)
    
    resultParameters1.SetIncludeMidNode(True)
    
    resultParameters1.SetIsReferenceNode(False)
    
    resultParameters1.SetReferenceNode(None)
    
    cycparams1 = resultParameters1.GetCyclicSymmParameters()
    
    cycparams1[0].ResultOption = NXOpen.CAE.CyclicSymmetricParameters.GetResult.OnOriginalModel
    
    cycparams1[0].OriginalResultOption = NXOpen.CAE.CyclicSymmetricParameters.OriginalResult.BySector
    
    cycparams1[0].SectCriteria = NXOpen.CAE.CyclicSymmetricParameters.SectorCriteria.Index
    
    cycparams1[0].SectorValue = NXOpen.CAE.CyclicSymmetricParameters.Value.Maximum
    
    cycparams1[0].EnvValue = NXOpen.CAE.CyclicSymmetricParameters.EnvelopeValue.Average
    
    cycparams1[0].SectorIndex = 1
    
    sectors1 = []
    cycparams1[0].SetSectorIndices(sectors1)
    
    cycparams2 = [NXOpen.CAE.CyclicSymmetricParameters.Null] * 1 
    cycparams2[0] = cycparams1[0]
    resultParameters1.SetCyclicSymmParameters(cycparams2)
    
    axiSymmetricParameters1 = resultParameters1.GetAxiSymmetricParameters()
    
    axiSymmetricParameters1.ResultOption = NXOpen.CAE.AxiSymmetricParameters.GetResult.OnOriginalModel
    
    axiSymmetricParameters1.RotationAxis = NXOpen.CAE.AxiSymmetricParameters.AxisOfRotation.ValueOf(-1)
    
    axiSymmetricParameters1.AxiOptions = NXOpen.CAE.AxiSymmetricParameters.Options.AtRevolveAngle
    
    axiSymmetricParameters1.EnvelopeVal = NXOpen.CAE.AxiSymmetricParameters.EnvVal.Average
    
    axiSymmetricParameters1.RevolveAngle = 0.0
    
    axiSymmetricParameters1.StartRevolveAngle = 0.0
    
    axiSymmetricParameters1.EndRevolveAngle = 360.0
    
    axiSymmetricParameters1.NumberOfSections = 40
    
    resultParameters1.SetProjectOnNodeNormal(False)
    
    resultParameters2 = theSession.ResultManager.CreateResultParameters()
    
    resultParameters2.SetDBScaling(0)
    
    signalProcessingDBSettings2 = resultParameters2.GetDbSettings()
    
    solutionResult2 = resultManager1.FindObject("SolutionResult[hullModelNX12_fem1_sim1.sim_Longitudinal]")
    loadcase2 = solutionResult2.Find("Loadcase[1]")
    iteration2 = loadcase2.Find("Iteration[1]")
    resultType2 = iteration2.Find("ResultType[[Stress][Element-Nodal]]")
    resultParameters2.SetGenericResultType(resultType2)
    
    resultParameters2.SetBeamSection(NXOpen.CAE.Result.BeamSection.ValueOf(-1))
    
    resultParameters2.SetShellSection(NXOpen.CAE.Result.ShellSection.TrueMaximum)
    
    resultParameters2.SetResultComponent(NXOpen.CAE.Result.Component.VonMises)
    
    resultParameters2.SetCoordinateSystem(NXOpen.CAE.Result.CoordinateSystem.AbsoluteRectangular)
    
    resultParameters2.SetSelectedCoordinateSystem(NXOpen.CAE.Result.CoordinateSystemSource.NotSet, -1)
    
    resultParameters2.SetRotationAxisOfAbsoluteCyndricalCSYS(NXOpen.CAE.Post.AxisymetricAxis.NotSet)
    
    resultParameters2.SetBeamResultsInLocalCoordinateSystem(True)
    
    resultParameters2.SetShellResultsInProjectedCoordinateSystem(False)
    
    resultParameters2.MakeElementResult(False)
    
    resultParameters2.SetElementValueCriterion(NXOpen.CAE.Result.ElementValueCriterion.Average)
    
    resultParameters2.SetSpectrumScaling(NXOpen.CAE.SignalProcessingPlotData.ScalingType.Unknown)
    
    resultParameters2.SetAcousticWeighting(NXOpen.CAE.SignalProcessingPlotData.AcousticalWeighting.NotSet)
    
    average2 = NXOpen.CAE.Result.Averaging()
    
    average2.DoAveraging = False
    average2.AverageAcrossPropertyIds = True
    average2.AverageAcrossMaterialIds = True
    average2.AverageAcrossElementTypes = False
    average2.AverageAcrossFeatangle = True
    average2.AverageAcrossAnglevalue = 45.0
    average2.IncludeInternalElementContributions = True
    resultParameters2.SetAveragingCriteria(average2)
    
    resultParameters2.SetComputationType(NXOpen.CAE.Result.ComputationType.NotSet)
    
    resultParameters2.SetComputeOnVisible(False)
    
    resultParameters2.SetComplexCriterion(NXOpen.CAE.Result.Complex.Real)
    
    resultParameters2.SetPhaseAngle(0.0)
    
    resultParameters2.SetSectionPlyLayer(0, 0, 1)
    
    resultParameters2.SetPlyID(0)
    
    resultParameters2.SetPlyLocation(NXOpen.CAE.Result.PlyLocation.Middle)
    
    resultParameters2.SetScale(1.0)
    
    resultParameters2.SetUnit(unit1)
    
    resultParameters2.SetAbsoluteValue(False)
    
    resultParameters2.SetTensorComponentAbsoluteValue(NXOpen.CAE.Result.TensorDerivedAbsolute.DerivedComponent)
    
    resultParameters2.SetCalculateBeamStrResults(False)
    
    resultParameters2.SetBeamFillets(False)
    
    resultParameters2.SetBeamFilletRadius(0.0)
    
    resultParameters2.SetIncludeMidNode(True)
    
    resultParameters2.SetIsReferenceNode(False)
    
    resultParameters2.SetReferenceNode(None)
    
    cycparams3 = resultParameters2.GetCyclicSymmParameters()
    
    cycparams3[0].ResultOption = NXOpen.CAE.CyclicSymmetricParameters.GetResult.OnOriginalModel
    
    cycparams3[0].OriginalResultOption = NXOpen.CAE.CyclicSymmetricParameters.OriginalResult.BySector
    
    cycparams3[0].SectCriteria = NXOpen.CAE.CyclicSymmetricParameters.SectorCriteria.Index
    
    cycparams3[0].SectorValue = NXOpen.CAE.CyclicSymmetricParameters.Value.Maximum
    
    cycparams3[0].EnvValue = NXOpen.CAE.CyclicSymmetricParameters.EnvelopeValue.Average
    
    cycparams3[0].SectorIndex = 1
    
    sectors2 = []
    cycparams3[0].SetSectorIndices(sectors2)
    
    cycparams4 = [NXOpen.CAE.CyclicSymmetricParameters.Null] * 1 
    cycparams4[0] = cycparams3[0]
    resultParameters2.SetCyclicSymmParameters(cycparams4)
    
    axiSymmetricParameters2 = resultParameters2.GetAxiSymmetricParameters()
    
    axiSymmetricParameters2.ResultOption = NXOpen.CAE.AxiSymmetricParameters.GetResult.OnOriginalModel
    
    axiSymmetricParameters2.RotationAxis = NXOpen.CAE.AxiSymmetricParameters.AxisOfRotation.ValueOf(-1)
    
    axiSymmetricParameters2.AxiOptions = NXOpen.CAE.AxiSymmetricParameters.Options.AtRevolveAngle
    
    axiSymmetricParameters2.EnvelopeVal = NXOpen.CAE.AxiSymmetricParameters.EnvVal.Average
    
    axiSymmetricParameters2.RevolveAngle = 0.0
    
    axiSymmetricParameters2.StartRevolveAngle = 0.0
    
    axiSymmetricParameters2.EndRevolveAngle = 360.0
    
    axiSymmetricParameters2.NumberOfSections = 40
    
    resultParameters2.SetProjectOnNodeNormal(False)
    
    results1 = [NXOpen.CAE.Result.Null] * 2 
    results1[0] = solutionResult1
    results1[1] = solutionResult2
    parameters1 = [NXOpen.CAE.ResultParameters.Null] * 2 
    parameters1[0] = resultParameters1
    parameters1[1] = resultParameters2
    resultsManipulationEnvelopeBuilder1.InputSettings.SetResultsAndParameters(results1, parameters1)
    
    resultsManipulationEnvelopeBuilder1.UnitSystem.UnitsSystemType = NXOpen.CAE.ResultsManipulationUnitsSystem.Type.FromResult
    
    resultsManipulationEnvelopeBuilder1.UnitSystem.Result = solutionResult2
    
    resultsManipulationEnvelopeBuilder1.OutputFileSettings.OutputFile = "C:\\Users\\Frederik\\Documents\\SC2022\\Python\\CompanionIdentifier.unv"
    
    simSimulation1 = workSimPart.FindObject("Simulation")
    simSolution1 = simSimulation1.FindObject("Solution[Transverse]")
    simResultReference1 = simSolution1.Find("Structural")
    resultsManipulationEnvelopeBuilder1.OutputFileSettings.CompanionResultReference = simResultReference1
    
    nXObject1 = resultsManipulationEnvelopeBuilder1.Commit()
    
    resultsManipulationEnvelopeBuilder1.UnitSystem.UnitsSystemType = NXOpen.CAE.ResultsManipulationUnitsSystem.Type.FromResult
    
    resultsManipulationEnvelopeBuilder1.UnitSystem.Result = solutionResult2
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.SetUndoMarkName(markId1, "Results Envelope")
    
    resultsManipulationEnvelopeBuilder1.Destroy()
    
    selectElementsBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()