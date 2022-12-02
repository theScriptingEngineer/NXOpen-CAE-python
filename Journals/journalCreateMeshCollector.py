# Simcenter 3D 2023
# Journal created by Frederik on Thu Aug 25 08:12:28 2022 W. Europe Daylight Time
#
import math
import DSEDesignWorkflow
import DSEPlatform
import Join
import MoldCooling
import NXOpen
import NXOpen.CAE
import NXOpen.PhysMat
import SafetyOpen
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    fEModel1 = workFemPart.FindObject("FEModel")
    meshManager1 = fEModel1.Find("MeshManager")
    meshCollectorBuilder1 = meshManager1.CreateCollectorBuilder(NXOpen.CAE.MeshCollector.Null, "Solid")
    
    meshCollectorBuilder1.CollectorName = "Solid(1)"
    
    meshCollectorBuilder1.CollectorName = "inherited"
    
    theSession.SetUndoMarkName(markId1, "Mesh Collector Dialog")
    
    meshCollectorBuilder1.CollectorName = "Solid(1)"
    
    meshCollectorBuilder1.Destroy()
    
    theSession.UndoToMark(markId1, None)
    
    theSession.DeleteUndoMark(markId1, None)
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    meshCollectorBuilder2 = meshManager1.CreateCollectorBuilder(NXOpen.CAE.MeshCollector.Null, "ThinShell")
    
    meshCollectorBuilder2.CollectorName = "Thin Shell(1)"
    
    theSession.SetUndoMarkName(markId2, "Mesh Collector Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Mesh Collector
    # ----------------------------------------------
    caePart1 = workFemPart
    physicalPropertyTable1 = caePart1.PhysicalPropertyTables.CreatePhysicalPropertyTable("PSHELL", "NX NASTRAN - Structural", "NX NASTRAN", "PSHELL1", 26)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    propertyTable1 = physicalPropertyTable1.PropertyTable
    
    theSession.SetUndoMarkName(markId3, "PSHELL Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin PSHELL
    # ----------------------------------------------
    physicalMaterialListBuilder1 = workFemPart.MaterialManager.PhysicalMaterials.CreateListBlockBuilder()
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    theSession.SetUndoMarkName(markId4, "Material List Dialog")
    
    id1 = theSession.GetNewestUndoMark(NXOpen.Session.MarkVisibility.AnyVisibility)
    
    theSession.DeleteUndoMark(id1, None)
    
    # ----------------------------------------------
    #   Dialog Begin Material List
    # ----------------------------------------------
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Material List")
    
    theSession.DeleteUndoMark(markId5, None)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Material List")
    
    physicalMaterial1 = workFemPart.MaterialManager.PhysicalMaterials.LoadFromNxmatmllibrary("Brass")
    
    theSession.DeleteUndoMark(markId6, None)
    
    theSession.DeleteUndoMark(id1, None)
    
    physicalMaterialListBuilder1.Destroy()
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "PSHELL")
    
    theSession.DeleteUndoMark(markId7, None)
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "PSHELL")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    physicalPropertyTable1.SetName("propertyName")
    
    propertyTable1.SetMaterialPropertyValue("material", False, physicalMaterial1)
    
    propertyTable1.SetTablePropertyWithoutValue("bending material")
    
    propertyTable1.SetTablePropertyWithoutValue("transverse shear material")
    
    propertyTable1.SetTablePropertyWithoutValue("membrane-bending coupling material")
    
    unit1 = workFemPart.UnitCollection.FindObject("MilliMeter")
    propertyTable1.SetBaseScalarWithDataPropertyValue("element thickness", "123", unit1)
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId9)
    
    theSession.DeleteUndoMark(markId9, None)
    
    theSession.DeleteUndoMark(markId8, None)
    
    theSession.SetUndoMarkName(markId3, "PSHELL")
    
    theSession.DeleteUndoMark(markId3, None)
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Mesh Collector")
    
    meshCollectorBuilder2.CollectorName = "collectorName"
    
    theSession.DeleteUndoMark(markId10, None)
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Mesh Collector")
    
    meshCollectorBuilder2.PropertyTable.SetNamedPropertyTablePropertyValue("Shell Property", physicalPropertyTable1)
    
    nXObject1 = meshCollectorBuilder2.Commit()
    
    theSession.DeleteUndoMark(markId11, None)
    
    theSession.SetUndoMarkName(markId2, "Mesh Collector")
    
    meshCollectorBuilder2.Destroy()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()