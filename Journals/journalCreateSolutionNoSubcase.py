# Simcenter 3D 2023
# Journal created by Frederik on Thu Aug 25 08:05:57 2022 W. Europe Daylight Time
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
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    theSession.SetUndoMarkName(markId2, "Solution Dialog")
    
    theSession.SetUndoMarkVisibility(markId2, None, NXOpen.Session.MarkVisibility.Invisible)
    
    theSession.SetUndoMarkName(markId2, "Solution")
    
    theSession.SetUndoMarkVisibility(markId2, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    simPart1 = workSimPart
    simSimulation1 = simPart1.Simulation
    
    simSolution1 = simSimulation1.CreateSolution("NX NASTRAN", "Structural", "SESTATIC 101 - Single Constraint", "Solution 2", NXOpen.CAE.SimSimulation.AxisymAbstractionType.NotSet)
    
    propertyTable1 = simSolution1.PropertyTable
    
    theSession.SetUndoMarkName(markId3, "Solution Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Solution
    # ----------------------------------------------
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution")
    
    theSession.DeleteUndoMark(markId4, None)
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution")
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    propertyTable2 = simSolution1.PropertyTable
    
    modelingObjectPropertyTable1 = workSimPart.ModelingObjectPropertyTables.FindObject("SsmoPropTable[Bulk Data Echo Request1]")
    propertyTable2.SetNamedPropertyTablePropertyValue("Bulk Data Echo Request", modelingObjectPropertyTable1)
    
    modelingObjectPropertyTable2 = workSimPart.ModelingObjectPropertyTables.FindObject("SsmoPropTable[Structural Output Requests1]")
    propertyTable2.SetNamedPropertyTablePropertyValue("Output Requests", modelingObjectPropertyTable2)
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId6)
    
    theSession.DeleteUndoMark(markId6, None)
    
    theSession.DeleteUndoMark(markId5, None)
    
    theSession.SetUndoMarkName(markId3, "Solution")
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.DeleteUndoMark(markId2, None)
    
    theSession.SetUndoMarkVisibility(markId1, None, NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()