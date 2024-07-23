# Simcenter 3D 2306
# Journal created by HP on Tue Jul 23 09:09:53 2024 W. Europe Daylight Time
#
import math
import NXOpen
import NXOpen.CAE
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay
    results1 = [NXOpen.CAE.Result.Null] * 1 
    resultManager1 = theSession.ResultManager
    solutionResult1 = resultManager1.FindObject("SolutionResult[Full_crane_assyfem_sim.sim_Position0][Structural]")
    results1[0] = solutionResult1
    usergroupIds1 = [None] * 1 
    usergroupIds1[0] = 1
    theSession.Post.PostviewApplyUserGroupVisibility(2, results1, usergroupIds1, NXOpen.CAE.Post.GroupVisibility.ShowOnly)
    
    results2 = [NXOpen.CAE.Result.Null] * 1 
    results2[0] = solutionResult1
    usergroupIds2 = [None] * 1 
    usergroupIds2[0] = 107
    theSession.Post.PostviewApplyUserGroupVisibility(2, results2, usergroupIds2, NXOpen.CAE.Post.GroupVisibility.ShowOnly)
    
    # ----------------------------------------------
    #   Menu: Tools->Automation->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()