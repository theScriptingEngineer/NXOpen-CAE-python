# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)

# SimCenter support for universal file:
# NX12 https://docs.sw.siemens.com/en-US/product/289054037/doc/PL20190719090640300.advanced/html/xid1404617
# Release SC2019.1 https://docs.sw.siemens.com/en-US/product/289054037/doc/PL20190702084816205.advanced/html/xid1404617
# Release SC2020.1 https://docs.sw.siemens.com/en-US/product/289054037/doc/PL20191009145841552.advanced/html/xid1404617
# Release SC2021.1 https://docs.sw.siemens.com/en-US/product/289054037/doc/PL20200601120302950.advanced/html/xid1404617
# Release SC2022.1 https://docs.sw.siemens.com/en-US/product/289054037/doc/PL20201105151514625.advanced/html/xid1404617

# Fortran format codes
# https://www.l3harrisgeospatial.com/docs/format_codes_fortran.html
# https://help.perforce.com/pv-wave/2017.1/PVWAVE_Online_Help/pvwave.html#page/Foundation/ap.a.format.066.09.html

import os
import datetime
import NXOpen
import NXOpen.CAE
from typing import List, cast, Dict

the_session: NXOpen.Session = NXOpen.Session.GetSession()
the_uf_session: NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()
base_part = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow

def create_thickness_header(dataset_label: int, dataset_name: str, type: str) -> str:
    """Creates a universal file dataset header

    Parameters
    ----------
    dataset_label: int
        The label for the dataset
    dataset_name: str
        The name for the dataset
    type: str
        The type of result for the dataset: "Elemental" or "Element-Nodal"
        
    Returns
    -------
    str
        The header as a string
    """
    the_uf_session.Ui.SetStatus("Creating thickness header")
    header: str = ""
    header = header + "{: ^6}".format("-1") + "\n" # every dataset starts with -1
    header = header + "{: ^6}".format("2414") + "\n" # this is the header for dataset 2414
    header = header + "{: ^10}".format(dataset_label) + "\n" # record 1
    header = header + "LOADCASE_NAME_KEY " + dataset_name + "\n" # record 2 - analysis dataset name 40A2: using this syntax, SimCenter will set the load case name to "datasetName"

    # record 3
    if type.strip().lower() == "elemental":
        header = header + "{: ^10}".format("2") + "\n" # Record 3 - dataset location - data on elements

    elif type.strip().lower() == "element-nodal" or type.strip().lower() == "elementnodal" or type.strip().lower() == "element nodal":
        header = header + "{: ^10}".format("3") + "\n" # Record 3 - dataset location - data at nodes on element

    else:
        the_lw.WriteFullline("Unsupported type " + type + " in CreateThicknessHeader. Should be \"elemental\" or \"element-nodal\"")
        raise ValueError("Unsupported type " + type + " in CreateThicknessHeader. Should be \"elemental\" or \"element-nodal\"")
    
    header = header + "RESULT_NAME_KEY " + dataset_name + "\n" # record 4 - analysis dataset name 40A2: using this syntax, will set the resulttype to dataset_name
    header = header + "NONE" + "\n" # record 5 - analysis dataset name 40A2: using this syntax, Simcenter will parse it and show in the GUI.
    header = header + "EXPRESSION_NAME_KEY " + dataset_name + "\n" # record 6 - analysis dataset name 40A2: using this syntax, Simcenter will parse it and show in the GUI.
    # by using utc, the time is clear.
    header = header + "Creation time: "  + str(datetime.datetime.utcnow()) + "\n" # record 7 - analysis dataset name 40A2: using this syntax, Simcenter will parse it and show in the GUI.
    header = header + "NONE" + "\n" # record 8 - analysis dataset name 40A2: using this syntax, Simcenter will parse it and show in the GUI.
    header = header + "{: ^10}".format("1") + "{: ^10}".format("1") + "{: ^10}".format("1") + "{: ^10}".format("94") + "{: ^10}".format("2") + "{: ^10}".format("1") + "\n" # record 9
    header = header + "{: ^10}".format("1") + "{: ^10}".format("0") + "{: ^10}".format(dataset_label) + "{: ^10}".format("0") + "{: ^10}".format("1") + "{: ^10}".format("0") + "{: ^10}".format("0") + "{: ^10}".format("0") + "\n" # record 10
    header = header + "{: ^10}".format("0") + "{: ^10}".format("0") + "\n" # record 11: using this syntax for Simcenter to parse it properly
    header = header + "{: ^10}".format("0.00000E+00") + "{: ^10}".format("0.00000E+00") + "{: ^10}".format("0.00000E+00") + "{: ^10}".format("0.00000E+00") + "{: ^10}".format("0.00000E+00") + "{: ^10}".format("0.00000E+00") + "\n" # record 12: using this syntax for Simcenter to parse it properly
    header = header + "{: ^10}".format("0.00000E+00") + "{: ^10}".format("0.00000E+00") + "{: ^10}".format("0.00000E+00") + "{: ^10}".format("0.00000E+00") + "{: ^10}".format("0.00000E+00") + "{: ^10}".format("0.00000E+00") + "\n" # record 13: using this syntax for Simcenter to parse it properly

    return header


def get_all_fe_elements(base_fem_part: NXOpen.CAE.BaseFemPart) -> Dict[int, NXOpen.CAE.FEElement]:
    """Get all elements from the model.
       Note that this is the most performant way to do so.

    Parameters
    ----------
    base_fem_part: NXOpen.CAE.BaseFemPart
        The BaseFemPart to get the elements from.

    Returns
    -------
    List[NXOpen.CAE.FEElement]
        A list of all FEElements in the base_fem_part
    """

    all_elements: Dict[int, NXOpen.CAE.FEElement] = {}
    fe_element_label_map = base_fem_part.BaseFEModel.FeelementLabelMap
    element_label: int = fe_element_label_map.AskNextElementLabel(0)
    while (element_label > 0):
        all_elements[element_label] = fe_element_label_map.GetElement(element_label)
        element_label = fe_element_label_map.AskNextElementLabel(element_label)
    
    # sort the dict (valid for python 3.7+) even thought the items should be in order from the element label map
    all_elements = dict(sorted(all_elements.items()))
    return all_elements


def create_thickness_records(base_fem_part: NXOpen.CAE.BaseFemPart, fe_element: NXOpen.CAE.FEElement) -> List[str]:
    """This function returns a representation of the Results used in PostInputs.
    Note that the representation is taken from the SolutionResult and not the SimSolution!

    Parameters
    ----------
    base_fem_part: NXOpen.CAE.BaseFemPart
        The BaseFemPart to generate the thickness datasets for.
    fe_element: NXOpen.CAE.FEElement
        The FEElement for which to generate to thickness records for

    Returns
    -------
    List[str]
        A list with the elemental and element-nodal record for the given FEElement.
    """
    
    # user feedback, but not for all, othwerwise some performance hit
    if (fe_element.Label % 1000 == 0):
        the_uf_session.Ui.SetStatus("Generating records for element " + str(fe_element.Label))

    # from the manual it looks like this is the correct code, but it unchecked
    # https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_python_ref/a09128.html#aa053492346c7911e6691696cb41fcb56
    thickness: float = -1
    thickness_unit: NXOpen.Unit
    thickness, thickness_unit = fe_element.Mesh.MeshCollector.ElementPropertyTable.GetNamedPropertyTablePropertyValue("Shell Property").PropertyTable.GetScalarWithDataPropertyValue("element thickness")

    record14_elemental: str = "{: ^10}".format(fe_element.Label) + "{: ^10}".format("1") + "\n"
    record15_elemental: str = "{: ^13}".format(thickness) + "\n"

    # even though the second record is 1 (data present for all nodes) SimCenter will not read it properly use the first value for all nodes!!
    # some versions of (NX12) will even give a "result file in wrong format" error. In this case, simply change the value to 2
    record14_element_nodal: str = "{: ^10}".format(fe_element.Label) + "{: ^10}".format("2") +  "{: ^10}".format(len(fe_element.GetNodes())) + "{: ^10}".format("1") + "\n"

    # Get the element nodal thickness form the element associated data (if defined) - NOT IMPLEMENTED
    # for the python documentation it seems like it is not possible to get the thickness
    # https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_python_ref/a03583.html#a35f17731a5527236c5a8731fce37a741
    # compare to .net:
    # https://docs.sw.siemens.com/documentation/external/PL20200522120320484/en-US/nx_api_sc/nx/1980/nx_api_sc/en-US/nxopen_net/a35347.html#a7a1d17eb44c21e11636df16ecfa16fc4
    # however, should test how many items are returned from the method: all out elements could be returned as a tuple, which is typical for pyton.
    # element_associated_data_utils = base_fem_part.BaseFEModel.NodeElementMgr.ElemAssociatedDataUtils
    # element_associated_data_utils.AskShellData()

    record15_element_nodal: str = "{: ^10}".format("{:.5E}".format(thickness))
    result: List[str] = [record14_elemental + record15_elemental, record14_element_nodal + record15_element_nodal]
    return result


def create_thickness_datasets(base_fem_part: NXOpen.CAE.BaseFemPart) -> List[str]:
    """This function creates an elemental and element-nodal thickness dataset
       for all shell elements in the base_fem_part.

    Parameters
    ----------
    base_fem_part: NXOpen.CAE.BaseFemPart
        The BaseFemPart to generate the thickness datasets for.

    Returns
    -------
    List[str]
        Each dataset as a string.
    """
    the_lw.WriteFullline("---------- WARNING ----------")
    the_lw.WriteFullline("The Element-Nodal result Record 14 field 2 is set to 2: ")
    the_lw.WriteFullline("'Data present for only first node, all other nodes the same'")
    the_lw.WriteFullline("While all nodes are listed individually in Record 15, which is contradictory.")
    the_lw.WriteFullline("When using externally, update Record 14 field 2 to 1!")
    the_lw.WriteFullline("-------- END WARNING ---------")
    
    thickness_dataset_elemental = create_thickness_header(1, "Thickness", "Elemental")
    thickness_dataset_element_nodal = create_thickness_header(1, "Thickness", "Elemental-Nodal") # by providing the same label, both results will get grouped under the loadcase thickness

    all_elements: Dict[int, NXOpen.CAE.FEElement] = get_all_fe_elements(base_fem_part)
    for key, value in all_elements.items():
        if str(value.Shape) == "Quad" or str(value.Shape) == "Tri":
            thickness_dataset_elemental = thickness_dataset_elemental + create_thickness_records(base_fem_part, value)[0]
            thickness_dataset_elemental = thickness_dataset_elemental + create_thickness_records(base_fem_part, value)[1]
    
    thickness_dataset_elemental = thickness_dataset_elemental + "{: ^6}".format("-1")
    thickness_dataset_element_nodal = thickness_dataset_element_nodal + "{: ^6}".format("-1")

    thickness_datasets: List[str] = [thickness_dataset_elemental, thickness_dataset_element_nodal]
    return thickness_datasets


def create_full_path(file_name: str, extension: str = ".unv") -> str:
    """This function takes a filename and adds the .unv extension and path of the part if not provided by the user.
    If the fileName contains an extension, this function leaves it untouched, othwerwise adds .unv as extension.
    If the fileName contains a path, this function leaves it untouched, otherwise adds the path of the BasePart as the path.
    Undefined behaviour if basePart has not yet been saved (eg FullPath not available)

    Parameters
    ----------
    file_name: str
        The filename with or without path and .unv extension.
    extension (optional): str
        The extension to add if not provided. Defaults to .unv

    Returns
    -------
    str
        A string with .unv extension and path of the basePart if the fileName parameter did not include a path.
    """
    # check if .unv is included in fileName
    if os.path.splitext(file_name)[1] != ".unv":
        file_name = file_name + ".unv"

    # check if path is included in fileName, if not add path of the .sim file
    unv_file_path: str = os.path.dirname(file_name)
    if unv_file_path == "":
        # if the .sim file has never been saved, the next will give an error
        file_name = os.path.join(os.path.dirname(base_part.FullPath), file_name)

    return file_name


def write_thickness_results(base_fem_part: NXOpen.CAE.BaseFemPart, file_name: str):
    """This function writes an elemental and element-nodal result to a universal file.
    The content of the result is the shell thickness of all shell elements in the model.

    Parameters
    ----------
    base_fem_part: NXOpen.CAE.BaseFemPart
        The BaseFemPart to generate the thickness result for.
    file_name: str
        The name of the universal file to write the results to
    """
    datasets: List[str] = create_thickness_datasets(base_fem_part)
    file_name = create_full_path(file_name)

    # concatenate all datasets
    unv_file: str = datasets[0] + "\n" + datasets[1]
    with open(file_name, 'w') as file:
        file.write(unv_file)


def main():
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)

    base_fem_part: NXOpen.CAE.BaseFemPart
    if isinstance(base_part, NXOpen.CAE.SimPart):
        the_lw.WriteFullline("Starting from sim file.")
        sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part)
        base_fem_part = cast(NXOpen.CAE.BaseFemPart, sim_part.FemPart)

        # if the baseFemPart is an AssyFemPart then need to make it work for the code to run.
        the_session.Parts.SetWork(base_fem_part)
    
    elif isinstance(base_part, NXOpen.CAE.BaseFemPart):
        the_lw.WriteFullline("Starting from a fem or afem file.")
        base_fem_part = cast(NXOpen.CAE.BaseFemPart, base_part)
    
    else:
        the_lw.WriteFullline("This function needs to start from a .sim, .afem or .fem.")
        return
    
    write_thickness_results(base_fem_part, "Thickness.unv")

    # return to original work part.
    the_session.Parts.SetWork(base_part)


if __name__ == '__main__':
    main()
