# intellisense by theScriptingEngineer
import imp
import math
import NXOpen
import NXOpen.CAE
import NXOpen.Fields
from typing import List, cast
from multipledispatch import dispatch

theSession = NXOpen.Session.GetSession()
basePart: NXOpen.BasePart = theSession.Parts.BaseWork
theLW: NXOpen.ListingWindow = theSession.ListingWindow

def CreateConstraint(nodeLabel: int, dx: float, dy : float, dz: float, rx: float, ry: float, rz: float, constraintName: str):
    # check if started from a SimPart, returning othwerwise
    if not isinstance(basePart, NXOpen.CAE.SimPart):
        theLW.WriteFullline("CreateConstraint needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart) # explicit casting makes it clear
    
    simSimulation: NXOpen.CAE.SimSimulation = simPart.Simulation
    # make the active solution inactive, so bondary condition is not automatically added to active subcase
    simSimulation.ActiveSolution = NXOpen.CAE.SimSolution.Null

    # check if constaint already exists
    simConstraints: List[NXOpen.CAE.SimConstraint] = simSimulation.Constraints
    simConstraint: NXOpen.CAE.SimConstraint = [item for item in simConstraints if item.Name.lower() == constraintName.lower()]
    simBCBuilder: NXOpen.CAE.SimBCBuilder
    if len(simConstraint == 0):
        # no constraint with the given name, thus creating the constrain
        simBCBuilder = simSimulation.CreateBcBuilderForConstraintDescriptor("UserDefinedDisplacementConstraint", constraintName, 0)
    else:
        # a constraint with the given name already exists therefore editing the constraint
        simBCBuilder = simSimulation.CreateBcBuilderForBc(simConstraint)

    propertyTable: NXOpen.CAE.PropertyTable = simBCBuilder.PropertyTable
    fieldExpression1: NXOpen.Fields.FieldExpression = propertyTable.GetScalarFieldPropertyValue("DOF1")
    fieldExpression2: NXOpen.Fields.FieldExpression = propertyTable.GetScalarFieldPropertyValue("DOF2")
    fieldExpression3: NXOpen.Fields.FieldExpression = propertyTable.GetScalarFieldPropertyValue("DOF3")
    fieldExpression4: NXOpen.Fields.FieldExpression = propertyTable.GetScalarFieldPropertyValue("DOF4")
    fieldExpression5: NXOpen.Fields.FieldExpression = propertyTable.GetScalarFieldPropertyValue("DOF5")
    fieldExpression6: NXOpen.Fields.FieldExpression = propertyTable.GetScalarFieldPropertyValue("DOF6")
    
    unitMillimeter: NXOpen.Unit = cast(NXOpen.Unit, simPart.UnitCollection.FindObject("MilliMeter"))
    indepVarArray1: List[NXOpen.Fields.FieldVariable] = []
    fieldExpression1.EditFieldExpression(str(dx), unitMillimeter, indepVarArray1, False)
    propertyTable.SetScalarFieldPropertyValue("DOF1", fieldExpression1)

    indepVarArray2: List[NXOpen.Fields.FieldVariable] = []
    fieldExpression2.EditFieldExpression(str(dy), unitMillimeter, indepVarArray2, False)
    propertyTable.SetScalarFieldPropertyValue("DOF2", fieldExpression2)

    indepVarArray3: List[NXOpen.Fields.FieldVariable] = []
    fieldExpression3.EditFieldExpression(str(dz), unitMillimeter, indepVarArray3, False)
    propertyTable.SetScalarFieldPropertyValue("DOF3", fieldExpression3)

    unitDegrees: NXOpen.Unit = cast(NXOpen.Unit, simPart.UnitCollection.FindObject("Degrees"))
    indepVarArray4: List[NXOpen.Fields.FieldVariable] = []
    fieldExpression4.EditFieldExpression(str(rx), unitDegrees, indepVarArray4, False)
    propertyTable.SetScalarFieldPropertyValue("DOF4", fieldExpression4)

    indepVarArray5: List[NXOpen.Fields.FieldVariable] = []
    fieldExpression5.EditFieldExpression(str(ry), unitDegrees, indepVarArray5, False)
    propertyTable.SetScalarFieldPropertyValue("DOF5", fieldExpression5)

    indepVarArray6: List[NXOpen.Fields.FieldVariable] = []
    fieldExpression6.EditFieldExpression(str(rx), unitDegrees, indepVarArray6, False)
    propertyTable.SetScalarFieldPropertyValue("DOF6", fieldExpression6)

    # select the node via the label to assign the constraint to
    setManager: NXOpen.CAE.SetManager = simBCBuilder.TargetSetManager
    
    objects: List[NXOpen.CAE.SetObject] = [NXOpen.CAE.SetObject.Obj] * 1
    objects[0] = NXOpen.CAE.SetObject()
    fEModelOccurrence: NXOpen.CAE.FEModelOccurrence = simPart.Simulation.Femodel
    fENode: NXOpen.CAE.FENode = fEModelOccurrence.FenodeLabelMap.GetNode(nodeLabel)
    if fENode is None:
        theLW.WriteFullline("CreateConstraint: node with label " + str(nodeLabel) + " not found in the model. Constaint not created.")
        return

    objects[0].Obj = fENode
    objects[0].SubType = NXOpen.CAE.CaeSetObjectSubType.NotSet
    objects[0].SubId = 0
    setManager.SetTargetSetMembers(0, NXOpen.CAE.CaeSetGroupFilterType.Node, objects)
    
    simBC: NXOpen.CAE.SimBC = simBCBuilder.CommitAddBc()
    simBCBuilder.Destroy()
    
    return simBC

@dispatch(int, float, float, float)
def CreateNodalForce(nodeLabel: int, fx: float, fy : float, fz: float):
    defaultName: str = "Nodalforce_" + str(nodeLabel)
    CreateNodalForce(nodeLabel, fx, fy, fz, defaultName)

@dispatch(int, float, float, float, str)
def CreateNodalForce(nodeLabel: int, fx: float, fy: float, fz: float, forceName: str):
    # check if started from a SimPart, returning othwerwise
    if not isinstance(basePart, NXOpen.CAE.SimPart):
        theLW.WriteFullline("CreateNodalForce needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart) # explicit casting makes it clear
    
    simSimulation: NXOpen.CAE.SimSimulation = simPart.Simulation
    # make the active solution inactive, so load is not automatically added to active subcase
    simSimulation.ActiveSolution = NXOpen.CAE.SimSolution.Null

    # check if a nodal force with that name already exists. If it does, update, if not create it
    simLoads: List[NXOpen.CAE.SimLoad] = simPart.Simulation.Loads
    simLoad: NXOpen.CAE.SimLoad = [item for item in simLoads if item.Name.lower() == forceName.lower()]
    if len(simLoad) == 0:
        # load not found
        simBCBuilder: NXOpen.CAE.SimBCBuilder = simSimulation.CreateBcBuilderForLoadDescriptor("ComponentForceField", forceName, 0) # overloaded function is unknow to intellisense
    else:
        simBCBuilder: NXOpen.CAE.SimBCBuilder = simSimulation.CreateBcBuilderForBc(simLoad[0])
    
    # define the force
    propertyTable: NXOpen.CAE.PropertyTable = simBCBuilder.PropertyTable
    setManager: NXOpen.CAE.SetManager = simBCBuilder.TargetSetManager
    
    objects: List[NXOpen.CAE.SetObject] = [NXOpen.CAE.SetObject.Obj] * 1
    objects[0] = NXOpen.CAE.SetObject()
    fENode: NXOpen.CAE.FENode = simPart.Simulation.Femodel.FenodeLabelMap.GetNode(nodeLabel)
    if fENode is None:
        theLW.WriteFullline("CreateNodalForce: node with label " + str(nodeLabel) + " not found in the model. Force not created.")
        return

    objects[0].Obj = fENode
    objects[0].SubType = NXOpen.CAE.CaeSetObjectSubType.NotSet
    objects[0].SubId = 0
    setManager.SetTargetSetMembers(0, NXOpen.CAE.CaeSetGroupFilterType.Node, objects)
    
    unit1: NXOpen.Unit = simPart.UnitCollection.FindObject("Newton")
    expression1: NXOpen.Expression = simPart.Expressions.CreateSystemExpressionWithUnits(str(fx), unit1)
    expression2: NXOpen.Expression = simPart.Expressions.CreateSystemExpressionWithUnits(str(fy), unit1)
    expression3: NXOpen.Expression = simPart.Expressions.CreateSystemExpressionWithUnits(str(fz), unit1)

    fieldManager: NXOpen.Fields.FieldManager = cast(NXOpen.Fields.FieldManager, simPart.FindObject("FieldManager"))
    expressions: List[NXOpen.Expression] = [NXOpen.Expression.Null] * 3 
    expressions[0] = expression1
    expressions[1] = expression2
    expressions[2] = expression3
    vectorFieldWrapper: NXOpen.Fields.VectorFieldWrapper = fieldManager.CreateVectorFieldWrapperWithExpressions(expressions)
    
    propertyTable.SetVectorFieldWrapperPropertyValue("CartesianMagnitude", vectorFieldWrapper)
    propertyTable.SetTablePropertyWithoutValue("CylindricalMagnitude")
    propertyTable.SetVectorFieldWrapperPropertyValue("CylindricalMagnitude", NXOpen.Fields.VectorFieldWrapper.Null)
    propertyTable.SetTablePropertyWithoutValue("SphericalMagnitude")
    propertyTable.SetVectorFieldWrapperPropertyValue("SphericalMagnitude", NXOpen.Fields.VectorFieldWrapper.Null)
    propertyTable.SetTablePropertyWithoutValue("DistributionField")
    propertyTable.SetScalarFieldWrapperPropertyValue("DistributionField", NXOpen.Fields.ScalarFieldWrapper.Null)
    propertyTable.SetTablePropertyWithoutValue("ComponentsDistributionField")
    propertyTable.SetVectorFieldWrapperPropertyValue("ComponentsDistributionField", NXOpen.Fields.VectorFieldWrapper.Null)
    
    simBC1: NXOpen.CAE.SimBC = simBCBuilder.CommitAddBc()
    
    simBCBuilder.Destroy()

def main() :
    theLW.Open()
    theLW.WriteFullline("Starting Main() in " + theSession.ExecutingJournal)

    CreateNodalForce(1871, 0, 0, -9810, "DeckLoadPS1")
    CreateNodalForce(1948, 0, 0, -9810, "DeckLoadPS2")
    CreateNodalForce(1908, 0, 0, -9810, "DeckLoadPS3")

    CreateNodalForce(1870, 0, 0, -9810, "DeckLoadSB1")
    CreateNodalForce(1938, 0, 0, -9810, "DeckLoadSB2")
    CreateNodalForce(1907, 0, 0, -9810, "DeckLoadSB3")

    CreateNodalForce(1882, 0, 0, -9810, "DeckLoadCenter1")
    CreateNodalForce(1927, 0, 0, -9810, "DeckLoadCenter2")
    CreateNodalForce(1918, 0, 0, -9810, "DeckLoadCenter3")

    CreateNodalForce(3810, 0, 0, 9810, "BottomLoadPS1")
    CreateNodalForce(3692, 0, 0, 9810, "BottomLoadPS2")
    CreateNodalForce(3739, 0, 0, 9810, "BottomLoadPS3")

    CreateNodalForce(3649, 0, 0, 9810, "BottomLoadSB1")
    CreateNodalForce(3684, 0, 0, 9810, "BottomLoadSB2")
    CreateNodalForce(3710, 0, 0, 9810, "BottomLoadSB3")

    CreateNodalForce(3773, 0, 0, 9810, "BottomLoadCenter1")
    CreateNodalForce(3668, 0, 0, 9810, "BottomLoadCenter2")
    CreateNodalForce(3705, 0, 0, 9810, "BottomLoadCenter3")

    CreateConstraint(1969, 0, 0, 0, -777777, -777777, -777777, "XYZ_Fixed")
    CreateConstraint(2010, -777777, 0, 0, -777777, -777777, -777777, "YZ_Fixed")
    CreateConstraint(2012, -777777, -777777, 0, -777777, -777777, -777777, "Z_Fixed")
    
if __name__ == '__main__':
    main()
