# Simcenter 3D 2306
# Journal created by HP on Tue Jul 23 10:22:48 2024 W. Europe Daylight Time
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
    usergroupIds1[0] = 1500
    # Potential journal callback detected. Pausing journal.
    
if __name__ == '__main__':
    main()