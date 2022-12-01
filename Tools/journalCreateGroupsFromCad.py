# Simcenter 3D 2023
# Journal created by Frederik on Thu Aug 25 08:43:07 2022 W. Europe Daylight Time
#
import math
import DSEDesignWorkflow
import DSEPlatform
import Join
import MoldCooling
import NXOpen
import NXOpen.Assemblies
import NXOpen.CAE
import NXOpen.Features
import NXOpen.MenuBar
import SafetyOpen
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Load Part")
    
    part1, partLoadStatus1 = theSession.Parts.Open("C:\\Users\\Frederik\\Documents\\SC2022\\Python\\hullModelNX12.prt")
    
    partLoadStatus1.Dispose()
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    baseTemplateManager1 = theSession.XYPlotManager.TemplateManager
    
    status1, partLoadStatus2 = theSession.Parts.SetActiveDisplay(part1, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workFemPart = NXOpen.BasePart.Null
    workPart = theSession.Parts.Work
    displayFemPart = NXOpen.BasePart.Null
    displayPart = theSession.Parts.Display
    partLoadStatus2.Dispose()
    # ----------------------------------------------
    #   Menu: Application->Modeling
    # ----------------------------------------------
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Modeling")
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assign Name")
    
    datumPlaneFeature1 = workPart.Features.FindObject("DATUM_PLANE(4)")
    datumPlaneFeature1.SetName("Frame00")
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId4)
    
    theSession.SetUndoMarkVisibility(markId4, "Assign Name", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    #   Menu: Window->2. hullModelNX12_fem1.fem
    # ----------------------------------------------
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    femPart1 = theSession.Parts.FindObject("hullModelNX12_fem1")
    status2, partLoadStatus3 = theSession.Parts.SetActiveDisplay(femPart1, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workPart = NXOpen.Part.Null
    workFemPart = theSession.Parts.BaseWork # hullModelNX12_fem1
    displayPart = NXOpen.Part.Null
    displayFemPart = theSession.Parts.BaseDisplay # hullModelNX12_fem1
    partLoadStatus3.Dispose()
    theSession.ApplicationSwitchImmediate("UG_APP_SFEM")
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Pre/Post")
    
    # ----------------------------------------------
    #   Menu: Window->3. hullModelNX12_fem1_sim1.sim
    # ----------------------------------------------
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    simPart1 = theSession.Parts.FindObject("hullModelNX12_fem1_sim1")
    status3, partLoadStatus4 = theSession.Parts.SetActiveDisplay(simPart1, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay
    partLoadStatus4.Dispose()
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    caePart1 = workSimPart
    selRecipeBuilder1 = caePart1.SelectionRecipes.CreateSelRecipeBuilder()
    
    unit1 = workSimPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1)
    
    expression1.SetFormula("5.0")
    
    expression2 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1)
    
    expression2.SetFormula("5.0")
    
    expression3 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1)
    
    expression3.SetFormula("5.0")
    
    expression4 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1)
    
    expression4.SetFormula("5.0")
    
    expression5 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression6 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1)
    
    expression6.SetFormula("5.0")
    
    expression7 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression8 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1)
    
    expression8.SetFormula("5.0")
    
    expression9 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1)
    
    expression9.SetFormula("5.0")
    
    expression10 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression11 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1)
    
    expression11.SetFormula("5.0")
    
    expression12 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1)
    
    expression12.SetFormula("5.0")
    
    unit2 = workSimPart.UnitCollection.FindObject("Degrees")
    expression13 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression14 = workSimPart.Expressions.CreateSystemExpressionWithUnits("360", unit2)
    
    expression14.SetFormula("360")
    
    theSession.SetUndoMarkName(markId8, "Create Selection Recipe Dialog")
    
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    xDirection1 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    yDirection1 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    xform1 = workSimPart.Xforms.CreateXform(origin1, xDirection1, yDirection1, NXOpen.SmartObject.UpdateOption.AfterModeling, 1.0)
    
    cartesianCoordinateSystem1 = workSimPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    expression1.SetFormula("100000")
    
    expression2.SetFormula("100000")
    
    expression3.SetFormula("500")
    
    scaleAboutPoint1 = NXOpen.Point3d(-7152.6268364746447, 3558.8679869288485, 0.0)
    viewCenter1 = NXOpen.Point3d(7152.6268364746447, -3558.8679869288485, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(-8940.7835455933018, 4448.5849836610605, 0.0)
    viewCenter2 = NXOpen.Point3d(8940.7835455933091, -4448.5849836610632, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(-11175.979431991631, 5560.7312295763249, 0.0)
    viewCenter3 = NXOpen.Point3d(11175.979431991631, -5560.7312295763286, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(-13969.974289989548, 6950.9140369704055, 0.0)
    viewCenter4 = NXOpen.Point3d(13969.97428998953, -6950.914036970411, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint4, viewCenter4)
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = -0.44673942119408988
    rotMatrix1.Xy = -0.89436719641466811
    rotMatrix1.Xz = -0.023047939789410013
    rotMatrix1.Yx = 0.39488655312465781
    rotMatrix1.Yy = -0.22023262709323432
    rotMatrix1.Yz = 0.89194293546444992
    rotMatrix1.Zx = -0.8028004108821174
    rotMatrix1.Zy = 0.38936474922748088
    rotMatrix1.Zz = 0.45156017577563728
    translation1 = NXOpen.Point3d(-7115.3336631949387, -586.98833788152479, -979.09072295236228)
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.0046590994835716852)
    
    origin2 = NXOpen.Point3d(0.0, 0.0, -250.0)
    xDirection2 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    yDirection2 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    xform2 = workSimPart.Xforms.CreateXform(origin2, xDirection2, yDirection2, NXOpen.SmartObject.UpdateOption.AfterModeling, 1.0)
    
    cartesianCoordinateSystem2 = workSimPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = -0.41730310092334594
    rotMatrix2.Xy = -0.90824153533018548
    rotMatrix2.Xz = -0.03091011906847085
    rotMatrix2.Yx = 0.16693753298015526
    rotMatrix2.Yy = -0.11004726454913918
    rotMatrix2.Yz = 0.97980684813270713
    rotMatrix2.Zx = -0.89330285012545352
    rotMatrix2.Zy = 0.4037163770102955
    rotMatrix2.Zz = 0.19754266600261691
    translation2 = NXOpen.Point3d(-7134.8954073411214, -570.40986093380525, 472.00170439941212)
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 0.0046590994835716852)
    
    scaleAboutPoint5 = NXOpen.Point3d(-9228.1334232654572, 1817.2324279661154, 0.0)
    viewCenter5 = NXOpen.Point3d(9228.1334232654335, -1817.2324279661154, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(-11535.166779081808, 2271.5405349576449, 0.0)
    viewCenter6 = NXOpen.Point3d(11535.166779081808, -2271.5405349576449, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(-14418.958473852261, 2839.4256686970557, 0.0)
    viewCenter7 = NXOpen.Point3d(14418.958473852261, -2839.4256686970557, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(-11535.166779081808, 2271.5405349576449, 0.0)
    viewCenter8 = NXOpen.Point3d(11535.166779081808, -2271.5405349576449, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(-9228.1334232654481, 1817.2324279661159, 0.0)
    viewCenter9 = NXOpen.Point3d(9228.1334232654481, -1817.2324279661159, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(-7382.5067386123583, 1453.7859423728928, 0.0)
    viewCenter10 = NXOpen.Point3d(7382.5067386123583, -1453.7859423728928, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(-3688.9818287712219, -2762.1932905085018, 0.0)
    viewCenter11 = NXOpen.Point3d(3688.9818287712219, 2762.1932905085096, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(-4611.227285964027, -3452.7416131356272, 0.0)
    viewCenter12 = NXOpen.Point3d(4611.227285964027, 3452.7416131356367, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(-5764.0341074550342, -4315.9270164195341, 0.0)
    viewCenter13 = NXOpen.Point3d(5764.0341074550342, 4315.9270164195459, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(-7205.0426343188083, -5394.9087705244174, 0.0)
    viewCenter14 = NXOpen.Point3d(7205.0426343187783, 5394.9087705244328, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint14, viewCenter14)
    
    expression5.SetFormula("0")
    
    expression7.SetFormula("0")
    
    expression10.SetFormula("0")
    
    expression13.SetFormula("0")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Selection Recipe")
    
    theSession.DeleteUndoMark(markId9, None)
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Selection Recipe")
    
    entitytypes1 = [None] * 2 
    entitytypes1[0] = NXOpen.CAE.CaeSetGroupFilterType.GeomFace
    entitytypes1[1] = NXOpen.CAE.CaeSetGroupFilterType.GeomBody
    selRecipeBoundingVolumeStrategy1 = selRecipeBuilder1.AddBoxBoundingVolumeStrategy(cartesianCoordinateSystem2, expression1, expression2, expression3, entitytypes1, NXOpen.CAE.SelRecipeBuilder.InputFilterType.EntireModel, NXOpen.TaggedObject.Null)
    
    boundingVolumePrimitive1 = selRecipeBoundingVolumeStrategy1.BoundingVolume
    
    boxBoundingVolume1 = boundingVolumePrimitive1
    boxBoundingVolume1.Containment = NXOpen.CAE.CaeBoundingVolumePrimitiveContainment.Inside
    
    selRecipeBuilder1.RecipeName = "SelectionRecipe"
    
    nXObject1 = selRecipeBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId10, None)
    
    theSession.SetUndoMarkName(markId8, "Create Selection Recipe")
    
    selectionRecipe1 = nXObject1
    selectionRecipe1.Display.Update()
    
    selRecipeBuilder1.Destroy()
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    caePart2 = workSimPart
    caeGroupBuilder1 = caePart2.CaeGroups.CreateGroupBuilder(NXOpen.CAE.CaeGroup.Null)
    
    caePart3 = workSimPart
    selectElementsBuilder1 = caePart3.SelectElementMgr.CreateSelectElementsBuilder()
    
    theSession.SetUndoMarkName(markId11, "New Group Dialog")
    
    caeGroupBuilder1.Label = 7
    
    caeGroupBuilder1.Name = "Group(7)"
    
    # ----------------------------------------------
    #   Dialog Begin New Group
    # ----------------------------------------------
    scaleAboutPoint15 = NXOpen.Point3d(-21961.182906328853, -6299.9757024216051, 0.0)
    viewCenter15 = NXOpen.Point3d(21961.182906328817, 6299.9757024216242, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(-17568.946325063083, -5039.9805619372846, 0.0)
    viewCenter16 = NXOpen.Point3d(17568.946325063054, 5039.9805619372992, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(-14055.157060050471, -4031.9844495498287, 0.0)
    viewCenter17 = NXOpen.Point3d(14055.15706005044, 4031.9844495498405, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint17, viewCenter17)
    
    scaleAboutPoint18 = NXOpen.Point3d(-11244.125648040384, -3225.5875596398578, 0.0)
    viewCenter18 = NXOpen.Point3d(11244.125648040346, 3225.5875596398719, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(-8995.3005184323065, -2580.4700477118859, 0.0)
    viewCenter19 = NXOpen.Point3d(8995.3005184322756, 2580.4700477119009, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint19, viewCenter19)
    
    scaleAboutPoint20 = NXOpen.Point3d(-7632.376197457711, -2674.9661339661225, 0.0)
    viewCenter20 = NXOpen.Point3d(7632.3761974576837, 2674.9661339661379, 0.0)
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint20, viewCenter20)
    
    caePart4 = workSimPart
    seeds1 = [NXOpen.CAE.CAEBody.Null] * 1 
    component1 = workSimPart.ComponentAssembly.RootComponent.FindObject("COMPONENT hullModelNX12_fem1 1")
    cAEBody1 = component1.FindObject("PROTO#CAE_Body(102)")
    seeds1[0] = cAEBody1
    relatedElemMethod1 = caePart4.SmartSelectionMgr.CreateRelatedElemMethod(seeds1, True)
    
    added1 = caeGroupBuilder1.Selection.Add(relatedElemMethod1)
    
    relatedElemMethod1.Dispose()
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New Group")
    
    caeGroupBuilder1.Name = "recipeGroup"
    
    theSession.DeleteUndoMark(markId12, None)
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New Group")
    
    caeGroupBuilder1.ClearDescription()
    
    nXObject2 = caeGroupBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId13, None)
    
    theSession.SetUndoMarkName(markId11, "New Group")
    
    caeGroupBuilder1.Destroy()
    
    selectElementsBuilder1.Destroy()
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete Selection Recipe(s)")
    
    caePart5 = workSimPart
    recipes1 = [NXOpen.CAE.SelectionRecipe.Null] * 1 
    boundingVolumeSelectionRecipe1 = selectionRecipe1
    recipes1[0] = boundingVolumeSelectionRecipe1
    caePart5.SelectionRecipes.Delete(recipes1)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()