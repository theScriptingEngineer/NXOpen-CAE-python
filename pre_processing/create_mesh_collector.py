# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# NXOpen Python Reference Guide:
# https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_python_ref/index.html

import sys
import math
import NXOpen
import NXOpen.CAE
from typing import List, cast, Optional, Union

the_session: NXOpen.Session = NXOpen.Session.GetSession()
the_uf_session: NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()
base_part = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow


def create_2dmesh_collector(thickness: float, physical_property_label: int) -> Optional[NXOpen.CAE.MeshCollector]:
    """This function creates a 2d mesh collector with the given thickness and label.
       the color of the mesh collector is set as 10 times the label
    
    Parameters
    ----------
    thickness: float
        The thickness to set in the mesh collector
    physical_property_label: int
        The label of the physical property. Needs to be unique and thus cannot already be used in the part.


    Returns
    -------
    NXOpen.CAE.MeshCollector
        Returns the created 2d mesh collector.
    """

    if not isinstance(NXOpen.CAE.FemPart, base_part):
        the_lw.WriteFullline("create_node needs to start from a .fem file. Exiting")
        return
    
    fem_part: NXOpen.CAE.FemPart = cast(NXOpen.CAE.FemPart, base_part)
    fe_model: NXOpen.CAE.FEModel = fem_part.BaseFEModel
    
    mesh_manager: NXOpen.CAE.MeshManager = cast(NXOpen.CAE.MeshManager, fe_model.MeshManager)
    null_mesh_collector: NXOpen.CAE.MeshCollector = None
    mesh_collector_builder: NXOpen.CAE.MeshCollectorBuilder = mesh_manager.CreateCollectorBuilder(null_mesh_collector, "ThinShell")

    physical_property_table: NXOpen.CAE.PhysicalPropertyTable = fem_part.PhysicalPropertyTables.CreatePhysicalPropertyTable("PSHELL", "NX NASTRAN - Structural", "NX NASTRAN", "PSHELL2", physical_property_label)
    physical_property_table.SetName(str(thickness) + "mm")

    material_manager: NXOpen.CAE.MaterialManager = cast(NXOpen.CAE.MaterialManager, fem_part.MaterialManager) # cast only required because of intellisensse
    physical_materials: List[NXOpen.CAE.PhysicalMaterial] = material_manager.PhysicalMaterials.GetUsedMaterials()
    steel: List[NXOpen.CAE.PhysicalMaterial] = [item for item in physical_materials if item.Name == "Steel"]
    if steel == None:
        steel = material_manager.PhysicalMaterials.LoadFromNxlibrary("Steel")
    else:
        steel = steel[0]

    property_table: NXOpen.CAE.PropertyTable = physical_property_table.PropertyTable
    property_table.SetMaterialPropertyValue("material", False, steel)
    property_table.SetTablePropertyWithoutValue("bending material")
    property_table.SetTablePropertyWithoutValue("transverse shear material")
    property_table.SetTablePropertyWithoutValue("membrane-bending coupling material")

    unit_millimeter: NXOpen.Unit = cast(NXOpen.UnitCollection, fem_part.UnitCollection).FindObject("MilliMeter")
    property_table.SetBaseScalarWithDataPropertyValue("element thickness", str(thickness), unit_millimeter)

    mesh_collector_builder.CollectorName = str(thickness) + "mm"
    mesh_collector_builder.PropertyTable.SetNamedPropertyTablePropertyValue("Shell Property", physical_property_table)

    nx_object: NXOpen.NXObject = mesh_collector_builder.Commit()

    mesh_collector_builder.Destroy()

    # Setting the color of the MeshCollector we just created
    mesh_collector: NXOpen.CAE.MeshCollector = cast(NXOpen.CAE.MeshCollector, nx_object)
    mesh_collector_display_defaults = mesh_collector.GetMeshDisplayDefaults()

    # we set the color as label * 10 to make a distinction between the colors. The maximum color number is 216, therefore we take the modulus to not exceed this numer (eg. 15%4 -> 3)
    mesh_collector_display_defaults.Color = NXOpen.NXColor.NXColor._Get((label * 10) % 216)

    mesh_collector_display_defaults.Dispose()


def main():
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)

    thicknesses: List[float] = [6, 8, 10, 12, 14, 15, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100]
    for i in range(len(thicknesses)):
        create_2dmesh_collector(thicknesses[i], i + 1)


if __name__ == '__main__':
    main()
