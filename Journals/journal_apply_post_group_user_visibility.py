# Simcenter 3D 2306
# Journal created by HP on Mon Jul 22 17:20:15 2024 W. Europe Daylight Time
#
import math
import NXOpen
import NXOpen.CAE
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Show Only Group(s)")
    
    fEModelOccurrence1 = workSimPart.FindObject("FEModelOccurrence[8]")
    caeGroup1 = fEModelOccurrence1.FindObject("CaeGroup[MainBoomBottom]")
    caeGroup1.ShowOnlyGroup()
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = 0.81868981892792381
    rotMatrix1.Xy = 0.57332503243447586
    rotMatrix1.Xz = -0.032332453785181028
    rotMatrix1.Yx = -0.039084264791366577
    rotMatrix1.Yy = 0.11180874101363869
    rotMatrix1.Yz = 0.99296083793806467
    rotMatrix1.Zx = 0.5729043555686073
    rotMatrix1.Zy = -0.81166323842893884
    rotMatrix1.Zz = 0.11394466531420301
    translation1 = NXOpen.Point3d(-7554.342606962492, 2034.2802574848361, -15739.214069367838)
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.01213137740467715)
    
    results1 = [NXOpen.CAE.Result.Null] * 1 
    resultManager1 = theSession.ResultManager
    solutionResult1 = resultManager1.FindObject("SolutionResult[Full_crane_assyfem_sim.sim_Position0][Structural]")
    results1[0] = solutionResult1
    usergroupIds1 = [None] * 1 
    usergroupIds1[0] = 36
    theSession.Post.PostviewApplyUserGroupVisibility(6, results1, usergroupIds1, NXOpen.CAE.Post.GroupVisibility.ShowOnly)
    
    # ----------------------------------------------
    #   Menu: Tools->Automation->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()