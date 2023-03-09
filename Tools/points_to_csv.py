# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# NXOpen Python Reference Guide:
# https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_python_ref/index.html

# untested

import os
import math
import NXOpen
import NXOpen.CAE
from typing import List, cast, Optional, Union

the_session: NXOpen.Session = NXOpen.Session.GetSession()
the_uf_session: NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()
base_part = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow


def get_all_points(base_part: NXOpen.BasePart) -> List[NXOpen.Point]:
    """This function returns all points in a part.

    Parameters
    ----------
    base_part: NXOpen.BasePart
        The part for which to to return the points

    Returns
    -------
    List[NXOpen.Point]
        A list containing all points in the base part.
    """
    return base_part.Points.ToArray()


def list_csv(points: List[NXOpen.Point]) -> None:
    """This function lists the coordinates of all points to the listing window.

    Parameters
    ----------
    points: List[NXOpen.Point]
        The list of points to list the coordinates for in the listing window.
    """
    for item in points:
        the_lw.WriteFullline(str(item.Coordinates.X).replace(",",".") + "," + str(item.Coordinates.Y).replace(",",".") + "," + str(item.Coordinates.Z).replace(",","."))


def create_full_path(file_name: str, extension: str = ".unv") -> str:
    """This function takes a filename and adds the .unv extension and path of the part if not provided by the user.
    If the fileName contains an extension, this function leaves it untouched, othwerwise adds .unv as extension.
    If the fileName contains a path, this function leaves it untouched, otherwise adds the path of the BasePart as the path.
    Undefined behaviour if basePart has not yet been saved (eg FullPath not available)

    Parameters
    ----------
    file_name: str
        The filename with or without path and .unv extension.

    Returns
    -------
    str
        A string with .unv extension and path of the basePart if the fileName parameter did not include a path.
    """
    # check if an extension is included
    if os.path.splitext(file_name)[1] == "":
        file_name = file_name + extension

    # check if path is included in fileName, if not add path of the .sim file
    unv_file_path: str = os.path.dirname(file_name)
    if unv_file_path == "":
        # if the .sim file has never been saved, the next will give an error
        file_name = os.path.join(os.path.dirname(base_part.FullPath), file_name)

    return file_name


def write_csv(file_name: str, points: List[NXOpen.Point]):
    """This function writes the coordinates of all points to a .csv file.

    Parameters
    ----------
    file_name: str
        The file name and path for the csv file. If no path provided, it is written to the location of the part.
    points: List[NXOpen.Point]
        The list of points to write the coordinates to file.
    """

    full_path: str = create_full_path(file_name, ".csv")
    file_content: str = ""
    for item in points:
        file_content = file_content + str(item.Coordinates.X).replace(",",".") + "," + str(item.Coordinates.Y).replace(",",".") + "," + str(item.Coordinates.Z).replace(",",".") + "\n"

    with open(full_path, 'w') as file:
        file.write(file_content)


def main():
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)

    all_points: List[NXOpen.Point] = get_all_points(base_part)
    # List all points in the listing window
    list_csv(all_points)
    # Write points to csv file
    write_csv(f"C:\\myPoints.csv", all_points)


if __name__ == '__main__':
    main()
