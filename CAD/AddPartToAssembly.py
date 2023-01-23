# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# Untested

import sys
import math
import NXOpen
import NXOpen.CAE
from typing import cast

theSession: NXOpen.Session = NXOpen.Session.GetSession()
basePart = theSession.Parts.BaseWork
theLW: NXOpen.ListingWindow = theSession.ListingWindow


def main():
    theLW.Open()
    theLW.WriteFullline("Starting Main() in " + theSession.ExecutingJournal)

    # full path of the part to add as a component
    file_name = "LocationWithFullPath"
    # The name of the reference set used to represent the new component
    referenceset_name = "ReferenceSetName"
    # The name of the new component
    component_name = "ComponentName"
    # The layer to place the new component on:
    # -1 means use the original layers defined in the component.
    # 0 means use the work layer.
    # 1-256 means use the specified layer.
    layer: int = 1
    # Location of the new component
    base_point = NXOpen.Point3d(0, 0, 0)
    # Orientation of the new component
    orientation: NXOpen.Matrix3x3 = NXOpen.Matrix3x3()
    orientation.Xx = 1
    orientation.Xy = 0
    orientation.Xz = 0
    orientation.Yx = 0
    orientation.Yy = 1
    orientation.Yz = 0
    orientation.Zx = 0
    orientation.Zy = 0
    orientation.Zz = 1

    assembly: NXOpen.Part = cast(NXOpen.BasePart, basePart)  # explicit casting required in Visual Studio Code
    component_assembly: NXOpen.Assemblies.ComponentAssembly = assembly.ComponentAssembly
    loadstatus, component = component_assembly.AddComponent(file_name, referenceset_name, component_name, base_point, orientation, layer)


if __name__ == '__main__':
    main()
