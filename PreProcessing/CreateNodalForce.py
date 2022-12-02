# Simcenter 12.0.1.7
# Journal created by Frederik on Thu Aug  4 13:55:20 2022 W. Europe Daylight Time
#
# tested and working in version 2023 release SC2022.1
import math
import NXOpen
import NXOpen.CAE
import NXOpen.Fields
from typing import List, cast

theSession = NXOpen.Session.GetSession()
basePart: NXOpen.BasePart = theSession.Parts.BaseWork
theLW: NXOpen.ListingWindow = theSession.ListingWindow

def CreateNodalForce(nodeLabel, fx, fy, fz, forceName):
    # check if started from a SimPart, returning othwerwise
    if not isinstance(basePart, NXOpen.CAE.SimPart):
        theLW.WriteFullline("CreateNodalForce needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart) # explicit casting makes it clear
    
    simSimulation: NXOpen.CAE.SimSimulation = simPart.Simulation
    # make the active solution inactive, so load is not automatically added to active subcase
    simPart.Simulation.ActiveSolution = NXOpen.CAE.SimSolution.Null

    # check if a nodal force with that name already exists. If it does, update, if not create it
    simLoads: List[NXOpen.CAE.SimLoad] = simPart.Simulation.Loads
    simLoad = [item for item in simLoads if item.Name.lower() == forceName.lower()]
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
    fEModelOccurrence: NXOpen.CAE.FEModelOccurrence = simPart.Simulation.Femodel
    fENode: NXOpen.CAE.FENode = fEModelOccurrence.FenodeLabelMap.GetNode(nodeLabel)
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
    CreateNodalForce(1475, 100, 200, 300, "ourForce")
    
if __name__ == '__main__':
    main()