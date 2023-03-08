# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# NXOpen Python Reference Guide:
# https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_python_ref/index.html

# This file is used to demonstrate a working intellisense (code completion) for 
# writing NXOpen journals using Python

import sys
import math
import NXOpen
import NXOpen.CAE
from typing import List, cast, Optional, Union

the_session: NXOpen.Session = NXOpen.Session.GetSession()
the_uf_session: NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()
base_part = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow


def create_node(label: int, x_coordinate: float, y_coordinate: float, z_coordinate: float) -> Optional[NXOpen.CAE.FENode]:
    """This function creates a node with given label and coordinates.
       It is the user responsibility to make sure the label does not already exists in the model!
    
    Parameters
    ----------
    label: int
        The node label
    x_coordinate: float
        The global x-coordinate of the node to be created
    y_coordinate: float
        The global y-coordinate of the node to be created
    z_coordinate: float
        The global z-coordinate of the node to be created

    Returns
    -------
    NXOpen.CAE.FENode
        Returns the created node.
    """

    if not isinstance(NXOpen.CAE.BaseFemPart, base_part):
        the_lw.WriteFullline("create_node needs to start from a .fem or .afem file. Exiting")
        return
    
    base_fem_part: NXOpen.CAE.BaseFemPart = cast(NXOpen.CAE.BaseFemPart, base_part)
    base_fe_model: NXOpen.CAE.FEModel = base_fem_part.BaseFEModel
    node_create_builder: NXOpen.CAE.NodeCreateBuilder = base_fe_model.NodeElementMgr.CreateNodeCreateBuilder()

    node_create_builder.Label = label
    null_nxopen_coordinate_system: NXOpen.CoordinateSystem = None
    node_create_builder.Csys = null_nxopen_coordinate_system
    node_create_builder.SingleOption = True

    node_create_builder.X.Value = x_coordinate
    node_create_builder.Y.Value = y_coordinate
    node_create_builder.Z.Value = z_coordinate

    coordinates: NXOpen.Point3d = NXOpen.Point3d(x_coordinate, y_coordinate, z_coordinate)
    point: NXOpen.Point = base_fem_part.Points.CreatePoint(coordinates)
    node_create_builder.Point = point

    node: NXOpen.NXObject = node_create_builder.Commit()

    node_create_builder.Csys = null_nxopen_coordinate_system
    node_create_builder.DispCsys = null_nxopen_coordinate_system

    node_create_builder.Destroy()

    return cast(NXOpen.CAE.FENode, node)


def main():
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)

    for i in range(1000):
        create_node(10000 + i, 0, 0, i)


if __name__ == '__main__':
    main()
