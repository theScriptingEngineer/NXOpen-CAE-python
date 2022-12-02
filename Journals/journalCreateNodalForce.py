# Simcenter 3D 2023
# Journal created by Frederik on Thu Aug 25 08:01:47 2022 W. Europe Daylight Time
#
import math
import DSEDesignWorkflow
import DSEPlatform
import Join
import MoldCooling
import NXOpen
import NXOpen.CAE
import NXOpen.Fields
import SafetyOpen
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    simPart1 = workSimPart
    simSimulation1 = simPart1.Simulation
    
    simBCBuilder1 = simSimulation1.CreateBcBuilderForLoadDescriptor("magnitudeDirectionForce", "Force(1)", 37)
    
    propertyTable1 = simBCBuilder1.PropertyTable
    
    setManager1 = simBCBuilder1.TargetSetManager
    
    setManager2 = propertyTable1.GetSetManagerPropertyValue("DirectionNode1")
    
    setManager3 = propertyTable1.GetSetManagerPropertyValue("DirectionNode2")
    
    setManager4 = propertyTable1.GetSetManagerPropertyValue("DirectionNode3")
    
    setManager5 = propertyTable1.GetSetManagerPropertyValue("DirectionNode4")
    
    theSession.SetUndoMarkName(markId1, "Force Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Force
    # ----------------------------------------------
    simBCBuilder1.Destroy()
    
    theSession.UndoToMark(markId1, None)
    
    theSession.DeleteUndoMark(markId1, None)
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    simPart2 = workSimPart
    simSimulation2 = simPart2.Simulation
    
    simBCBuilder2 = simSimulation2.CreateBcBuilderForLoadDescriptor("ComponentForceField", "Force(1)", 37)
    
    propertyTable2 = simBCBuilder2.PropertyTable
    
    setManager6 = simBCBuilder2.TargetSetManager
    
    theSession.SetUndoMarkName(markId2, "Force Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Force
    # ----------------------------------------------
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Force")
    
    theSession.DeleteUndoMark(markId3, None)
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Force")
    
    objects1 = [None] * 1 
    objects1[0] = NXOpen.CAE.SetObject()
    fEModelOccurrence1 = workSimPart.FindObject("FEModelOccurrence[2]")
    fENode1 = fEModelOccurrence1.Find("Node[1459]")
    objects1[0].Obj = fENode1
    objects1[0].SubType = NXOpen.CAE.CaeSetObjectSubType.NotSet
    objects1[0].SubId = 0
    setManager6.SetTargetSetMembers(0, NXOpen.CAE.CaeSetGroupFilterType.Node, objects1)
    
    simBCBuilder2.BcName = "ourForce"
    
    vectorFieldWrapper1 = propertyTable2.GetVectorFieldWrapperPropertyValue("CartesianMagnitude")
    
    unit1 = workSimPart.UnitCollection.FindObject("Newton")
    expression1 = workSimPart.Expressions.CreateSystemExpressionWithUnits("123", unit1)
    
    expression2 = workSimPart.Expressions.CreateSystemExpressionWithUnits("456", unit1)
    
    expression3 = workSimPart.Expressions.CreateSystemExpressionWithUnits("789", unit1)
    
    fieldManager1 = workSimPart.FindObject("FieldManager")
    expressions1 = [NXOpen.Expression.Null] * 3 
    expressions1[0] = expression1
    expressions1[1] = expression2
    expressions1[2] = expression3
    vectorFieldWrapper2 = fieldManager1.CreateVectorFieldWrapperWithExpressions(expressions1)
    
    propertyTable2.SetVectorFieldWrapperPropertyValue("CartesianMagnitude", vectorFieldWrapper2)
    
    propertyTable2.SetTablePropertyWithoutValue("CylindricalMagnitude")
    
    propertyTable2.SetVectorFieldWrapperPropertyValue("CylindricalMagnitude", NXOpen.Fields.VectorFieldWrapper.Null)
    
    propertyTable2.SetTablePropertyWithoutValue("SphericalMagnitude")
    
    propertyTable2.SetVectorFieldWrapperPropertyValue("SphericalMagnitude", NXOpen.Fields.VectorFieldWrapper.Null)
    
    propertyTable2.SetTablePropertyWithoutValue("DistributionField")
    
    propertyTable2.SetScalarFieldWrapperPropertyValue("DistributionField", NXOpen.Fields.ScalarFieldWrapper.Null)
    
    propertyTable2.SetTablePropertyWithoutValue("ComponentsDistributionField")
    
    propertyTable2.SetVectorFieldWrapperPropertyValue("ComponentsDistributionField", NXOpen.Fields.VectorFieldWrapper.Null)
    
    propertyValue1 = [None] * 1 
    propertyValue1[0] = ""
    propertyTable2.SetTextPropertyValue("description", propertyValue1)
    
    simBCBuilder2.DestinationFolder = NXOpen.CAE.SimLbcFolder.Null
    
    simBC1 = simBCBuilder2.CommitAddBc()
    
    simBCBuilder2.Destroy()
    
    theSession.DeleteUndoMark(markId4, None)
    
    theSession.SetUndoMarkName(markId2, "Force")
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()