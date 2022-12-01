# Simcenter 3D 2023
# Journal created by Frederik on Thu Aug 25 08:04:24 2022 W. Europe Daylight Time
#
import math
import DSEDesignWorkflow
import DSEPlatform
import Join
import MoldCooling
import NXOpen
import NXOpen.CAE
import SafetyOpen
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    theSession.SetUndoMarkName(markId2, "Solution Dialog")
    
    theSession.SetUndoMarkVisibility(markId2, None, NXOpen.Session.MarkVisibility.Invisible)
    
    theSession.SetUndoMarkName(markId2, "Solution")
    
    theSession.SetUndoMarkVisibility(markId2, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    simPart1 = workSimPart
    simSimulation1 = simPart1.Simulation
    
    simSolution1 = simSimulation1.CreateSolution("NX NASTRAN", "Structural", "SESTATIC 101 - Single Constraint", "Solution 1", NXOpen.CAE.SimSimulation.AxisymAbstractionType.NotSet)
    
    propertyTable1 = simSolution1.PropertyTable
    
    caePart1 = workSimPart
    modelingObjectPropertyTable1 = caePart1.ModelingObjectPropertyTables.CreateModelingObjectPropertyTable("Bulk Data Echo Request", "NX NASTRAN - Structural", "NX NASTRAN", "Bulk Data Echo Request1", 1)
    
    caePart2 = workSimPart
    modelingObjectPropertyTable2 = caePart2.ModelingObjectPropertyTables.CreateModelingObjectPropertyTable("Structural Output Requests", "NX NASTRAN - Structural", "NX NASTRAN", "Structural Output Requests1", 2)
    
    theSession.SetUndoMarkName(markId3, "Solution Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Solution
    # ----------------------------------------------
    # ----------------------------------------------
    #   Dialog Begin Solution
    # ----------------------------------------------
    # ----------------------------------------------
    #   Dialog Begin Solution
    # ----------------------------------------------
    # ----------------------------------------------
    #   Dialog Begin Solution
    # ----------------------------------------------
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    propertyTable2 = modelingObjectPropertyTable2.PropertyTable
    
    setManager1 = propertyTable2.GetSetManagerPropertyValue("Acceleration - Set")
    
    setManager2 = propertyTable2.GetSetManagerPropertyValue("Applied Load - Set")
    
    setManager3 = propertyTable2.GetSetManagerPropertyValue("Bolt Results - Set")
    
    setManager4 = propertyTable2.GetSetManagerPropertyValue("Gap Distance - Set")
    
    setManager5 = propertyTable2.GetSetManagerPropertyValue("Cohesive Element Results - Set")
    
    setManager6 = propertyTable2.GetSetManagerPropertyValue("Contact Result - Set")
    
    setManager7 = propertyTable2.GetSetManagerPropertyValue("Creep Strain - Set")
    
    setManager8 = propertyTable2.GetSetManagerPropertyValue("Cyclic Forces - Set")
    
    setManager9 = propertyTable2.GetSetManagerPropertyValue("Displacement - Set")
    
    setManager10 = propertyTable2.GetSetManagerPropertyValue("Elastic Strain - Set")
    
    setManager11 = propertyTable2.GetSetManagerPropertyValue("Energy Loss Per Cycle - Set")
    
    setManager12 = propertyTable2.GetSetManagerPropertyValue("Flexible Slider Result - Set")
    
    setManager13 = propertyTable2.GetSetManagerPropertyValue("Force - Set")
    
    setManager14 = propertyTable2.GetSetManagerPropertyValue("Gauss Point Creep Strain - Set")
    
    setManager15 = propertyTable2.GetSetManagerPropertyValue("Gauss Point Elastic Strain - Set")
    
    setManager16 = propertyTable2.GetSetManagerPropertyValue("Gauss Point Plastic Strain - Set")
    
    setManager17 = propertyTable2.GetSetManagerPropertyValue("Gauss Point Strain - Set")
    
    setManager18 = propertyTable2.GetSetManagerPropertyValue("Gauss Point Stress - Set")
    
    setManager19 = propertyTable2.GetSetManagerPropertyValue("Gauss Point Thermal Strain - Set")
    
    setManager20 = propertyTable2.GetSetManagerPropertyValue("Glue Result - Set")
    
    setManager21 = propertyTable2.GetSetManagerPropertyValue("Gpforce - Set")
    
    setManager22 = propertyTable2.GetSetManagerPropertyValue("Joint Result - Set")
    
    setManager23 = propertyTable2.GetSetManagerPropertyValue("Initial Strain - Set")
    
    setManager24 = propertyTable2.GetSetManagerPropertyValue("Kinetic Energy - Set")
    
    setManager25 = propertyTable2.GetSetManagerPropertyValue("Output Transformation Matrix Force - Set")
    
    setManager26 = propertyTable2.GetSetManagerPropertyValue("MPC Forces - Set")
    
    setManager27 = propertyTable2.GetSetManagerPropertyValue("Nonlinear Stress - Set")
    
    setManager28 = propertyTable2.GetSetManagerPropertyValue("Plastic Strain - Set")
    
    setManager29 = propertyTable2.GetSetManagerPropertyValue("Progressive Failure Results - Set")
    
    setManager30 = propertyTable2.GetSetManagerPropertyValue("SPC Forces - Set")
    
    setManager31 = propertyTable2.GetSetManagerPropertyValue("State Variable - Set")
    
    setManager32 = propertyTable2.GetSetManagerPropertyValue("Strain - Set")
    
    setManager33 = propertyTable2.GetSetManagerPropertyValue("Strain Energy - Set")
    
    setManager34 = propertyTable2.GetSetManagerPropertyValue("Stress - Set")
    
    setManager35 = propertyTable2.GetSetManagerPropertyValue("Thermal Strain - Set")
    
    setManager36 = propertyTable2.GetSetManagerPropertyValue("Temperature - Set")
    
    setManager37 = propertyTable2.GetSetManagerPropertyValue("Velocity - Set")
    
    theSession.SetUndoMarkName(markId4, "Structural Output Requests Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Structural Output Requests
    # ----------------------------------------------
    # ----------------------------------------------
    #   Dialog Begin Structural Output Requests
    # ----------------------------------------------
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Structural Output Requests")
    
    theSession.DeleteUndoMark(markId5, None)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Structural Output Requests")
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    propertyValue1 = []
    propertyTable2.SetScalarArrayPropertyValue("Acceleration - Frequencies", propertyValue1)
    
    propertyTable2.SetTablePropertyWithoutValue("Acceleration - Frequencies")
    
    setManager38 = propertyTable2.GetSetManagerPropertyValue("Acceleration - Set")
    
    setManager39 = propertyTable2.GetSetManagerPropertyValue("Applied Load - Set")
    
    setManager40 = propertyTable2.GetSetManagerPropertyValue("Bolt Results - Set")
    
    setManager41 = propertyTable2.GetSetManagerPropertyValue("Gap Distance - Set")
    
    setManager42 = propertyTable2.GetSetManagerPropertyValue("Cohesive Element Results - Set")
    
    setManager43 = propertyTable2.GetSetManagerPropertyValue("Contact Result - Set")
    
    setManager44 = propertyTable2.GetSetManagerPropertyValue("Creep Strain - Set")
    
    setManager45 = propertyTable2.GetSetManagerPropertyValue("Cyclic Forces - Set")
    
    propertyValue2 = []
    propertyTable2.SetScalarArrayPropertyValue("Displacement - Frequencies", propertyValue2)
    
    propertyTable2.SetTablePropertyWithoutValue("Displacement - Frequencies")
    
    setManager46 = propertyTable2.GetSetManagerPropertyValue("Displacement - Set")
    
    setManager47 = propertyTable2.GetSetManagerPropertyValue("Elastic Strain - Set")
    
    setManager48 = propertyTable2.GetSetManagerPropertyValue("Energy Loss Per Cycle - Set")
    
    propertyValue3 = []
    propertyTable2.SetScalarArrayPropertyValue("Equivalent Radiated Power - Frequencies", propertyValue3)
    
    propertyTable2.SetTablePropertyWithoutValue("Equivalent Radiated Power - Frequencies")
    
    setManager49 = propertyTable2.GetSetManagerPropertyValue("Flexible Slider Result - Set")
    
    setManager50 = propertyTable2.GetSetManagerPropertyValue("Force - Set")
    
    setManager51 = propertyTable2.GetSetManagerPropertyValue("Gauss Point Creep Strain - Set")
    
    setManager52 = propertyTable2.GetSetManagerPropertyValue("Gauss Point Elastic Strain - Set")
    
    setManager53 = propertyTable2.GetSetManagerPropertyValue("Gauss Point Plastic Strain - Set")
    
    setManager54 = propertyTable2.GetSetManagerPropertyValue("Gauss Point Strain - Set")
    
    setManager55 = propertyTable2.GetSetManagerPropertyValue("Gauss Point Stress - Set")
    
    setManager56 = propertyTable2.GetSetManagerPropertyValue("Gauss Point Thermal Strain - Set")
    
    setManager57 = propertyTable2.GetSetManagerPropertyValue("Glue Result - Set")
    
    setManager58 = propertyTable2.GetSetManagerPropertyValue("Gpforce - Set")
    
    setManager59 = propertyTable2.GetSetManagerPropertyValue("Joint Result - Set")
    
    setManager60 = propertyTable2.GetSetManagerPropertyValue("Initial Strain - Set")
    
    setManager61 = propertyTable2.GetSetManagerPropertyValue("Kinetic Energy - Set")
    
    setManager62 = propertyTable2.GetSetManagerPropertyValue("Output Transformation Matrix Force - Set")
    
    propertyValue4 = []
    propertyTable2.SetScalarArrayPropertyValue("Modal Contribution - Frequencies", propertyValue4)
    
    propertyTable2.SetTablePropertyWithoutValue("Modal Contribution - Frequencies")
    
    setManager63 = propertyTable2.GetSetManagerPropertyValue("MPC Forces - Set")
    
    setManager64 = propertyTable2.GetSetManagerPropertyValue("Nonlinear Stress - Set")
    
    setManager65 = propertyTable2.GetSetManagerPropertyValue("Plastic Strain - Set")
    
    setManager66 = propertyTable2.GetSetManagerPropertyValue("Progressive Failure Results - Set")
    
    setManager67 = propertyTable2.GetSetManagerPropertyValue("SPC Forces - Set")
    
    setManager68 = propertyTable2.GetSetManagerPropertyValue("State Variable - Set")
    
    setManager69 = propertyTable2.GetSetManagerPropertyValue("Strain - Set")
    
    setManager70 = propertyTable2.GetSetManagerPropertyValue("Strain Energy - Set")
    
    propertyTable2.SetIntegerPropertyValue("Stress - Location", 1)
    
    setManager71 = propertyTable2.GetSetManagerPropertyValue("Stress - Set")
    
    setManager72 = propertyTable2.GetSetManagerPropertyValue("Thermal Strain - Set")
    
    setManager73 = propertyTable2.GetSetManagerPropertyValue("Temperature - Set")
    
    propertyValue5 = []
    propertyTable2.SetScalarArrayPropertyValue("Velocity - Frequencies", propertyValue5)
    
    propertyTable2.SetTablePropertyWithoutValue("Velocity - Frequencies")
    
    setManager74 = propertyTable2.GetSetManagerPropertyValue("Velocity - Set")
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId7)
    
    theSession.DeleteUndoMark(markId7, None)
    
    theSession.DeleteUndoMark(markId6, None)
    
    theSession.SetUndoMarkName(markId4, "Structural Output Requests")
    
    theSession.DeleteUndoMark(markId4, None)
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution")
    
    theSession.DeleteUndoMark(markId8, None)
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution")
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    propertyTable3 = simSolution1.PropertyTable
    
    propertyTable3.SetNamedPropertyTablePropertyValue("Bulk Data Echo Request", modelingObjectPropertyTable1)
    
    propertyTable3.SetNamedPropertyTablePropertyValue("Output Requests", modelingObjectPropertyTable2)
    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs2 = theSession.UpdateManager.DoUpdate(id1)
    
    simSolutionStep1 = simSolution1.CreateStep(0, True, "Subcase - Statics 1")
    
    nErrs3 = theSession.UpdateManager.DoUpdate(markId10)
    
    theSession.DeleteUndoMark(markId10, None)
    
    theSession.DeleteUndoMark(markId9, None)
    
    theSession.SetUndoMarkName(markId3, "Solution")
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.DeleteUndoMark(id1, None)
    
    theSession.SetUndoMarkVisibility(markId1, None, NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()