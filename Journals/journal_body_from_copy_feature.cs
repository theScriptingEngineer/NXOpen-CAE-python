// Simcenter 3D 2212
// Journal created by frederik on Tue Apr  2 17:26:20 2024 W. Europe Daylight Time
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
    //   Menu: Insert->Associative Copy->Mirror Geometry...
    // ----------------------------------------------
    NXOpen.Session.UndoMarkId markId1;
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start");
    
    NXOpen.Features.Feature nullNXOpen_Features_Feature = null;
    NXOpen.Features.GeomcopyBuilder geomcopyBuilder1;
    geomcopyBuilder1 = workPart.Features.CreateGeomcopyBuilder(nullNXOpen_Features_Feature);
    
    NXOpen.Point3d origin1 = new NXOpen.Point3d(0.0, 0.0, 0.0);
    NXOpen.Vector3d normal1 = new NXOpen.Vector3d(0.0, 0.0, 1.0);
    NXOpen.Plane plane1;
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling);
    
    geomcopyBuilder1.MirrorPlane = plane1;
    
    NXOpen.Unit unit1;
    unit1 = geomcopyBuilder1.TranslateDistance.Units;
    
    NXOpen.Expression expression1;
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression2;
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    theSession.SetUndoMarkName(markId1, "Mirror Geometry Dialog");
    
    geomcopyBuilder1.Type = NXOpen.Features.GeomcopyBuilder.TransformTypes.Mirror;
    
    NXOpen.Body body1 = ((NXOpen.Body)workPart.Bodies.FindObject("BLOCK(1)"));
    bool added1;
    added1 = geomcopyBuilder1.GeometryToInstance.Add(body1);
    
    plane1.SetMethod(NXOpen.PlaneTypes.MethodType.Distance);
    
    NXOpen.NXObject[] geom1 = new NXOpen.NXObject[1];
    NXOpen.DatumPlane datumPlane1 = ((NXOpen.DatumPlane)workPart.Datums.FindObject("DATUM_CSYS(0) XY plane"));
    geom1[0] = datumPlane1;
    plane1.SetGeometry(geom1);
    
    plane1.SetFlip(false);
    
    plane1.SetReverseSide(false);
    
    NXOpen.Expression expression3;
    expression3 = plane1.Expression;
    
    expression3.RightHandSide = "0";
    
    plane1.SetAlternate(NXOpen.PlaneTypes.AlternateType.One);
    
    plane1.Evaluate();
    
    plane1.SetMethod(NXOpen.PlaneTypes.MethodType.Distance);
    
    NXOpen.NXObject[] geom2 = new NXOpen.NXObject[1];
    geom2[0] = datumPlane1;
    plane1.SetGeometry(geom2);
    
    plane1.SetFlip(false);
    
    plane1.SetReverseSide(false);
    
    NXOpen.Expression expression4;
    expression4 = plane1.Expression;
    
    expression4.RightHandSide = "0";
    
    plane1.SetAlternate(NXOpen.PlaneTypes.AlternateType.One);
    
    plane1.Evaluate();
    
    NXOpen.Session.UndoMarkId markId2;
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Mirror Geometry");
    
    theSession.DeleteUndoMark(markId2, null);
    
    NXOpen.Session.UndoMarkId markId3;
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Mirror Geometry");
    
    NXOpen.Features.Feature feature1;
    feature1 = geomcopyBuilder1.CommitFeature();
    
    theSession.DeleteUndoMark(markId3, null);
    
    theSession.SetUndoMarkName(markId1, "Mirror Geometry");
    
    NXOpen.Expression expression5 = geomcopyBuilder1.NumberOfCopies;
    geomcopyBuilder1.Destroy();
    
    try
    {
      // Expression is still in use.
      workPart.Expressions.Delete(expression2);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workPart.Expressions.Delete(expression1);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    // ----------------------------------------------
    //   Menu: Tools->Automation->Journal->Stop Recording
    // ----------------------------------------------
    
  }
  public static int GetUnloadOption(string dummy) { return (int)NXOpen.Session.LibraryUnloadOption.Immediately; }
}
