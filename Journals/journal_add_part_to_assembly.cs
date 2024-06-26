// Simcenter 3D 2212
// Journal created by frederik on Fri May 17 09:50:28 2024 W. Europe Daylight Time
//
using System;
using NXOpen;

public class SCJournal
{
  public static void Main(string[] args)
  {
    NXOpen.Session theSession = NXOpen.Session.GetSession();
    NXOpen.Part workPart = theSession.Parts.Work;
    NXOpen.Part displayPart = theSession.Parts.Display;
    // ----------------------------------------------
    //   Menu: Assemblies->Components->Add Component...
    // ----------------------------------------------
    NXOpen.Session.UndoMarkId markId1;
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start");
    
    NXOpen.Assemblies.AddComponentBuilder addComponentBuilder1;
    addComponentBuilder1 = workPart.AssemblyManager.CreateAddComponentBuilder();
    
    addComponentBuilder1.SetAllowMultipleAssemblyLocations(false);
    
    NXOpen.Positioning.ComponentPositioner componentPositioner1;
    componentPositioner1 = workPart.ComponentAssembly.Positioner;
    
    componentPositioner1.ClearNetwork();
    
    NXOpen.Assemblies.Arrangement arrangement1 = ((NXOpen.Assemblies.Arrangement)workPart.ComponentAssembly.Arrangements.FindObject("Arrangement 1"));
    componentPositioner1.PrimaryArrangement = arrangement1;
    
    componentPositioner1.BeginAssemblyConstraints();
    
    bool allowInterpartPositioning1;
    allowInterpartPositioning1 = theSession.Preferences.Assemblies.InterpartPositioning;
    
    NXOpen.Unit nullNXOpen_Unit = null;
    NXOpen.Expression expression1;
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("1", nullNXOpen_Unit);
    
    NXOpen.Unit unit1 = ((NXOpen.Unit)workPart.UnitCollection.FindObject("MilliMeter"));
    NXOpen.Expression expression2;
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1);
    
    NXOpen.Expression expression3;
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Unit unit2 = ((NXOpen.Unit)workPart.UnitCollection.FindObject("Degrees"));
    NXOpen.Expression expression4;
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2);
    
    NXOpen.Positioning.Network network1;
    network1 = componentPositioner1.EstablishNetwork();
    
    NXOpen.Positioning.ComponentNetwork componentNetwork1 = ((NXOpen.Positioning.ComponentNetwork)network1);
    componentNetwork1.MoveObjectsState = true;
    
    NXOpen.Assemblies.Component nullNXOpen_Assemblies_Component = null;
    componentNetwork1.DisplayComponent = nullNXOpen_Assemblies_Component;
    
    theSession.SetUndoMarkName(markId1, "Add Component Dialog");
    
    componentNetwork1.MoveObjectsState = true;
    
    NXOpen.Session.UndoMarkId markId2;
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update");
    
    NXOpen.Assemblies.ProductInterface.InterfaceObject nullNXOpen_Assemblies_ProductInterface_InterfaceObject = null;
    addComponentBuilder1.SetComponentAnchor(nullNXOpen_Assemblies_ProductInterface_InterfaceObject);
    
    addComponentBuilder1.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.WorkPartAbsolute);
    
    addComponentBuilder1.SetCount(1);
    
    addComponentBuilder1.SetScatterOption(true);
    
    addComponentBuilder1.ReferenceSet = "Unknown";
    
    addComponentBuilder1.Layer = -1;
    
    addComponentBuilder1.SetUseReferenceSetAndApplyInitialLocation(false);
    
    addComponentBuilder1.ReferenceSet = "Entire Part";
    
    addComponentBuilder1.Layer = -1;
    
    NXOpen.BasePart[] partstouse1 = new NXOpen.BasePart[1];
    NXOpen.Part part1 = ((NXOpen.Part)theSession.Parts.FindObject("model1"));
    partstouse1[0] = part1;
    addComponentBuilder1.SetPartsToAdd(partstouse1);
    
    NXOpen.Assemblies.ProductInterface.InterfaceObject[] productinterfaceobjects1;
    addComponentBuilder1.GetAllProductInterfaceObjects(out productinterfaceobjects1);
    
    NXOpen.NXObject[] movableObjects1 = new NXOpen.NXObject[1];
    NXOpen.Assemblies.Component component1 = ((NXOpen.Assemblies.Component)workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT model1 1"));
    movableObjects1[0] = component1;
    componentNetwork1.SetMovingGroup(movableObjects1);
    
    NXOpen.Session.UndoMarkId markId3;
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Translate Along Y-axis");
    
    bool loaded1;
    loaded1 = componentNetwork1.IsReferencedGeometryLoaded();
    
    componentNetwork1.BeginDrag();
    
    NXOpen.Vector3d translation1 = new NXOpen.Vector3d(0.0, -270.0, 0.0);
    componentNetwork1.DragByTranslation(translation1);
    
    NXOpen.Vector3d translation2 = new NXOpen.Vector3d(0.0, -350.0, 0.0);
    componentNetwork1.DragByTranslation(translation2);
    
    NXOpen.Vector3d translation3 = new NXOpen.Vector3d(0.0, -380.0, 0.0);
    componentNetwork1.DragByTranslation(translation3);
    
    NXOpen.Vector3d translation4 = new NXOpen.Vector3d(0.0, -430.0, 0.0);
    componentNetwork1.DragByTranslation(translation4);
    
    componentNetwork1.EndDrag();
    
    componentNetwork1.ResetDisplay();
    
    componentNetwork1.ApplyToModel();
    
    NXOpen.Session.UndoMarkId markId4;
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Translate Along Z-axis");
    
    bool loaded2;
    loaded2 = componentNetwork1.IsReferencedGeometryLoaded();
    
    componentNetwork1.BeginDrag();
    
    NXOpen.Vector3d translation5 = new NXOpen.Vector3d(0.0, 0.0, -180.0);
    componentNetwork1.DragByTranslation(translation5);
    
    NXOpen.Vector3d translation6 = new NXOpen.Vector3d(0.0, 0.0, -220.0);
    componentNetwork1.DragByTranslation(translation6);
    
    NXOpen.Vector3d translation7 = new NXOpen.Vector3d(0.0, 0.0, -250.0);
    componentNetwork1.DragByTranslation(translation7);
    
    NXOpen.Vector3d translation8 = new NXOpen.Vector3d(0.0, 0.0, -310.0);
    componentNetwork1.DragByTranslation(translation8);
    
    NXOpen.Vector3d translation9 = new NXOpen.Vector3d(0.0, 0.0, -320.0);
    componentNetwork1.DragByTranslation(translation9);
    
    componentNetwork1.EndDrag();
    
    componentNetwork1.ResetDisplay();
    
    componentNetwork1.ApplyToModel();
    
    NXOpen.Session.UndoMarkId markId5;
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component");
    
    theSession.DeleteUndoMark(markId5, null);
    
    NXOpen.Session.UndoMarkId markId6;
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component");
    
    NXOpen.Session.UndoMarkId markId7;
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply");
    
    componentNetwork1.Solve();
    
    componentPositioner1.ClearNetwork();
    
    int nErrs1;
    nErrs1 = theSession.UpdateManager.AddToDeleteList(componentNetwork1);
    
    int nErrs2;
    nErrs2 = theSession.UpdateManager.DoUpdate(markId2);
    
    componentPositioner1.EndAssemblyConstraints();
    
    NXOpen.PDM.LogicalObject[] logicalobjects1;
    addComponentBuilder1.GetLogicalObjectsHavingUnassignedRequiredAttributes(out logicalobjects1);
    
    addComponentBuilder1.ComponentName = "MODEL1";
    
    NXOpen.NXObject nXObject1;
    nXObject1 = addComponentBuilder1.Commit();
    
    NXOpen.ErrorList errorList1;
    errorList1 = addComponentBuilder1.GetOperationFailures();
    
    errorList1.Dispose();
    addComponentBuilder1.ResetPartsToAdd();
    
    theSession.DeleteUndoMark(markId6, null);
    
    theSession.SetUndoMarkName(markId1, "Add Component");
    
    addComponentBuilder1.Destroy();
    
    NXOpen.Assemblies.Arrangement nullNXOpen_Assemblies_Arrangement = null;
    componentPositioner1.PrimaryArrangement = nullNXOpen_Assemblies_Arrangement;
    
    theSession.DeleteUndoMark(markId2, null);
    
    theSession.DeleteUndoMark(markId4, null);
    
    theSession.DeleteUndoMark(markId3, null);
    
    theSession.CleanUpFacetedFacesAndEdges();
    
    // ----------------------------------------------
    //   Menu: Tools->Automation->Journal->Stop Recording
    // ----------------------------------------------
    
  }
  public static int GetUnloadOption(string dummy) { return (int)NXOpen.Session.LibraryUnloadOption.Immediately; }
}
