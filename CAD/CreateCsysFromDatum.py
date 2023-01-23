# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# Untested

import sys
import math
import NXOpen
import NXOpen.CAE

theSession: NXOpen.Session = NXOpen.Session.GetSession()
basePart = theSession.Parts.BaseWork
theLW: NXOpen.ListingWindow = theSession.ListingWindow


def create_csys_from_datum(datum_plane: NXOpen.DatumPlane) -> NXOpen.CartesianCoordinateSystem:
    """This function creates a Cartesion coordinates system using a datumPlane as input.
    The orthogonal vectors are constructed in the plane to define the coordinate system, using basic geometry.

    Parameters
    ----------
    datum_plane: NXOpen.DatumPlane
        Instance of the datumPlane to create the coordinate system for.

    Returns
    -------
    NXOpen.CartesianCoordinateSystem
        A coordinate system which has the same origin as the plane with x and y axis in the plane.
    """
    origin: NXOpen.Point3d = datum_plane.Origin
    normal: NXOpen.Vector3d = datum_plane.Normal

    # we choose the global X vector to project on the plane.
    global_vector: NXOpen.Vector3d = NXOpen.Vector3d(1,0,0)
    projection: float = abs(normal.X * global_vector.X + normal.Y * global_vector.Y * normal.Z * global_vector.Z)
    # need to change that choice if global X is normal to the plane
    if (projection >= 0.999):
        global_vector.X = 0
        global_vector.Y = 1
        global_vector.Z = 0

    # we first project the global onto the plane normal
    # then subtract to get the component of global IN the plane which will be are local axis in the recipe definition
    projection_magnitude: float = global_vector.X * normal.X + global_vector.Y * normal.Y + global_vector.Z * normal.Z
    global_on_normal = NXOpen.Vector3d(projection_magnitude * normal.X, projection_magnitude * normal.Y, projection_magnitude * normal.Z)
    global_on_plane = NXOpen.Vector3d(global_vector.X - global_on_normal.X, global_vector.Y - global_on_normal.Y, global_vector.Z - global_on_normal.Z)

    # normalize
    magnitude: float = math.sqrt(global_on_plane.X ** 2 + global_on_plane.Y ** 2 + global_on_plane.Z ** 2)
    global_on_plane = NXOpen.Vector3d(global_on_plane.X / magnitude, global_on_plane.Y / magnitude, global_on_plane.Z / magnitude)

    # cross product of globalOnPlane and normal give vector in plane, otrhogonal to globalOnPlane
    global_on_plane_normal = NXOpen.Vector3d(
                                            normal.Y * global_on_plane.Z - normal.Z * global_on_plane.Y,
                                            -normal.X * global_on_plane.Z + normal.Z * global_on_plane.X,
                                            normal.X * global_on_plane.Y - normal.Y * global_on_plane.X)

    # normalize
    magnitude: float = math.sqrt(global_on_plane_normal.X ** 2 + global_on_plane_normal.Y ** 2 + global_on_plane_normal.Z ** 2)
    global_on_plane_normal = NXOpen.Vector3d(global_on_plane_normal.X / magnitude, global_on_plane_normal.Y / magnitude, global_on_plane_normal.Z / magnitude)

    # Create the coordinate system with these vectors
    xform: NXOpen.Xform = basePart.Xforms.CreateXform(origin, global_on_plane, global_on_plane_normal, NXOpen.SmartObject.UpdateOption.AfterModeling, 1.0)
    coordinate_system: NXOpen.CartesianCoordinateSystem = basePart.CoordinateSystems.CreateCoordinateSystem(xform, NXOpen.SmartObject.UpdateOption.AfterModeling)

    return coordinate_system


def main():
    theLW.Open()
    theLW.WriteFullline("Starting Main() in " + theSession.ExecutingJournal)


if __name__ == '__main__':
    main()
