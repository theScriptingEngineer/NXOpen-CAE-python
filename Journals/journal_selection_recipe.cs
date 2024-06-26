// Simcenter 3D 2306
// Journal created by HP on Thu May 16 15:34:47 2024 W. Europe Daylight Time
//
using System;
using NXOpen;

public class SCJournal
{
  public static void Main(string[] args)
  {
    NXOpen.Session theSession = NXOpen.Session.GetSession();
    NXOpen.CAE.SimPart workSimPart = ((NXOpen.CAE.SimPart)theSession.Parts.BaseWork);
    NXOpen.CAE.SimPart displaySimPart = ((NXOpen.CAE.SimPart)theSession.Parts.BaseDisplay);
    NXOpen.Matrix3x3 rotMatrix1 = new NXOpen.Matrix3x3();
    rotMatrix1.Xx = 0.65903249124569663;
    rotMatrix1.Xy = -0.75204687057664055;
    rotMatrix1.Xz = -0.010083647076971416;
    rotMatrix1.Yx = 0.24178472194616818;
    rotMatrix1.Yy = 0.19914691001207988;
    rotMatrix1.Yz = 0.94967397377523644;
    rotMatrix1.Zx = -0.71219121288872045;
    rotMatrix1.Zy = -0.62830407661300336;
    rotMatrix1.Zz = 0.31307772772200143;
    NXOpen.Point3d translation1 = new NXOpen.Point3d(-3274.553992894289, -1022.1300048056233, 14548.37343789067);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.054654067089426488);
    
    NXOpen.Session.UndoMarkId markId1;
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start");
    
    NXOpen.CAE.CaePart caePart1 = ((NXOpen.CAE.CaePart)workSimPart);
    NXOpen.CAE.SelRecipeBuilder selRecipeBuilder1;
    selRecipeBuilder1 = caePart1.SelectionRecipes.CreateSelRecipeBuilder();
    
    NXOpen.Unit unit1 = ((NXOpen.Unit)workSimPart.UnitCollection.FindObject("MilliMeter"));
    NXOpen.Expression expression1;
    expression1 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1);
    
    expression1.SetFormula("5.0");
    
    NXOpen.Expression expression2;
    expression2 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1);
    
    expression2.SetFormula("5.0");
    
    NXOpen.Expression expression3;
    expression3 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1);
    
    expression3.SetFormula("5.0");
    
    NXOpen.Expression expression4;
    expression4 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1);
    
    expression4.SetFormula("5.0");
    
    NXOpen.Expression expression5;
    expression5 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression6;
    expression6 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1);
    
    expression6.SetFormula("5.0");
    
    NXOpen.Expression expression7;
    expression7 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression8;
    expression8 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1);
    
    expression8.SetFormula("5.0");
    
    NXOpen.Expression expression9;
    expression9 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1);
    
    expression9.SetFormula("5.0");
    
    NXOpen.Expression expression10;
    expression10 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression11;
    expression11 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1);
    
    expression11.SetFormula("5.0");
    
    NXOpen.Expression expression12;
    expression12 = workSimPart.Expressions.CreateSystemExpressionWithUnits("5.0", unit1);
    
    expression12.SetFormula("5.0");
    
    NXOpen.Unit unit2 = ((NXOpen.Unit)workSimPart.UnitCollection.FindObject("Degrees"));
    NXOpen.Expression expression13;
    expression13 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit2);
    
    NXOpen.Expression expression14;
    expression14 = workSimPart.Expressions.CreateSystemExpressionWithUnits("360", unit2);
    
    expression4.SetFormula("5");
    
    expression1.SetFormula("1000");
    
    expression2.SetFormula("1000");
    
    expression3.SetFormula("1000");
    
    expression9.SetFormula("5");
    
    expression5.SetFormula("3000");
    
    expression7.SetFormula("0");
    
    expression6.SetFormula("3200");
    
    expression8.SetFormula("5");
    
    expression12.SetFormula("5");
    
    expression10.SetFormula("0");
    
    expression11.SetFormula("5");
    
    expression13.SetFormula("0");
    
    expression14.SetFormula("360");
    
    theSession.SetUndoMarkName(markId1, "Create Selection Recipe Dialog");
    
    NXOpen.Xform xform1;
    xform1 = workSimPart.Xforms.CreateXform(NXOpen.SmartObject.UpdateOption.AfterModeling, 1.0);
    
    NXOpen.CartesianCoordinateSystem cartesianCoordinateSystem1;
    cartesianCoordinateSystem1 = workSimPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    // ----------------------------------------------
    //   Dialog Begin Create Selection Recipe
    // ----------------------------------------------
    NXOpen.Matrix3x3 rotMatrix2 = new NXOpen.Matrix3x3();
    rotMatrix2.Xx = 0.90984758461543791;
    rotMatrix2.Xy = -0.4146728197373229;
    rotMatrix2.Xz = 0.014960793446516837;
    rotMatrix2.Yx = 0.14275578915039172;
    rotMatrix2.Yy = 0.34667223750667653;
    rotMatrix2.Yz = 0.92705940716124491;
    rotMatrix2.Zx = -0.38961283017054438;
    rotMatrix2.Zy = -0.84134702252590543;
    rotMatrix2.Zz = 0.37461584356949729;
    NXOpen.Point3d translation2 = new NXOpen.Point3d(-4515.3315694696867, -428.09712456852384, 12953.910887673304);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 0.05087048532741692);
    
    expression1.SetFormula("10000");
    
    NXOpen.Matrix3x3 rotMatrix3 = new NXOpen.Matrix3x3();
    rotMatrix3.Xx = 0.96895660617553214;
    rotMatrix3.Xy = -0.24603161489883982;
    rotMatrix3.Xz = -0.024321591622646542;
    rotMatrix3.Yx = 0.096072057173352834;
    rotMatrix3.Yy = 0.28405821374771439;
    rotMatrix3.Yz = 0.95398170372021973;
    rotMatrix3.Zx = -0.22780091127840338;
    rotMatrix3.Zy = -0.92670349933121587;
    rotMatrix3.Zz = 0.29887684612228116;
    NXOpen.Point3d translation3 = new NXOpen.Point3d(-4756.353874191168, -259.49136706031948, 12154.095839069334);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 0.045870888695108178);
    
    NXOpen.Matrix3x3 rotMatrix4 = new NXOpen.Matrix3x3();
    rotMatrix4.Xx = 0.64515040005741875;
    rotMatrix4.Xy = -0.76366024199283733;
    rotMatrix4.Xz = -0.024576332215990506;
    rotMatrix4.Yx = 0.23502314145918418;
    rotMatrix4.Yy = 0.16773915961413466;
    rotMatrix4.Yz = 0.95740675645756534;
    rotMatrix4.Zx = -0.72701106200965537;
    rotMatrix4.Zy = -0.6234473587492213;
    rotMatrix4.Zz = 0.28769481501098959;
    NXOpen.Point3d translation4 = new NXOpen.Point3d(-3806.8525830915419, -748.36266007905056, 14621.626004364882);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 0.044686184245675553);
    
    expression1.SetFormula("12000");
    
    NXOpen.Session.UndoMarkId markId2;
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start");
    
    NXOpen.Point3d origin1 = new NXOpen.Point3d(0.0, 0.0, 0.0);
    NXOpen.Vector3d normal1 = new NXOpen.Vector3d(0.0, 0.0, 1.0);
    NXOpen.Plane plane1;
    plane1 = workSimPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling);
    
    NXOpen.Expression expression15;
    expression15 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression16;
    expression16 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Point3d origin2 = new NXOpen.Point3d(0.0, 0.0, 0.0);
    NXOpen.Vector3d normal2 = new NXOpen.Vector3d(0.0, 0.0, 1.0);
    NXOpen.Plane plane2;
    plane2 = workSimPart.Planes.CreatePlane(origin2, normal2, NXOpen.SmartObject.UpdateOption.WithinModeling);
    
    NXOpen.Expression expression17;
    expression17 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression18;
    expression18 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Point3d origin3 = new NXOpen.Point3d(0.0, 0.0, 0.0);
    NXOpen.Vector3d normal3 = new NXOpen.Vector3d(0.0, 0.0, 1.0);
    NXOpen.Plane plane3;
    plane3 = workSimPart.Planes.CreatePlane(origin3, normal3, NXOpen.SmartObject.UpdateOption.WithinModeling);
    
    NXOpen.Expression expression19;
    expression19 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression20;
    expression20 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Point3d origin4 = new NXOpen.Point3d(0.0, 0.0, 0.0);
    NXOpen.Vector3d normal4 = new NXOpen.Vector3d(0.0, 0.0, 1.0);
    NXOpen.Plane plane4;
    plane4 = workSimPart.Planes.CreatePlane(origin4, normal4, NXOpen.SmartObject.UpdateOption.WithinModeling);
    
    NXOpen.Expression expression21;
    expression21 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression22;
    expression22 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression23;
    expression23 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit2);
    
    NXOpen.Expression expression24;
    expression24 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit2);
    
    NXOpen.Expression expression25;
    expression25 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit2);
    
    NXOpen.Expression expression26;
    expression26 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression27;
    expression27 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit2);
    
    NXOpen.Expression expression28;
    expression28 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression29;
    expression29 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit2);
    
    NXOpen.Expression expression30;
    expression30 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression31;
    expression31 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit2);
    
    theSession.SetUndoMarkName(markId2, "CSYS Dialog");
    
    // ----------------------------------------------
    //   Dialog Begin CSYS
    // ----------------------------------------------
    NXOpen.Expression expression32;
    expression32 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Point3d scaleAboutPoint1 = new NXOpen.Point3d(-4183.1301588049591, -1119.0539278331664, 0.0);
    NXOpen.Point3d viewCenter1 = new NXOpen.Point3d(4183.1301588049719, 1119.0539278331839, 0.0);
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1);
    
    NXOpen.Point3d scaleAboutPoint2 = new NXOpen.Point3d(-3346.5041270439665, -895.24314226653098, 0.0);
    NXOpen.Point3d viewCenter2 = new NXOpen.Point3d(3346.5041270439797, 895.24314226654928, 0.0);
    workSimPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2);
    
    NXOpen.Matrix3x3 rotMatrix5 = new NXOpen.Matrix3x3();
    rotMatrix5.Xx = 0.65006212216929293;
    rotMatrix5.Xy = -0.75962318100035076;
    rotMatrix5.Xz = -0.01979545926872852;
    rotMatrix5.Yx = 0.23087258006872152;
    rotMatrix5.Yy = 0.17262032085674966;
    rotMatrix5.Yz = 0.95754899435993357;
    rotMatrix5.Zx = -0.72395931452890672;
    rotMatrix5.Zy = -0.62703656010970821;
    rotMatrix5.Zz = 0.28759009578324157;
    NXOpen.Point3d translation5 = new NXOpen.Point3d(-2232.8207882622487, -314.9267389084755, 14606.541617650026);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 0.069846365595307866);
    
    NXOpen.Session.UndoMarkId markId3;
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start");
    
    NXOpen.Expression expression33;
    expression33 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression34;
    expression34 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p191_x=0.00000000000", unit1);
    
    NXOpen.Expression expression35;
    expression35 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p192_y=0.00000000000", unit1);
    
    NXOpen.Expression expression36;
    expression36 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p193_z=0.00000000000", unit1);
    
    NXOpen.Expression expression37;
    expression37 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_xdelta=0.00000000000", unit1);
    
    NXOpen.Expression expression38;
    expression38 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p195_ydelta=0.00000000000", unit1);
    
    NXOpen.Expression expression39;
    expression39 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p196_zdelta=0.00000000000", unit1);
    
    NXOpen.Expression expression40;
    expression40 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p197_radius=0.00000000000", unit1);
    
    NXOpen.Expression expression41;
    expression41 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p198_angle=0.00000000000", unit2);
    
    NXOpen.Expression expression42;
    expression42 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p199_zdelta=0.00000000000", unit1);
    
    NXOpen.Expression expression43;
    expression43 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p200_radius=0.00000000000", unit1);
    
    NXOpen.Expression expression44;
    expression44 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p201_angle1=0.00000000000", unit2);
    
    NXOpen.Expression expression45;
    expression45 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p202_angle2=0.00000000000", unit2);
    
    NXOpen.Expression expression46;
    expression46 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p203_distance=0", unit1);
    
    NXOpen.Expression expression47;
    expression47 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p204_arclen=0", unit1);
    
    NXOpen.Unit nullNXOpen_Unit = null;
    NXOpen.Expression expression48;
    expression48 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p205_percent=0", nullNXOpen_Unit);
    
    expression34.SetFormula("750");
    
    expression35.SetFormula("-5000");
    
    expression36.SetFormula("5500");
    
    expression37.SetFormula("0");
    
    expression38.SetFormula("0");
    
    expression39.SetFormula("0");
    
    expression40.SetFormula("0");
    
    expression41.SetFormula("0");
    
    expression42.SetFormula("0");
    
    expression43.SetFormula("0");
    
    expression44.SetFormula("0");
    
    expression45.SetFormula("0");
    
    expression46.SetFormula("0");
    
    expression48.SetFormula("100");
    
    expression47.SetFormula("0");
    
    theSession.SetUndoMarkName(markId3, "Point Dialog");
    
    NXOpen.Expression expression49;
    expression49 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p206_x=0.00000000000", unit1);
    
    NXOpen.Scalar scalar1;
    scalar1 = workSimPart.Scalars.CreateScalarExpression(expression49, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression50;
    expression50 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p207_y=0.00000000000", unit1);
    
    NXOpen.Scalar scalar2;
    scalar2 = workSimPart.Scalars.CreateScalarExpression(expression50, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression51;
    expression51 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p208_z=0.00000000000", unit1);
    
    NXOpen.Scalar scalar3;
    scalar3 = workSimPart.Scalars.CreateScalarExpression(expression51, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point1;
    point1 = workSimPart.Points.CreatePoint(scalar1, scalar2, scalar3, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    expression34.SetFormula("0");
    
    expression35.SetFormula("0");
    
    expression36.SetFormula("0");
    
    expression34.SetFormula("0.00000000000");
    
    expression35.SetFormula("0.00000000000");
    
    expression36.SetFormula("0.00000000000");
    
    expression34.SetFormula("0");
    
    expression35.SetFormula("0");
    
    expression36.SetFormula("0");
    
    expression34.SetFormula("0.00000000000");
    
    expression35.SetFormula("0.00000000000");
    
    expression36.SetFormula("0.00000000000");
    
    expression37.SetFormula("0.00000000000");
    
    expression38.SetFormula("0.00000000000");
    
    expression39.SetFormula("0.00000000000");
    
    expression40.SetFormula("0.00000000000");
    
    expression41.SetFormula("0.00000000000");
    
    expression42.SetFormula("0.00000000000");
    
    expression43.SetFormula("0.00000000000");
    
    expression44.SetFormula("0.00000000000");
    
    expression45.SetFormula("0.00000000000");
    
    expression48.SetFormula("100.00000000000");
    
    // ----------------------------------------------
    //   Dialog Begin Point
    // ----------------------------------------------
    NXOpen.Matrix3x3 rotMatrix6 = new NXOpen.Matrix3x3();
    rotMatrix6.Xx = 0.49067618419655079;
    rotMatrix6.Xy = -0.87129686391590866;
    rotMatrix6.Xz = -0.0088688890292325153;
    rotMatrix6.Yx = 0.2400506629539127;
    rotMatrix6.Yy = 0.12538745670769252;
    rotMatrix6.Yz = 0.96262851864868537;
    rotMatrix6.Zx = -0.83762316197541964;
    rotMatrix6.Zy = -0.47446787102044702;
    rotMatrix6.Zz = 0.27068002861611662;
    NXOpen.Point3d translation6 = new NXOpen.Point3d(-1890.2188571193542, -57.589696949615217, 15168.367077062216);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix6, translation6, 0.059388559840087285);
    
    expression35.SetFormula("400");
    
    workSimPart.Points.DeletePoint(point1);
    
    expression34.RightHandSide = "0.00000000000";
    
    expression35.RightHandSide = "400";
    
    expression36.RightHandSide = "0.00000000000";
    
    NXOpen.Expression expression52;
    expression52 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p192_x=0.00000000000", unit1);
    
    NXOpen.Scalar scalar4;
    scalar4 = workSimPart.Scalars.CreateScalarExpression(expression52, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression53;
    expression53 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p193_y=400", unit1);
    
    NXOpen.Scalar scalar5;
    scalar5 = workSimPart.Scalars.CreateScalarExpression(expression53, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression54;
    expression54 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_z=0.00000000000", unit1);
    
    NXOpen.Scalar scalar6;
    scalar6 = workSimPart.Scalars.CreateScalarExpression(expression54, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point2;
    point2 = workSimPart.Points.CreatePoint(scalar4, scalar5, scalar6, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    expression36.SetFormula("-500");
    
    expression34.RightHandSide = "0.00000000000";
    
    expression35.RightHandSide = "400";
    
    expression36.RightHandSide = "-500";
    
    workSimPart.Points.DeletePoint(point2);
    
    NXOpen.Expression expression55;
    expression55 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p192_x=0.00000000000", unit1);
    
    NXOpen.Scalar scalar7;
    scalar7 = workSimPart.Scalars.CreateScalarExpression(expression55, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression56;
    expression56 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p193_y=400", unit1);
    
    NXOpen.Scalar scalar8;
    scalar8 = workSimPart.Scalars.CreateScalarExpression(expression56, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression57;
    expression57 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_z=-500", unit1);
    
    NXOpen.Scalar scalar9;
    scalar9 = workSimPart.Scalars.CreateScalarExpression(expression57, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point3;
    point3 = workSimPart.Points.CreatePoint(scalar7, scalar8, scalar9, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Matrix3x3 rotMatrix7 = new NXOpen.Matrix3x3();
    rotMatrix7.Xx = 0.25418536320668605;
    rotMatrix7.Xy = -0.96693910382891834;
    rotMatrix7.Xz = 0.020458998460644369;
    rotMatrix7.Yx = 0.12408746153902182;
    rotMatrix7.Yy = 0.053584006652714997;
    rotMatrix7.Yz = 0.99082342327977024;
    rotMatrix7.Zx = -0.95916218806846609;
    rotMatrix7.Zy = -0.24931410653544811;
    rotMatrix7.Zz = 0.13360528905003358;
    NXOpen.Point3d translation7 = new NXOpen.Point3d(-921.20044236228728, 345.9219156978441, 15769.118509511929);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix7, translation7, 0.059409145913581277);
    
    expression36.SetFormula("-600");
    
    expression34.RightHandSide = "0.00000000000";
    
    expression35.RightHandSide = "400";
    
    expression36.RightHandSide = "-600";
    
    workSimPart.Points.DeletePoint(point3);
    
    NXOpen.Expression expression58;
    expression58 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p192_x=0.00000000000", unit1);
    
    NXOpen.Scalar scalar10;
    scalar10 = workSimPart.Scalars.CreateScalarExpression(expression58, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression59;
    expression59 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p193_y=400", unit1);
    
    NXOpen.Scalar scalar11;
    scalar11 = workSimPart.Scalars.CreateScalarExpression(expression59, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression60;
    expression60 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_z=-600", unit1);
    
    NXOpen.Scalar scalar12;
    scalar12 = workSimPart.Scalars.CreateScalarExpression(expression60, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point4;
    point4 = workSimPart.Points.CreatePoint(scalar10, scalar11, scalar12, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Session.UndoMarkId markId4;
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Point");
    
    theSession.DeleteUndoMark(markId4, null);
    
    NXOpen.Session.UndoMarkId markId5;
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Point");
    
    expression34.RightHandSide = "0.00000000000";
    
    expression35.RightHandSide = "400";
    
    expression36.RightHandSide = "-600";
    
    workSimPart.Points.DeletePoint(point4);
    
    NXOpen.Expression expression61;
    expression61 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p192_x=0.00000000000", unit1);
    
    NXOpen.Scalar scalar13;
    scalar13 = workSimPart.Scalars.CreateScalarExpression(expression61, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression62;
    expression62 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p193_y=400", unit1);
    
    NXOpen.Scalar scalar14;
    scalar14 = workSimPart.Scalars.CreateScalarExpression(expression62, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression63;
    expression63 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_z=-600", unit1);
    
    NXOpen.Scalar scalar15;
    scalar15 = workSimPart.Scalars.CreateScalarExpression(expression63, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point5;
    point5 = workSimPart.Points.CreatePoint(scalar13, scalar14, scalar15, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    theSession.DeleteUndoMark(markId5, null);
    
    theSession.SetUndoMarkName(markId3, "Point");
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression34);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression35);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression36);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression37);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression38);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression39);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression40);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression41);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression42);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression43);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression44);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression45);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression46);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression47);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression48);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    workSimPart.MeasureManager.SetPartTransientModification();
    
    workSimPart.Expressions.Delete(expression33);
    
    workSimPart.MeasureManager.ClearPartTransientModification();
    
    theSession.DeleteUndoMark(markId3, null);
    
    NXOpen.Scalar scalar16;
    scalar16 = workSimPart.Scalars.CreateScalarExpression(expression61, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Scalar scalar17;
    scalar17 = workSimPart.Scalars.CreateScalarExpression(expression62, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Scalar scalar18;
    scalar18 = workSimPart.Scalars.CreateScalarExpression(expression63, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point6;
    point6 = workSimPart.Points.CreatePoint(scalar16, scalar17, scalar18, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Matrix3x3 rotMatrix8 = new NXOpen.Matrix3x3();
    rotMatrix8.Xx = 0.30367960635044472;
    rotMatrix8.Xy = -0.95277072727421031;
    rotMatrix8.Xz = 0.002576419261401119;
    rotMatrix8.Yx = 0.16545971476601715;
    rotMatrix8.Yy = 0.055400144738673392;
    rotMatrix8.Yz = 0.98465928460177599;
    rotMatrix8.Zx = -0.93829727670732699;
    rotMatrix8.Zy = -0.29859465034106897;
    rotMatrix8.Zz = 0.17446906691819591;
    NXOpen.Point3d translation8 = new NXOpen.Point3d(-1151.5391271804604, 111.47866475401315, 15665.98599486973);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix8, translation8, 0.062840081337838388);
    
    NXOpen.Session.UndoMarkId markId6;
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start");
    
    NXOpen.Expression expression64;
    expression64 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression65;
    expression65 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p191_x=0.00000000000", unit1);
    
    NXOpen.Expression expression66;
    expression66 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p192_y=0.00000000000", unit1);
    
    NXOpen.Expression expression67;
    expression67 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p193_z=0.00000000000", unit1);
    
    NXOpen.Expression expression68;
    expression68 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_xdelta=0.00000000000", unit1);
    
    NXOpen.Expression expression69;
    expression69 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p195_ydelta=0.00000000000", unit1);
    
    NXOpen.Expression expression70;
    expression70 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p196_zdelta=0.00000000000", unit1);
    
    NXOpen.Expression expression71;
    expression71 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p197_radius=0.00000000000", unit1);
    
    NXOpen.Expression expression72;
    expression72 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p198_angle=0.00000000000", unit2);
    
    NXOpen.Expression expression73;
    expression73 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p199_zdelta=0.00000000000", unit1);
    
    NXOpen.Expression expression74;
    expression74 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p200_radius=0.00000000000", unit1);
    
    NXOpen.Expression expression75;
    expression75 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p201_angle1=0.00000000000", unit2);
    
    NXOpen.Expression expression76;
    expression76 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p202_angle2=0.00000000000", unit2);
    
    NXOpen.Expression expression77;
    expression77 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p203_distance=0", unit1);
    
    NXOpen.Expression expression78;
    expression78 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p204_arclen=0", unit1);
    
    NXOpen.Expression expression79;
    expression79 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p205_percent=0", nullNXOpen_Unit);
    
    expression65.SetFormula("0");
    
    expression66.SetFormula("400");
    
    expression67.SetFormula("-600");
    
    expression68.SetFormula("0");
    
    expression69.SetFormula("0");
    
    expression70.SetFormula("0");
    
    expression71.SetFormula("0");
    
    expression72.SetFormula("0");
    
    expression73.SetFormula("0");
    
    expression74.SetFormula("0");
    
    expression75.SetFormula("0");
    
    expression76.SetFormula("0");
    
    expression77.SetFormula("0");
    
    expression79.SetFormula("100");
    
    expression78.SetFormula("0");
    
    theSession.SetUndoMarkName(markId6, "Point Dialog");
    
    NXOpen.Expression expression80;
    expression80 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p206_x=0.00000000000", unit1);
    
    NXOpen.Scalar scalar19;
    scalar19 = workSimPart.Scalars.CreateScalarExpression(expression80, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression81;
    expression81 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p207_y=0.00000000000", unit1);
    
    NXOpen.Scalar scalar20;
    scalar20 = workSimPart.Scalars.CreateScalarExpression(expression81, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression82;
    expression82 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p208_z=0.00000000000", unit1);
    
    NXOpen.Scalar scalar21;
    scalar21 = workSimPart.Scalars.CreateScalarExpression(expression82, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point7;
    point7 = workSimPart.Points.CreatePoint(scalar19, scalar20, scalar21, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    expression66.SetFormula("0");
    
    expression67.SetFormula("0");
    
    expression65.SetFormula("0.00000000000");
    
    expression66.SetFormula("0.00000000000");
    
    expression67.SetFormula("0.00000000000");
    
    expression65.SetFormula("0");
    
    expression66.SetFormula("0");
    
    expression67.SetFormula("0");
    
    expression65.SetFormula("0.00000000000");
    
    expression66.SetFormula("0.00000000000");
    
    expression67.SetFormula("0.00000000000");
    
    expression68.SetFormula("0.00000000000");
    
    expression69.SetFormula("0.00000000000");
    
    expression70.SetFormula("0.00000000000");
    
    expression71.SetFormula("0.00000000000");
    
    expression72.SetFormula("0.00000000000");
    
    expression73.SetFormula("0.00000000000");
    
    expression74.SetFormula("0.00000000000");
    
    expression75.SetFormula("0.00000000000");
    
    expression76.SetFormula("0.00000000000");
    
    expression79.SetFormula("100.00000000000");
    
    // ----------------------------------------------
    //   Dialog Begin Point
    // ----------------------------------------------
    expression65.SetFormula("100");
    
    workSimPart.Points.DeletePoint(point7);
    
    expression65.RightHandSide = "100";
    
    expression66.RightHandSide = "0.00000000000";
    
    expression67.RightHandSide = "0.00000000000";
    
    NXOpen.Expression expression83;
    expression83 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p193_x=100", unit1);
    
    NXOpen.Scalar scalar22;
    scalar22 = workSimPart.Scalars.CreateScalarExpression(expression83, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression84;
    expression84 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_y=0.00000000000", unit1);
    
    NXOpen.Scalar scalar23;
    scalar23 = workSimPart.Scalars.CreateScalarExpression(expression84, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression85;
    expression85 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p195_z=0.00000000000", unit1);
    
    NXOpen.Scalar scalar24;
    scalar24 = workSimPart.Scalars.CreateScalarExpression(expression85, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point8;
    point8 = workSimPart.Points.CreatePoint(scalar22, scalar23, scalar24, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    expression66.SetFormula("400");
    
    expression65.RightHandSide = "100";
    
    expression66.RightHandSide = "400";
    
    expression67.RightHandSide = "0.00000000000";
    
    workSimPart.Points.DeletePoint(point8);
    
    NXOpen.Expression expression86;
    expression86 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p193_x=100", unit1);
    
    NXOpen.Scalar scalar25;
    scalar25 = workSimPart.Scalars.CreateScalarExpression(expression86, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression87;
    expression87 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_y=400", unit1);
    
    NXOpen.Scalar scalar26;
    scalar26 = workSimPart.Scalars.CreateScalarExpression(expression87, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression88;
    expression88 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p195_z=0.00000000000", unit1);
    
    NXOpen.Scalar scalar27;
    scalar27 = workSimPart.Scalars.CreateScalarExpression(expression88, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point9;
    point9 = workSimPart.Points.CreatePoint(scalar25, scalar26, scalar27, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    expression67.SetFormula("-600");
    
    expression65.RightHandSide = "100";
    
    expression66.RightHandSide = "400";
    
    expression67.RightHandSide = "-600";
    
    workSimPart.Points.DeletePoint(point9);
    
    NXOpen.Expression expression89;
    expression89 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p193_x=100", unit1);
    
    NXOpen.Scalar scalar28;
    scalar28 = workSimPart.Scalars.CreateScalarExpression(expression89, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression90;
    expression90 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_y=400", unit1);
    
    NXOpen.Scalar scalar29;
    scalar29 = workSimPart.Scalars.CreateScalarExpression(expression90, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression91;
    expression91 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p195_z=-600", unit1);
    
    NXOpen.Scalar scalar30;
    scalar30 = workSimPart.Scalars.CreateScalarExpression(expression91, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point10;
    point10 = workSimPart.Points.CreatePoint(scalar28, scalar29, scalar30, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Matrix3x3 rotMatrix9 = new NXOpen.Matrix3x3();
    rotMatrix9.Xx = 0.82214038224975516;
    rotMatrix9.Xy = -0.56344966198992019;
    rotMatrix9.Xz = 0.081299878706366208;
    rotMatrix9.Yx = 0.045042987616304903;
    rotMatrix9.Yy = 0.20674552160964976;
    rotMatrix9.Yz = 0.97735736481644664;
    rotMatrix9.Zx = -0.56750006267913466;
    rotMatrix9.Zy = -0.7998629680750301;
    rotMatrix9.Zz = 0.19535329831200207;
    NXOpen.Point3d translation9 = new NXOpen.Point3d(-3129.1626392617404, 679.32509057067034, 13833.184098750684);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix9, translation9, 0.058621709830631072);
    
    NXOpen.Session.UndoMarkId markId7;
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Point");
    
    theSession.DeleteUndoMark(markId7, null);
    
    NXOpen.Session.UndoMarkId markId8;
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Point");
    
    expression65.RightHandSide = "100";
    
    expression66.RightHandSide = "400";
    
    expression67.RightHandSide = "-600";
    
    workSimPart.Points.DeletePoint(point10);
    
    NXOpen.Expression expression92;
    expression92 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p193_x=100", unit1);
    
    NXOpen.Scalar scalar31;
    scalar31 = workSimPart.Scalars.CreateScalarExpression(expression92, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression93;
    expression93 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_y=400", unit1);
    
    NXOpen.Scalar scalar32;
    scalar32 = workSimPart.Scalars.CreateScalarExpression(expression93, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression94;
    expression94 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p195_z=-600", unit1);
    
    NXOpen.Scalar scalar33;
    scalar33 = workSimPart.Scalars.CreateScalarExpression(expression94, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point11;
    point11 = workSimPart.Points.CreatePoint(scalar31, scalar32, scalar33, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    theSession.DeleteUndoMark(markId8, null);
    
    theSession.SetUndoMarkName(markId6, "Point");
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression65);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression66);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression67);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression68);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression69);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression70);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression71);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression72);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression73);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression74);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression75);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression76);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression77);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression78);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression79);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    workSimPart.MeasureManager.SetPartTransientModification();
    
    workSimPart.Expressions.Delete(expression64);
    
    workSimPart.MeasureManager.ClearPartTransientModification();
    
    theSession.DeleteUndoMark(markId6, null);
    
    NXOpen.Scalar scalar34;
    scalar34 = workSimPart.Scalars.CreateScalarExpression(expression92, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Scalar scalar35;
    scalar35 = workSimPart.Scalars.CreateScalarExpression(expression93, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Scalar scalar36;
    scalar36 = workSimPart.Scalars.CreateScalarExpression(expression94, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point12;
    point12 = workSimPart.Points.CreatePoint(scalar34, scalar35, scalar36, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Matrix3x3 rotMatrix10 = new NXOpen.Matrix3x3();
    rotMatrix10.Xx = 0.58224400920527764;
    rotMatrix10.Xy = -0.81225410013640997;
    rotMatrix10.Xz = -0.035145277864217249;
    rotMatrix10.Yx = 0.19530866292272175;
    rotMatrix10.Yy = 0.097778005255171371;
    rotMatrix10.Yz = 0.97585551588114505;
    rotMatrix10.Zx = -0.78920620875149061;
    rotMatrix10.Zy = -0.57505020519943262;
    rotMatrix10.Zz = 0.21557092004300316;
    NXOpen.Point3d translation10 = new NXOpen.Point3d(-2449.2649593007595, -43.423068335896119, 14929.048440578677);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix10, translation10, 0.063310072514406457);
    
    NXOpen.Session.UndoMarkId markId9;
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start");
    
    NXOpen.Expression expression95;
    expression95 = workSimPart.Expressions.CreateSystemExpressionWithUnits("0", unit1);
    
    NXOpen.Expression expression96;
    expression96 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p191_x=0.00000000000", unit1);
    
    NXOpen.Expression expression97;
    expression97 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p192_y=0.00000000000", unit1);
    
    NXOpen.Expression expression98;
    expression98 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p193_z=0.00000000000", unit1);
    
    NXOpen.Expression expression99;
    expression99 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_xdelta=0.00000000000", unit1);
    
    NXOpen.Expression expression100;
    expression100 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p195_ydelta=0.00000000000", unit1);
    
    NXOpen.Expression expression101;
    expression101 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p196_zdelta=0.00000000000", unit1);
    
    NXOpen.Expression expression102;
    expression102 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p197_radius=0.00000000000", unit1);
    
    NXOpen.Expression expression103;
    expression103 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p198_angle=0.00000000000", unit2);
    
    NXOpen.Expression expression104;
    expression104 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p199_zdelta=0.00000000000", unit1);
    
    NXOpen.Expression expression105;
    expression105 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p200_radius=0.00000000000", unit1);
    
    NXOpen.Expression expression106;
    expression106 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p201_angle1=0.00000000000", unit2);
    
    NXOpen.Expression expression107;
    expression107 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p202_angle2=0.00000000000", unit2);
    
    NXOpen.Expression expression108;
    expression108 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p203_distance=0", unit1);
    
    NXOpen.Expression expression109;
    expression109 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p204_arclen=0", unit1);
    
    NXOpen.Expression expression110;
    expression110 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p205_percent=0", nullNXOpen_Unit);
    
    expression96.SetFormula("100");
    
    expression97.SetFormula("400");
    
    expression98.SetFormula("-600");
    
    expression99.SetFormula("0");
    
    expression100.SetFormula("0");
    
    expression101.SetFormula("0");
    
    expression102.SetFormula("0");
    
    expression103.SetFormula("0");
    
    expression104.SetFormula("0");
    
    expression105.SetFormula("0");
    
    expression106.SetFormula("0");
    
    expression107.SetFormula("0");
    
    expression108.SetFormula("0");
    
    expression110.SetFormula("100");
    
    expression109.SetFormula("0");
    
    theSession.SetUndoMarkName(markId9, "Point Dialog");
    
    NXOpen.Expression expression111;
    expression111 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p206_x=0.00000000000", unit1);
    
    NXOpen.Scalar scalar37;
    scalar37 = workSimPart.Scalars.CreateScalarExpression(expression111, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression112;
    expression112 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p207_y=0.00000000000", unit1);
    
    NXOpen.Scalar scalar38;
    scalar38 = workSimPart.Scalars.CreateScalarExpression(expression112, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression113;
    expression113 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p208_z=0.00000000000", unit1);
    
    NXOpen.Scalar scalar39;
    scalar39 = workSimPart.Scalars.CreateScalarExpression(expression113, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point13;
    point13 = workSimPart.Points.CreatePoint(scalar37, scalar38, scalar39, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    expression96.SetFormula("0");
    
    expression97.SetFormula("0");
    
    expression98.SetFormula("0");
    
    expression96.SetFormula("0.00000000000");
    
    expression97.SetFormula("0.00000000000");
    
    expression98.SetFormula("0.00000000000");
    
    expression96.SetFormula("0");
    
    expression97.SetFormula("0");
    
    expression98.SetFormula("0");
    
    expression96.SetFormula("0.00000000000");
    
    expression97.SetFormula("0.00000000000");
    
    expression98.SetFormula("0.00000000000");
    
    expression99.SetFormula("0.00000000000");
    
    expression100.SetFormula("0.00000000000");
    
    expression101.SetFormula("0.00000000000");
    
    expression102.SetFormula("0.00000000000");
    
    expression103.SetFormula("0.00000000000");
    
    expression104.SetFormula("0.00000000000");
    
    expression105.SetFormula("0.00000000000");
    
    expression106.SetFormula("0.00000000000");
    
    expression107.SetFormula("0.00000000000");
    
    expression110.SetFormula("100.00000000000");
    
    // ----------------------------------------------
    //   Dialog Begin Point
    // ----------------------------------------------
    expression96.SetFormula("0");
    
    workSimPart.Points.DeletePoint(point13);
    
    expression96.RightHandSide = "0";
    
    expression97.RightHandSide = "0.00000000000";
    
    expression98.RightHandSide = "0.00000000000";
    
    NXOpen.Expression expression114;
    expression114 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_x=0", unit1);
    
    NXOpen.Scalar scalar40;
    scalar40 = workSimPart.Scalars.CreateScalarExpression(expression114, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression115;
    expression115 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p195_y=0.00000000000", unit1);
    
    NXOpen.Scalar scalar41;
    scalar41 = workSimPart.Scalars.CreateScalarExpression(expression115, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression116;
    expression116 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p196_z=0.00000000000", unit1);
    
    NXOpen.Scalar scalar42;
    scalar42 = workSimPart.Scalars.CreateScalarExpression(expression116, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point14;
    point14 = workSimPart.Points.CreatePoint(scalar40, scalar41, scalar42, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    expression97.SetFormula("500");
    
    expression96.RightHandSide = "0";
    
    expression97.RightHandSide = "500";
    
    expression98.RightHandSide = "0.00000000000";
    
    workSimPart.Points.DeletePoint(point14);
    
    NXOpen.Expression expression117;
    expression117 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_x=0", unit1);
    
    NXOpen.Scalar scalar43;
    scalar43 = workSimPart.Scalars.CreateScalarExpression(expression117, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression118;
    expression118 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p195_y=500", unit1);
    
    NXOpen.Scalar scalar44;
    scalar44 = workSimPart.Scalars.CreateScalarExpression(expression118, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression119;
    expression119 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p196_z=0.00000000000", unit1);
    
    NXOpen.Scalar scalar45;
    scalar45 = workSimPart.Scalars.CreateScalarExpression(expression119, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point15;
    point15 = workSimPart.Points.CreatePoint(scalar43, scalar44, scalar45, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    expression98.SetFormula("-600");
    
    expression96.RightHandSide = "0";
    
    expression97.RightHandSide = "500";
    
    expression98.RightHandSide = "-600";
    
    workSimPart.Points.DeletePoint(point15);
    
    NXOpen.Expression expression120;
    expression120 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_x=0", unit1);
    
    NXOpen.Scalar scalar46;
    scalar46 = workSimPart.Scalars.CreateScalarExpression(expression120, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression121;
    expression121 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p195_y=500", unit1);
    
    NXOpen.Scalar scalar47;
    scalar47 = workSimPart.Scalars.CreateScalarExpression(expression121, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression122;
    expression122 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p196_z=-600", unit1);
    
    NXOpen.Scalar scalar48;
    scalar48 = workSimPart.Scalars.CreateScalarExpression(expression122, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point16;
    point16 = workSimPart.Points.CreatePoint(scalar46, scalar47, scalar48, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Session.UndoMarkId markId10;
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Point");
    
    theSession.DeleteUndoMark(markId10, null);
    
    NXOpen.Session.UndoMarkId markId11;
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Point");
    
    expression96.RightHandSide = "0";
    
    expression97.RightHandSide = "500";
    
    expression98.RightHandSide = "-600";
    
    workSimPart.Points.DeletePoint(point16);
    
    NXOpen.Expression expression123;
    expression123 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p194_x=0", unit1);
    
    NXOpen.Scalar scalar49;
    scalar49 = workSimPart.Scalars.CreateScalarExpression(expression123, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression124;
    expression124 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p195_y=500", unit1);
    
    NXOpen.Scalar scalar50;
    scalar50 = workSimPart.Scalars.CreateScalarExpression(expression124, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Expression expression125;
    expression125 = workSimPart.Expressions.CreateSystemExpressionWithUnits("p196_z=-600", unit1);
    
    NXOpen.Scalar scalar51;
    scalar51 = workSimPart.Scalars.CreateScalarExpression(expression125, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point17;
    point17 = workSimPart.Points.CreatePoint(scalar49, scalar50, scalar51, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    theSession.DeleteUndoMark(markId11, null);
    
    theSession.SetUndoMarkName(markId9, "Point");
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression96);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression97);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression98);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression99);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression100);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression101);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression102);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression103);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression104);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression105);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression106);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression107);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression108);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression109);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression110);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    workSimPart.MeasureManager.SetPartTransientModification();
    
    workSimPart.Expressions.Delete(expression95);
    
    workSimPart.MeasureManager.ClearPartTransientModification();
    
    theSession.DeleteUndoMark(markId9, null);
    
    NXOpen.Scalar scalar52;
    scalar52 = workSimPart.Scalars.CreateScalarExpression(expression123, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Scalar scalar53;
    scalar53 = workSimPart.Scalars.CreateScalarExpression(expression124, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Scalar scalar54;
    scalar54 = workSimPart.Scalars.CreateScalarExpression(expression125, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point18;
    point18 = workSimPart.Points.CreatePoint(scalar52, scalar53, scalar54, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Xform xform2;
    xform2 = workSimPart.Xforms.CreateXform(point5, point11, point17, NXOpen.SmartObject.UpdateOption.AfterModeling, 1.0);
    
    NXOpen.Session.UndoMarkId markId12;
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "CSYS");
    
    theSession.DeleteUndoMark(markId12, null);
    
    NXOpen.Session.UndoMarkId markId13;
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "CSYS");
    
    NXOpen.CartesianCoordinateSystem cartesianCoordinateSystem2;
    cartesianCoordinateSystem2 = workSimPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    theSession.DeleteUndoMark(markId13, null);
    
    theSession.SetUndoMarkName(markId2, "CSYS");
    
    workSimPart.Expressions.Delete(expression26);
    
    workSimPart.Expressions.Delete(expression28);
    
    workSimPart.Expressions.Delete(expression30);
    
    workSimPart.Expressions.Delete(expression27);
    
    workSimPart.Expressions.Delete(expression29);
    
    workSimPart.Expressions.Delete(expression31);
    
    workSimPart.Expressions.Delete(expression23);
    
    workSimPart.Expressions.Delete(expression24);
    
    workSimPart.Expressions.Delete(expression25);
    
    workSimPart.Points.DeletePoint(point6);
    
    workSimPart.Points.DeletePoint(point12);
    
    workSimPart.Points.DeletePoint(point18);
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression16);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression18);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression20);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression22);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    workSimPart.MeasureManager.SetPartTransientModification();
    
    workSimPart.Expressions.Delete(expression32);
    
    workSimPart.MeasureManager.ClearPartTransientModification();
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression15);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    plane1.DestroyPlane();
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression17);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    plane2.DestroyPlane();
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression19);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    plane3.DestroyPlane();
    
    try
    {
      // Expression is still in use.
      workSimPart.Expressions.Delete(expression21);
    }
    catch (NXException ex)
    {
      ex.AssertErrorCode(1050029);
    }
    
    plane4.DestroyPlane();
    
    theSession.DeleteUndoMark(markId2, null);
    
    NXOpen.Scalar scalar55;
    scalar55 = workSimPart.Scalars.CreateScalarExpression(expression61, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Scalar scalar56;
    scalar56 = workSimPart.Scalars.CreateScalarExpression(expression62, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Scalar scalar57;
    scalar57 = workSimPart.Scalars.CreateScalarExpression(expression63, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point19;
    point19 = workSimPart.Points.CreatePoint(scalar55, scalar56, scalar57, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Scalar scalar58;
    scalar58 = workSimPart.Scalars.CreateScalarExpression(expression92, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Scalar scalar59;
    scalar59 = workSimPart.Scalars.CreateScalarExpression(expression93, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Scalar scalar60;
    scalar60 = workSimPart.Scalars.CreateScalarExpression(expression94, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point20;
    point20 = workSimPart.Points.CreatePoint(scalar58, scalar59, scalar60, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Scalar scalar61;
    scalar61 = workSimPart.Scalars.CreateScalarExpression(expression123, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Scalar scalar62;
    scalar62 = workSimPart.Scalars.CreateScalarExpression(expression124, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Scalar scalar63;
    scalar63 = workSimPart.Scalars.CreateScalarExpression(expression125, NXOpen.Scalar.DimensionalityType.None, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Point point21;
    point21 = workSimPart.Points.CreatePoint(scalar61, scalar62, scalar63, NXOpen.SmartObject.UpdateOption.AfterModeling);
    
    NXOpen.Matrix3x3 rotMatrix11 = new NXOpen.Matrix3x3();
    rotMatrix11.Xx = -0.010563312333795385;
    rotMatrix11.Xy = -0.9999346535308864;
    rotMatrix11.Xz = -0.0043709381831635108;
    rotMatrix11.Yx = 0.050352722732216464;
    rotMatrix11.Yy = -0.0048975527226842869;
    rotMatrix11.Yz = 0.99871948879091177;
    rotMatrix11.Zx = -0.99867563289888528;
    rotMatrix11.Zy = 0.010329697255529128;
    rotMatrix11.Zz = 0.050401166738652803;
    NXOpen.Point3d translation11 = new NXOpen.Point3d(-1656.2830494241496, 609.21396888147376, 15956.169786503906);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix11, translation11, 0.048776459698918063);
    
    expression2.SetFormula("500");
    
    NXOpen.Matrix3x3 rotMatrix12 = new NXOpen.Matrix3x3();
    rotMatrix12.Xx = 0.024920421658832473;
    rotMatrix12.Xy = -0.99968269960085276;
    rotMatrix12.Xz = 0.0036705180959981727;
    rotMatrix12.Yx = 0.032056949611945787;
    rotMatrix12.Yy = 0.0044688856206259618;
    rotMatrix12.Yz = 0.99947605326135114;
    rotMatrix12.Zx = -0.99917532223625349;
    rotMatrix12.Zy = -0.024789699071526738;
    rotMatrix12.Zz = 0.032158144443045787;
    NXOpen.Point3d translation12 = new NXOpen.Point3d(-1814.5835189334748, 692.47228728878247, 15957.727534110985);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix12, translation12, 0.049431649465242949);
    
    expression3.SetFormula("1500");
    
    NXOpen.Matrix3x3 rotMatrix13 = new NXOpen.Matrix3x3();
    rotMatrix13.Xx = 0.50259379714461572;
    rotMatrix13.Xy = -0.86444009816266154;
    rotMatrix13.Xz = 0.011949550630954842;
    rotMatrix13.Yx = 0.15956037294052439;
    rotMatrix13.Yy = 0.10633689077747174;
    rotMatrix13.Yz = 0.98144431989128211;
    rotMatrix13.Zx = -0.84967050228829077;
    rotMatrix13.Zy = -0.49136115266502928;
    rotMatrix13.Zz = 0.19137464615997574;
    NXOpen.Point3d translation13 = new NXOpen.Point3d(-4090.1464101543429, -232.11339011076274, 15226.705683186952);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix13, translation13, 0.036286553801305611);
    
    NXOpen.Matrix3x3 rotMatrix14 = new NXOpen.Matrix3x3();
    rotMatrix14.Xx = 0.35515614331541195;
    rotMatrix14.Xy = -0.93466088145592863;
    rotMatrix14.Xz = 0.016527266602354585;
    rotMatrix14.Yx = 0.16731404668970667;
    rotMatrix14.Yy = 0.080951162120926651;
    rotMatrix14.Yz = 0.98257463794440969;
    rotMatrix14.Zx = -0.9197119786355058;
    rotMatrix14.Zy = -0.34620217507591561;
    rotMatrix14.Zz = 0.18513219689472485;
    NXOpen.Point3d translation14 = new NXOpen.Point3d(-3586.6904810880196, 212.18972960724972, 15572.599372956127);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix14, translation14, 0.03450810014743777);
    
    NXOpen.Session.UndoMarkId markId14;
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Selection Recipe");
    
    theSession.DeleteUndoMark(markId14, null);
    
    NXOpen.Session.UndoMarkId markId15;
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Selection Recipe");
    
    NXOpen.CAE.CaeSetGroupFilterType[] entitytypes1 = new NXOpen.CAE.CaeSetGroupFilterType[2];
    entitytypes1[0] = NXOpen.CAE.CaeSetGroupFilterType.GeomFace;
    entitytypes1[1] = NXOpen.CAE.CaeSetGroupFilterType.GeomBody;
    NXOpen.TaggedObject nullNXOpen_TaggedObject = null;
    NXOpen.CAE.SelRecipeBoundingVolumeStrategy selRecipeBoundingVolumeStrategy1;
    selRecipeBoundingVolumeStrategy1 = selRecipeBuilder1.AddBoxBoundingVolumeStrategy(cartesianCoordinateSystem2, expression1, expression2, expression3, entitytypes1, NXOpen.CAE.SelRecipeBuilder.InputFilterType.EntireModel, nullNXOpen_TaggedObject);
    
    NXOpen.CAE.BoundingVolumePrimitive boundingVolumePrimitive1;
    boundingVolumePrimitive1 = selRecipeBoundingVolumeStrategy1.BoundingVolume;
    
    NXOpen.CAE.BoxBoundingVolume boxBoundingVolume1 = ((NXOpen.CAE.BoxBoundingVolume)boundingVolumePrimitive1);
    boxBoundingVolume1.Containment = NXOpen.CAE.CaeBoundingVolumePrimitiveContainment.Inside;
    
    selRecipeBuilder1.RecipeName = "SelectionRecipe";
    
    selRecipeBuilder1.SetAllowOccurrence(true);
    
    string[] description1 = new string[1];
    description1[0] = "";
    selRecipeBuilder1.SetDescription(description1);
    
    NXOpen.NXObject nXObject1;
    nXObject1 = selRecipeBuilder1.Commit();
    
    theSession.DeleteUndoMark(markId15, null);
    
    theSession.SetUndoMarkName(markId1, "Create Selection Recipe");
    
    NXOpen.CAE.SelectionRecipe selectionRecipe1 = ((NXOpen.CAE.SelectionRecipe)nXObject1);
    selectionRecipe1.Display.Update();
    
    selRecipeBuilder1.Destroy();
    
    workSimPart.Points.DeletePoint(point19);
    
    workSimPart.Points.DeletePoint(point20);
    
    workSimPart.Points.DeletePoint(point21);
    
    NXOpen.Matrix3x3 rotMatrix15 = new NXOpen.Matrix3x3();
    rotMatrix15.Xx = -0.58019968252762055;
    rotMatrix15.Xy = -0.81311767313990468;
    rotMatrix15.Xz = 0.046989126640030784;
    rotMatrix15.Yx = 0.18471650573856591;
    rotMatrix15.Yy = -0.075176363498269214;
    rotMatrix15.Yz = 0.97991240775842547;
    rotMatrix15.Zx = -0.7932516252126971;
    rotMatrix15.Zy = 0.57722453516696748;
    rotMatrix15.Zz = 0.19381355757194946;
    NXOpen.Point3d translation15 = new NXOpen.Point3d(1376.2207681838881, 139.26311820466984, 14635.074566773259);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix15, translation15, 0.035294296079381976);
    
    NXOpen.Session.UndoMarkId markId16;
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Show Selection Recipe Contents Only");
    
    NXOpen.CAE.BoundingVolumeSelectionRecipe boundingVolumeSelectionRecipe1 = ((NXOpen.CAE.BoundingVolumeSelectionRecipe)selectionRecipe1);
    boundingVolumeSelectionRecipe1.ShowContentsOnly();
    
    NXOpen.Matrix3x3 rotMatrix16 = new NXOpen.Matrix3x3();
    rotMatrix16.Xx = -0.4643900766871461;
    rotMatrix16.Xy = -0.88540764439889785;
    rotMatrix16.Xz = 0.019878629593041708;
    rotMatrix16.Yx = 0.18420403342175531;
    rotMatrix16.Yy = -0.074610189087356726;
    rotMatrix16.Yz = 0.98005213828423909;
    rotMatrix16.Zx = -0.86626250683361861;
    rotMatrix16.Zy = 0.45878821140515447;
    rotMatrix16.Zz = 0.19774389075264853;
    NXOpen.Point3d translation16 = new NXOpen.Point3d(833.31772461101264, 141.54239258326655, 15059.347136758775);
    workSimPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix16, translation16, 0.035269840414231521);
    
    // ----------------------------------------------
    //   Menu: Edit->Show and Hide->Show All
    // ----------------------------------------------
    NXOpen.Session.UndoMarkId markId17;
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Show");
    
    NXOpen.DisplayableObject[] objects1 = new NXOpen.DisplayableObject[38];
    NXOpen.Assemblies.Component component1 = ((NXOpen.Assemblies.Component)workSimPart.ComponentAssembly.RootComponent.FindObject("COMPONENT DemoBoxBeam_fem1 1"));
    NXOpen.Point point22 = ((NXOpen.Point)component1.FindObject("PROTO#.Points|HANDLE R-479027"));
    objects1[0] = point22;
    NXOpen.Point point23 = ((NXOpen.Point)component1.FindObject("PROTO#.Points|HANDLE R-479015"));
    objects1[1] = point23;
    NXOpen.CAE.CAEFace cAEFace1 = ((NXOpen.CAE.CAEFace)component1.FindObject("PROTO#CAE_Body(3)|CAE_Face(3)"));
    objects1[2] = cAEFace1;
    NXOpen.CAE.CAEFace cAEFace2 = ((NXOpen.CAE.CAEFace)component1.FindObject("PROTO#CAE_Body(2)|CAE_Face(2)"));
    objects1[3] = cAEFace2;
    NXOpen.CAE.CAEFace cAEFace3 = ((NXOpen.CAE.CAEFace)component1.FindObject("PROTO#CAE_Body(1)|CAE_Face(1)"));
    objects1[4] = cAEFace3;
    NXOpen.CAE.CAEBody cAEBody1 = ((NXOpen.CAE.CAEBody)component1.FindObject("PROTO#CAE_Body(3)"));
    objects1[5] = cAEBody1;
    NXOpen.CAE.CAEBody cAEBody2 = ((NXOpen.CAE.CAEBody)component1.FindObject("PROTO#CAE_Body(2)"));
    objects1[6] = cAEBody2;
    NXOpen.CAE.CAEBody cAEBody3 = ((NXOpen.CAE.CAEBody)component1.FindObject("PROTO#CAE_Body(1)"));
    objects1[7] = cAEBody3;
    NXOpen.CAE.CAEVertex cAEVertex1 = ((NXOpen.CAE.CAEVertex)component1.FindObject("PROTO#CAE_Body(3)|CAE_Vertex(13)"));
    objects1[8] = cAEVertex1;
    NXOpen.CAE.CAEVertex cAEVertex2 = ((NXOpen.CAE.CAEVertex)component1.FindObject("PROTO#CAE_Body(2)|CAE_Vertex(9)"));
    objects1[9] = cAEVertex2;
    NXOpen.CAE.CAEVertex cAEVertex3 = ((NXOpen.CAE.CAEVertex)component1.FindObject("PROTO#CAE_Body(1)|CAE_Vertex(5)"));
    objects1[10] = cAEVertex3;
    NXOpen.DisplayableObject displayableObject1 = ((NXOpen.DisplayableObject)component1.FindObject("PROTO#HANDLE R-445298"));
    objects1[11] = displayableObject1;
    NXOpen.CAE.CAEVertex cAEVertex4 = ((NXOpen.CAE.CAEVertex)component1.FindObject("PROTO#CAE_Body(1)|CAE_Vertex(14)"));
    objects1[12] = cAEVertex4;
    NXOpen.CAE.CAEVertex cAEVertex5 = ((NXOpen.CAE.CAEVertex)component1.FindObject("PROTO#CAE_Body(2)|CAE_Vertex(11)"));
    objects1[13] = cAEVertex5;
    NXOpen.CAE.CAEVertex cAEVertex6 = ((NXOpen.CAE.CAEVertex)component1.FindObject("PROTO#CAE_Body(1)|CAE_Vertex(8)"));
    objects1[14] = cAEVertex6;
    NXOpen.DisplayableObject displayableObject2 = ((NXOpen.DisplayableObject)component1.FindObject("PROTO#HANDLE R-445413"));
    objects1[15] = displayableObject2;
    NXOpen.DisplayableObject displayableObject3 = ((NXOpen.DisplayableObject)component1.FindObject("PROTO#HANDLE R-445409"));
    objects1[16] = displayableObject3;
    NXOpen.CAE.CAEVertex cAEVertex7 = ((NXOpen.CAE.CAEVertex)component1.FindObject("PROTO#CAE_Body(3)|CAE_Vertex(15)"));
    objects1[17] = cAEVertex7;
    NXOpen.CAE.CAEEdge cAEEdge1 = ((NXOpen.CAE.CAEEdge)component1.FindObject("PROTO#CAE_Body(3)|CAE_Edge(9)"));
    objects1[18] = cAEEdge1;
    NXOpen.CAE.CAEEdge cAEEdge2 = ((NXOpen.CAE.CAEEdge)component1.FindObject("PROTO#CAE_Body(2)|CAE_Edge(5)"));
    objects1[19] = cAEEdge2;
    NXOpen.DisplayableObject displayableObject4 = ((NXOpen.DisplayableObject)component1.FindObject("PROTO#HANDLE R-445519"));
    objects1[20] = displayableObject4;
    NXOpen.CAE.CAEVertex cAEVertex8 = ((NXOpen.CAE.CAEVertex)component1.FindObject("PROTO#CAE_Body(1)|CAE_Vertex(16)"));
    objects1[21] = cAEVertex8;
    NXOpen.CAE.CAEEdge cAEEdge3 = ((NXOpen.CAE.CAEEdge)component1.FindObject("PROTO#CAE_Body(3)|CAE_Edge(10)"));
    objects1[22] = cAEEdge3;
    NXOpen.CAE.CAEEdge cAEEdge4 = ((NXOpen.CAE.CAEEdge)component1.FindObject("PROTO#CAE_Body(2)|CAE_Edge(7)"));
    objects1[23] = cAEEdge4;
    NXOpen.CAE.CAEEdge cAEEdge5 = ((NXOpen.CAE.CAEEdge)component1.FindObject("PROTO#CAE_Body(1)|CAE_Edge(1)"));
    objects1[24] = cAEEdge5;
    NXOpen.DisplayableObject displayableObject5 = ((NXOpen.DisplayableObject)component1.FindObject("PROTO#HANDLE R-445629"));
    objects1[25] = displayableObject5;
    NXOpen.CAE.CAEEdge cAEEdge6 = ((NXOpen.CAE.CAEEdge)component1.FindObject("PROTO#CAE_Body(3)|CAE_Edge(12)"));
    objects1[26] = cAEEdge6;
    NXOpen.CAE.CAEEdge cAEEdge7 = ((NXOpen.CAE.CAEEdge)component1.FindObject("PROTO#CAE_Body(2)|CAE_Edge(8)"));
    objects1[27] = cAEEdge7;
    NXOpen.CAE.CAEEdge cAEEdge8 = ((NXOpen.CAE.CAEEdge)component1.FindObject("PROTO#CAE_Body(1)|CAE_Edge(4)"));
    objects1[28] = cAEEdge8;
    NXOpen.CAE.SimSimulation simSimulation1 = ((NXOpen.CAE.SimSimulation)workSimPart.FindObject("Simulation"));
    NXOpen.CAE.SimLoad simLoad1 = ((NXOpen.CAE.SimLoad)simSimulation1.Loads.FindObject("Load[fx_compression]"));
    objects1[29] = simLoad1;
    NXOpen.CAE.SimConstraint simConstraint1 = ((NXOpen.CAE.SimConstraint)simSimulation1.Constraints.FindObject("Constraint[FixedStart]"));
    objects1[30] = simConstraint1;
    NXOpen.CAE.SimConstraint simConstraint2 = ((NXOpen.CAE.SimConstraint)simSimulation1.Constraints.FindObject("Constraint[PinnedEnd]"));
    objects1[31] = simConstraint2;
    NXOpen.DisplayableObject displayableObject6 = ((NXOpen.DisplayableObject)workSimPart.FindObject("HANDLE R-120"));
    objects1[32] = displayableObject6;
    objects1[33] = boundingVolumeSelectionRecipe1;
    objects1[34] = component1;
    NXOpen.CAE.FEModelOccurrence fEModelOccurrence1 = ((NXOpen.CAE.FEModelOccurrence)workSimPart.FindObject("FEModelOccurrence[4]"));
    NXOpen.CAE.MeshManagerOccurrence meshManagerOccurrence1 = ((NXOpen.CAE.MeshManagerOccurrence)fEModelOccurrence1.Find("MeshManagerOccurrence"));
    NXOpen.CAE.Mesh2dFree mesh2dFree1 = ((NXOpen.CAE.Mesh2dFree)meshManagerOccurrence1.FindObject("MeshOccurrence[2d_mesh(1)]"));
    objects1[35] = mesh2dFree1;
    NXOpen.CAE.Mesh mesh1 = ((NXOpen.CAE.Mesh)meshManagerOccurrence1.FindObject("MeshOccurrence[connection_recipe_1_mesh]"));
    objects1[36] = mesh1;
    NXOpen.CAE.Mesh mesh2 = ((NXOpen.CAE.Mesh)meshManagerOccurrence1.FindObject("MeshOccurrence[connection_recipe_2_mesh]"));
    objects1[37] = mesh2;
    theSession.DisplayManager.UnblankObjects(objects1);
    
    workSimPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.ShowOnly);
    
    // ----------------------------------------------
    //   Menu: Tools->Automation->Journal->Stop Recording
    // ----------------------------------------------
    
  }
  public static int GetUnloadOption(string dummy) { return (int)NXOpen.Session.LibraryUnloadOption.Immediately; }
}
