# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# NXOpen Python Reference Guide:
# https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_python_ref/index.html

# example code for using NXOpen VectorArithmetic
# untested

import NXOpen
import NXOpen.CAE
from typing import List, cast, Optional, Union

the_session: NXOpen.Session = NXOpen.Session.GetSession()
the_uf_session: NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()
base_part = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow


def print_vector3(vector: NXOpen.VectorArithmetic.Vector3) -> str:
    """This function returns string representation of a NXOpen.VectorArithmetic.Vector3

    Parameters
    ----------
    vector: NXOpen.VectorArithmetic.Vector3
        The vector to represent as string

    Returns
    -------
    str
        A string representation of the vector3
    """
    return "(" + str(vector.x) + ", " + str(vector.y) + ", " + str(vector.z) + ")"

def main():
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)

    test: NXOpen.VectorArithmetic.Vector3 = NXOpen.VectorArithmetic.Vector3(1.0, 2.0, 3.0)
    sum: NXOpen.VectorArithmetic.Vector3 = test + test
    the_lw.WriteFullline(str(sum))

    global_x: NXOpen.VectorArithmetic.Vector3 = NXOpen.VectorArithmetic.Vector3(1.0, 0, 0)
    global_y: NXOpen.VectorArithmetic.Vector3 = NXOpen.VectorArithmetic.Vector3(0, 1.0, 0)
    global_z: NXOpen.VectorArithmetic.Vector3 = NXOpen.VectorArithmetic.Vector3(0, 0, 1.0)

    the_lw.WriteFullline("Some examples of vector arithmetic using NXOpen.VectorArithmetic:")
    the_lw.WriteFullline("Using the following vectors it the examples:")
    the_lw.WriteFullline("Test: " + print_vector3(test))
    the_lw.WriteFullline("global_x: " + print_vector3(global_x))
    the_lw.WriteFullline("global_y: " + print_vector3(global_y))
    the_lw.WriteFullline("global_z: " + print_vector3(global_z))
    the_lw.WriteFullline("")

    the_lw.WriteFullline("Test + global_x = " + print_vector3(test + global_x))
    the_lw.WriteFullline("Test - global_x = " + print_vector3(test - global_x))
    the_lw.WriteFullline("Test x 2 = " + print_vector3(test * 2))
    the_lw.WriteFullline("global_z x 2 = " + print_vector3(global_z * 2))
    the_lw.WriteFullline("Test - global_x - 2 x global_y - 3 x global_z = " + print_vector3(test - global_x - 2 * global_y - 3 * global_z))
    the_lw.WriteFullline("")

    the_lw.WriteFullline("Dot product of test and global_x = " + str(test.Dot(global_x)))
    the_lw.WriteFullline("Dot product of test and global_y = " + str(test.Dot(global_y)))
    the_lw.WriteFullline("Dot product of test and global_z = " + str(test.Dot(global_z)))
    the_lw.WriteFullline("")

    the_lw.WriteFullline("Cross product of test and global_x = " + print_vector3(test.Cross(global_x)))
    the_lw.WriteFullline("Cross product of global_x and global_y = " + print_vector3(global_x.Cross(global_y)))
    the_lw.WriteFullline("")

    test.Normalize()
    the_lw.WriteFullline("Test normalized = " + print_vector3(test))

if __name__ == '__main__':
    main()
