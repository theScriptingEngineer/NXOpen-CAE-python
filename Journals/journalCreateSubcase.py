# Simcenter 3D 2023
# Journal created by Frederik on Thu Aug 25 08:05:26 2022 W. Europe Daylight Time
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
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution Step")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    simSimulation1 = workSimPart.FindObject("Simulation")
    simSolution1 = simSimulation1.FindObject("Solution[Solution 1]")
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs1 = theSession.UpdateManager.DoUpdate(id1)
    
    simSolutionStep1 = simSolution1.CreateStep(0, True, "Subcase - Statics 2")
    
    propertyTable1 = simSolutionStep1.PropertyTable
    
    theSession.SetUndoMarkName(markId2, "Solution Step Dialog")
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution Step")
    
    theSession.DeleteUndoMark(markId3, None)
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution Step")
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    simSolutionStep1.SetName("mySecondSubcase")
    
    propertyTable2 = simSolutionStep1.PropertyTable
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId5)
    
    theSession.DeleteUndoMark(markId5, None)
    
    theSession.DeleteUndoMark(markId4, None)
    
    theSession.SetUndoMarkName(markId2, "Solution Step")
    
    theSession.DeleteUndoMark(markId2, None)
    
    theSession.SetUndoMarkVisibility(markId1, None, NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()