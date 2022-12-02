# Simcenter 3D 2023
# Journal created by Frederik on Thu Aug 25 08:02:57 2022 W. Europe Daylight Time
#
import math
import DSEDesignWorkflow
import DSEPlatform
import Join
import MoldCooling
import NXOpen
import NXOpen.Assemblies
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
    
    simBCBuilder1 = simSimulation1.CreateBcBuilderForConstraintDescriptor("UserDefinedDisplacementConstraint", "UserDefined(1)", 7)
    
    propertyTable1 = simBCBuilder1.PropertyTable
    
    setManager1 = simBCBuilder1.TargetSetManager
    
    fieldExpression1 = propertyTable1.GetScalarFieldPropertyValue("DOF1")
    
    fieldExpression2 = propertyTable1.GetScalarFieldPropertyValue("DOF2")
    
    fieldExpression3 = propertyTable1.GetScalarFieldPropertyValue("DOF3")
    
    fieldExpression4 = propertyTable1.GetScalarFieldPropertyValue("DOF4")
    
    fieldExpression5 = propertyTable1.GetScalarFieldPropertyValue("DOF5")
    
    fieldExpression6 = propertyTable1.GetScalarFieldPropertyValue("DOF6")
    
    theSession.SetUndoMarkName(markId1, "User Defined Constraint Dialog")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "User Defined Constraint")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "User Defined Constraint")
    
    objects1 = [None] * 1 
    objects1[0] = NXOpen.CAE.SetObject()
    component1 = workSimPart.ComponentAssembly.RootComponent.FindObject("COMPONENT hullModelNX12_fem1 1")
    cAEVertex1 = component1.FindObject("PROTO#CAE_Body(82)|CAE_Vertex(1278)")
    objects1[0].Obj = cAEVertex1
    objects1[0].SubType = NXOpen.CAE.CaeSetObjectSubType.NotSet
    objects1[0].SubId = 0
    setManager1.SetTargetSetMembers(0, NXOpen.CAE.CaeSetGroupFilterType.GeomVertex, objects1)
    
    simBCBuilder1.BcName = "myConstraint"
    
    unit1 = workSimPart.UnitCollection.FindObject("MilliMeter")
    indepVarArray1 = []
    fieldExpression1.EditFieldExpression("-777777", unit1, indepVarArray1, False)
    
    propertyTable1.SetScalarFieldPropertyValue("DOF1", fieldExpression1)
    
    indepVarArray2 = []
    fieldExpression2.EditFieldExpression("0", unit1, indepVarArray2, False)
    
    propertyTable1.SetScalarFieldPropertyValue("DOF2", fieldExpression2)
    
    indepVarArray3 = []
    fieldExpression3.EditFieldExpression("123", unit1, indepVarArray3, False)
    
    propertyTable1.SetScalarFieldPropertyValue("DOF3", fieldExpression3)
    
    unit2 = workSimPart.UnitCollection.FindObject("Degrees")
    indepVarArray4 = []
    fieldExpression4.EditFieldExpression("-777777", unit2, indepVarArray4, False)
    
    propertyTable1.SetScalarFieldPropertyValue("DOF4", fieldExpression4)
    
    indepVarArray5 = []
    fieldExpression5.EditFieldExpression("0", unit2, indepVarArray5, False)
    
    propertyTable1.SetScalarFieldPropertyValue("DOF5", fieldExpression5)
    
    indepVarArray6 = []
    fieldExpression6.EditFieldExpression("456", unit2, indepVarArray6, False)
    
    propertyTable1.SetScalarFieldPropertyValue("DOF6", fieldExpression6)
    
    propertyValue1 = [None] * 1 
    propertyValue1[0] = ""
    propertyTable1.SetTextPropertyValue("description", propertyValue1)
    
    simBCBuilder1.DestinationFolder = NXOpen.CAE.SimLbcFolder.Null
    
    simBC1 = simBCBuilder1.CommitAddBc()
    
    simBCBuilder1.Destroy()
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.SetUndoMarkName(markId1, "User Defined Constraint")
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()