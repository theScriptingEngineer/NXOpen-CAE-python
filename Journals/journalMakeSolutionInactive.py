# Simcenter 3D 2023
# Journal created by Frederik on Thu Aug 25 08:03:57 2022 W. Europe Daylight Time
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
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Deactivate Solution")
    
    simSimulation1 = workSimPart.FindObject("Simulation")
    simSimulation1.ActiveSolution = NXOpen.CAE.SimSolution.Null
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()