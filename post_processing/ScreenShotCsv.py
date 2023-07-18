# This script automatically generates screenshots of post processing results using the definitions in a .csv file.
# Needs to be run from the .sim file. 
# The definitions of the screenshots are provided as a csv file.
# The file format is as follows:
# FileName, AnnotationText, TemplateName, GroupName, CameraName, Solution, Subcase, Iteration, RestultType, ComponentName
# eg.
# screenshot1.tif, Text displayed on top of screenshot1, Template 1, Group 1, TopView, Solution 1, 1, 1, Stress - Element-Nodal, VonMises
# screenshot2.tif, Text displayed on top of screenshot2, Template 2, Group 2, SideView, Solution 1, 2, 1, Stress - Element-Nodal, VonMises

# These are the entries:
# - FileName: the file name for the screenshot, with or without path. If no path is included, it is saved in the location of the .sim file.
# - AnnotationText: the text to be displayed on top of the screenshot.
# - TemplateName: the name of the PostView template to apply to the displayed results. This contains HOW results are displayed (eg colorbar, feature edges,...)
#                 Note that the definition of the result to be displayed needs to be manually removed by editing the xml file, see NOTE for more details
# - GroupName: The name of the CaeGroup to be displayed. Only one group can be provided. 
#              The name is not case sensitive and if multiple groups with the same name, the first one found will be displayed.
# - CameraName: The name of the camera (as seen in the GUI) to be applied before taking the screenshot. This "orients" what is displayed.
#               Note that you need to save the camera while a result is being displayed, otherwise you might get unexpected results.
# - Solution: The name of the solution to display
# - Subcase: The follower number for the subcase in the solution. Counting starts at 1.
#            Note that this number can depend on the amount of output results.
# - Iteration: The follower number for the iteration. Counting starts at 1. Is 1 for results witout iterations (eg. static structural results)
# - RestultType: The name of the ResultType eg. "Stress - Element-Nodal", "Displacement - Nodal", ...
# - ComponentName: Name of the result component (case-sensitive) eg. 
#                  Scalar, X, Y, Z, Magnitude, Xx, Yy, Zz, Xy, Yz, Zx, MaximumPrincipal, VonMises, MembraneXX, BendingZZ, ShearYZ,... 

# easily create a csv from excel data by concatenating the cell data with commas

#  NOTE that the user needs to manually delete the result from the post template xml file.
#  - Delete the following entries in your template.xml file under the tag <ResultOptions>:
#    - <LoadCase>0</LoadCase>
#    - <Iteration>0</Iteration>
#    - <SubIteration>-1</SubIteration>
#    - <Result>[Displacement][Nodal]</Result>
#    - <Component>Magnitude</Component>

#  It is advised to update the group visibility with the following (assuming there are less than 1000 groups in the model).
#  Note that other types might exist (like <Num3DGroups>). Adjust accordingly.
#		<GroupVisibilities>
#			<Num1DGroups>1000</Num1DGroups>
#			<Visibilities1DGroups>1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1</Visibilities1DGroups>
#			<Num2DGroups>1000</Num2DGroups>
#			<Visibilities2DGroups>1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1</Visibilities2DGroups>
#		</GroupVisibilities>


#  Post processing XML template files are located under the location where UGII_CAE_POST_TEMPLATE_USER_DIR is pointing to.
#  This can be found in the log file.
#  If you also set UGII_CAE_POST_TEMPLATE_EDITOR to for example notepad++.exe,
#  you can directly edit by right-clicking the template in the NX GUI

# tested in
#  - NX12
#  - Simcenter release 2022.1 (version 2023)


import sys
import os # for path operations
import math
# for file open dialog.
# You can use the external TCL installation in combination with embedded python package for NX 
# by setting environment variable TCL_LIBRARY=C:\apps\Python\310\tcl\tcl8.6
# by setting environment variable TK_LIBRARY=C:\apps\Python\310\tcl\tk8.6

# should you get the error (log file) version conflict for package "Tk": have 8.6.9, need exactly 8.6.12
# You can update the version in the line "package require -exact Tk  8.6.12" in the file \tcl\tcl8.6\tcl.init to the one you have.
# You can update the version in the line "package require -exact Tk  8.6.12" in the file \tcl\tk8.6\tk.tcl to the one you have.
import tkinter as tk
from tkinter import filedialog
import NXOpen
import NXOpen.CAE
import NXOpen.Gateway # for creating the image
from typing import List, cast, Optional, Union

the_session: NXOpen.Session = NXOpen.Session.GetSession()
the_ui: NXOpen.UI = NXOpen.UI.GetUI() # type: ignore
base_part = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow
nx_version: str = the_session.GetEnvironmentVariableValue("UGII_VERSION") # theSession.BuildNumber only available from version 1926 onwards


class PostInput:
    """A class for declaring inputs used in CombineResults"""
    _solution: str
    _subcase: int
    _iteration: int
    _resultType: str
    _identifier: str


    def __repr__(self):
        return f"PostInput(Solution='{self._solution}', Subcase={self._subcase}, " \
               f"Iteration={self._iteration}, ResultType='{self._resultType}')"
    

def check_post_input(post_inputs: List[PostInput]) -> None:
    """Check if the provided list of PostInput will not return an error when used in CombineResults.
    Identifiers are checked with separate function check_post_input_identifiers
    Raises exceptions which can be caught by the user.

    Parameters
    ----------
    post_inputs: List[PostInput]
        The array of PostInput to check.
    """
    # Raising ValueError with my own message, instead of simply raising which is the proper way to keep the stack trace.
    # This journal is meant for non developers, so I think a simple clear message is more important than a stack trace.
    for i in range(len(post_inputs)):
        # Does the solution exist?
        sim_solution: NXOpen.CAE.SimSolution = get_solution(post_inputs[i]._solution)
        if sim_solution == None:
            the_lw.WriteFullline("Error in input " + str(post_inputs[i]))
            the_lw.WriteFullline("Solution with name " + post_inputs[i]._solution + " not found.")   
            raise ValueError("Solution with name " + post_inputs[i]._solution + " not found")
        
        # Does the result exist?
        solution_result: List[NXOpen.CAE.SolutionResult] = []
        try:
            solution_result = load_results([post_inputs[i]])
        except:
            the_lw.WriteFullline("Error in input " + str(post_inputs[i]))
            the_lw.WriteFullline("No result for Solution with name " + post_inputs[i]._solution)   
            raise ValueError("No result for Solution with name " + post_inputs[i]._solution)
        
        # Does the subcase exist?
        base_load_cases: List[NXOpen.CAE.BaseLoadcase] = solution_result[0].GetLoadcases()
        loadCase: NXOpen.CAE.Loadcase = None
        try:
            loadCase = cast(NXOpen.CAE.Loadcase, base_load_cases[post_inputs[i]._subcase - 1]) # user starts counting at 1
        except:
            the_lw.WriteFullline("Error in input " + str(post_inputs[i]))
            the_lw.WriteFullline("SubCase with number " + str(post_inputs[i]._subcase) + " not found in solution with name " + post_inputs[i]._solution)
            raise ValueError("SubCase with number " + str(post_inputs[i]._subcase) + " not found in solution with name " + post_inputs[i]._solution)

        # Does the iteration exist?
        base_iterations: List[NXOpen.CAE.BaseIteration] = loadCase.GetIterations()
        iteration: NXOpen.CAE.Iteration = None
        try:
            iteration = cast(NXOpen.CAE.Iteration, base_iterations[post_inputs[i]._iteration - 1]) # user starts counting at 1
        except:
            the_lw.WriteFullline("Error in input " + str(post_inputs[i]))
            the_lw.WriteFullline("Iteration number " + str(post_inputs[i]._iteration) + "not found in SubCase with number " + str(post_inputs[i]._subcase) + " in solution with name " + post_inputs[i]._solution)
            raise ValueError("Iteration number " + str(post_inputs[i]._iteration) + "not found in SubCase with number " + str(post_inputs[i]._subcase) + " in solution with name " + post_inputs[i]._solution)

        # Does the ResultType exist?
        base_result_types: List[NXOpen.CAE.BaseResultType] = iteration.GetResultTypes()
        base_result_type: List[NXOpen.CAE.BaseResultType] = [item for item in base_result_types if item.Name.lower().strip() == post_inputs[i]._resultType.lower().strip()]
        if len(base_result_type) == 0:
            # resulttype does not exist
            the_lw.WriteFullline("Error in input " + str(post_inputs[i]))
            the_lw.WriteFullline("ResultType " + post_inputs[i]._resultType + "not found in iteration number " + str(post_inputs[i]._iteration) + " in SubCase with number " + str(post_inputs[i]._subcase) + " in solution with name " + post_inputs[i]._solution)
            raise ValueError("ResultType " + post_inputs[i]._resultType + "not found in iteration number " + str(post_inputs[i]._iteration) + " in SubCase with number " + str(post_inputs[i]._subcase) + " in solution with name " + post_inputs[i]._solution)


class ScreenShot(PostInput):
    """A class for declaring screenshots, inherits from PostInput"""
    _file_name: str
    _annotation_text: str
    _template_name: str
    _group_name: str
    _component_name: str
    _camera_name: str

    def need_change_result(self, other) -> bool:
        if (self._solution != other._solution):
            return True

        if (self._subcase != other._subcase):
            return True

        if (self._iteration != other._iteration):
            return True

        if (self._resultType != other._resultType):
            return True

        if (self._component_name != other._component_name):
            return True
        
        return False


    def __repr__(self):
        return f"ScreenShot(file_name='{self._file_name}', annotation_text={self._annotation_text}, " \
               f"template_name={self._template_name}, group_name='{self._group_name}', " \
               f"component_name='{self._component_name}', camera_name='{self._camera_name}')"


# Sorting the screenshots
def sort_screenshots(screenshots: List[ScreenShot]) -> List[ScreenShot]:
    return sorted(screenshots, key=lambda x: (x._solution, x._subcase, x._iteration, x._resultType))


def check_screenshots(screenshots: List[ScreenShot]) -> None:
    # Raising ValueError with my own message, instead of simply raising which is the proper way to keep the stack trace.
    # This journal is meant for non developers, so I think a simple clear message is more important than a stack trace.
    
    check_post_input(screenshots)

    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part)
    cae_groups: List[NXOpen.CAE.CaeGroup] = sim_part.CaeGroups
    cameras: List[NXOpen.Display.Camera] = sim_part.Cameras
    # Reload in case template was just created
    the_session.Post.ReloadTemplates()

    for screenshot in screenshots:
        # check the group
        cae_group: List[NXOpen.CAE.CaeGroup] = [x for x in cae_groups if x.Name.lower() == screenshot._group_name.lower()]
        if len(cae_group) == 0:
            the_lw.WriteFullline("Error in input " + screenshot._file_name)
            the_lw.WriteFullline("Group with name " + screenshot._group_name + " not found")
            raise ValueError("Group with name " + screenshot._group_name + " not found")
        elif len(cae_group) != 1:   
            the_lw.WriteFullline("WARNING " + screenshot._file_name)
            the_lw.WriteFullline("FOUND MULTIPLE GROUPS WITH THE NAME " + screenshot._group_name)
        
        # Check the template
        # TemplateSearch throws an error in C# if the template is not found.
        try:
            the_session.Post.TemplateSearch(screenshot._template_name)
        except Exception as e:
            the_lw.WriteFullline("Error in input " + screenshot._file_name)
            the_lw.WriteFullline("Template with name " + screenshot._component_name + " could not be found.")
            raise ValueError("Template with name " + screenshot._template_name + " not found")

        # Check the component name
        try:
            # NXOpen.CAE.Result.Component is a class, not an enum. the __dict__.keys() gets all the attributes by name
            component: NXOpen.CAE.Result.Component = [x for x in NXOpen.CAE.Result.Component.__dict__.keys() if x.lower() == screenshot._group_name.lower()]
        except:
            the_lw.WriteFullline("Error in input " + screenshot._file_name)
            the_lw.WriteFullline("Component with name " + screenshot._component_name + " is not a valid identifier.")
            the_lw.WriteFullline("Component names are case sensitive.")
            the_lw.WriteFullline("Have a look at the options in the post processing navigator in the GUI.")
            the_lw.WriteFullline("Valid identifiers are:")
            for component in NXOpen.CAE.Result.Component.__dict__.keys():
                the_lw.WriteFullline(str(component))
            raise ValueError("Component with name " + screenshot._component_name + " not found")

        # check the camera
        camera: NXOpen.Display.Camera = [x for x in cameras if x.Name.lower() == screenshot._camera_name.lower()]
        if len(camera) == 0:
            the_lw.WriteFullline("Error in input " + screenshot._file_name)
            the_lw.WriteFullline("Camera with name " + screenshot._camera_name + " not found")
            raise ValueError("Camera with name " + screenshot._camera_name + " not found")
        elif len(camera) != 1:   
            the_lw.WriteFullline("WARNING " + screenshot._file_name)
            the_lw.WriteFullline("FOUND MULTIPLE CAMERAS WITH THE NAME " + screenshot._camera_name)


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
    if os.path.splitext(file_name)[1] != "":
        file_name = file_name + extension

    # check if path is included in fileName, if not add path of the .sim file
    unv_file_path: str = os.path.dirname(file_name)
    if unv_file_path == "":
        # if the .sim file has never been saved, the next will give an error
        file_name = os.path.join(os.path.dirname(base_part.FullPath), file_name)

    return file_name

def save_view_to_file(file_name: str) -> None:
    # TODO: add options for file formats other than .tiff
    # check if fileName contains a path. If not save with the .sim file
    file_path_without_extension: str = create_full_path(file_name, "") # should be in line with imageExportBuilder.FileFormat
    file_path_with_extension: str = file_path_without_extension + "tif"

    # delete existing file to mimic overwriting
    if (os.path.exists(file_path_with_extension)):
        os.remove(file_path_without_extension)
    
    image_export_builder: NXOpen.Gateway.ImageExportBuilder = the_ui.CreateImageExportBuilder()
    try:
        # Options
        image_export_builder.EnhanceEdges = True
        image_export_builder.RegionMode = False
        image_export_builder.FileFormat = NXOpen.Gateway.ImageExportBuilder.FileFormats.Tiff # should be in line with the fileName
        image_export_builder.FileName = file_path_without_extension # NX adds the extension for the specific file format
        image_export_builder.BackgroundOption = NXOpen.Gateway.ImageExportBuilder.BackgroundOptions.Transparent
        # Commit the builder
        image_export_builder.Commit()
    except Exception as e:
        the_lw.WriteFullline(str(e))
    finally:
        image_export_builder.Destroy()


def get_result_type(post_input: PostInput, solution_result: NXOpen.CAE.SolutionResult) -> NXOpen.CAE.BaseResultType:
    """Helper function for CombineResults and GetResultParameters.
    Returns the ResultTypes specified in PostInputs

    Parameters
    ----------
    postInputs: List[PostInput]
        The input as an array of PostInput.
    solutionResults: List[NXOpen.CAE.SolutionResult]
        The already loaded results to search through for the results.

    Returns
    -------
    List[NXOpen.CAE.BaseResultType]
        Returns the result objects
    """
    base_load_cases: List[NXOpen.CAE.BaseLoadcase] = solution_result.GetLoadcases()
    loadCase: NXOpen.CAE.Loadcase = cast(NXOpen.CAE.Loadcase, base_load_cases[post_input._subcase - 1]) # user starts counting at 1
    base_iterations: List[NXOpen.CAE.BaseIteration] = loadCase.GetIterations()
    iteration: NXOpen.CAE.Iteration = cast(NXOpen.CAE.Iteration, base_iterations[post_input._iteration - 1]) # user starts counting at 1
    base_result_types: List[NXOpen.CAE.BaseResultType] = iteration.GetResultTypes()
    base_result_type: List[NXOpen.CAE.ResultType] = [item for item in base_result_types if item.Name.lower().strip() == post_input._resultType.lower().strip()][0]
    result_types = cast(NXOpen.CAE.ResultType, base_result_type)
    
    return result_types


def display_result(post_input: PostInput, solution_result: NXOpen.CAE.SolutionResult, component_name: str) -> int:
    # Only set the result and the component, the rest is through the template.
    result_type: NXOpen.CAE.ResultType = get_result_type(post_input, solution_result)
    # Get the component object from the string componentName
    # note this needs to be exact. The check is done when checking the user input.
    component: NXOpen.CAE.Result.Component = getattr(NXOpen.CAE.Result.Component, component_name)
    result_parameters: NXOpen.CAE.ResultParameters = the_session.ResultManager.CreateResultParameters()
    result_parameters.SetGenericResultType(result_type)
    result_parameters.SetResultComponent(component)
    postview_id: int = the_session.Post.CreatePostviewForResult(0, solution_result, False, result_parameters)

    return postview_id


def change_component(postview_id: int, component_name: str) -> None:
    component: NXOpen.CAE.Result.Component = getattr(NXOpen.CAE.Result.Component, component_name)
    result: NXOpen.CAE.Result
    result_parameters: NXOpen.CAE.ResultParameters
    result, result_parameters = the_session.Post.GetResultForPostview(postview_id) # type: ignore
    result_parameters.SetResultComponent(component)
    the_session.Post.PostviewSetResult(postview_id, result_parameters)
    the_session.Post.PostviewUpdate(postview_id)


def set_post_template(postview_id: int, template_name: str) -> None:
    template_id: int = the_session.Post.TemplateSearch(template_name)
    the_session.Post.PostviewApplyTemplate(postview_id, template_id)


def display_elements_in_group(postview_id: int, group_name: str) -> None:

    if nx_version == "v12":
        # NX creates it's own postgroups from the groups in the sim.
        # It only creates a postgroup if either nodes or elements are present in the group.
        # Therefore it's hard to relate the postgroup labels to the group labels in the simfile...
        sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part)
        cae_groups: List[NXOpen.CAE.CaeGroup] = sim_part.CaeGroups
        cae_group: NXOpen.CAE.CaeGroup = [x for x in cae_groups if x.Name.lower() == group_name.lower()][0]

        groupItems: List[NXOpen.TaggedObject] = cae_group.GetEntities()
        # one longer, otherwise a single element is missing from each screenshot (bug in NX)
        groupElementLabels: List[int] = [NXOpen.CAE.BaseResultType] * (len(groupItems) + 1)
        groupElementLabels[0] = 0
        for i in range(len(groupItems)):
            if isinstance(groupItems[i], NXOpen.CAE.FEElement):
                groupElementLabels[i + 1] = (cast(NXOpen.CAE.FEElement, groupItems[i])).Label

        userGroupIds: List[int] = [int] * 1
        # This creates a "PostGroup"
        userGroupIds[0] = the_session.Post.CreateUserGroupFromEntityLabels(postview_id, NXOpen.CAE.CaeGroupCollection.EntityType.Element, groupElementLabels) # type: ignore
        the_session.Post.PostviewApplyUserGroupVisibility(postview_id, userGroupIds, NXOpen.CAE.Post.GroupVisibility.ShowOnly) # type: ignore

    else:
        usergroups_gids = the_session.Post.PostviewGetUserGroupGids(postview_id, [group_name]) # type: ignore single string according docs
        the_session.Post.PostviewApplyUserGroupVisibility(postview_id, usergroups_gids, NXOpen.CAE.Post.GroupVisibility.ShowOnly) # type: ignore


def create_annotation(postview_id: int, annotation_text: str) -> NXOpen.CAE.PostAnnotation:
    post_annotation_builder: NXOpen.CAE.PostAnnotationBuilder = the_session.Post.CreateAnnotationBuilder(postview_id)
    post_annotation_builder.SetName("AnnotationName")
    post_annotation_builder.SetAnnotationType(NXOpen.CAE.PostAnnotationBuilder.Type.Userloc)
    post_annotation_builder.SetCoordinate(0.5, 0.05)

    post_annotation_builder.SetUsertext([annotation_text]) # single string according docs, but actually requires a list of str

    post_annotation = post_annotation_builder.CommitAnnotation()
    post_annotation.DrawBox = True
    post_annotation.BoxTranslucency = False
    post_annotation.BoxFill = True
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part)
    post_annotation.BoxColor = sim_part.Colors.Find(0)
    post_annotation.Draw()

    post_annotation_builder.Dispose()

    return post_annotation


def print_message() -> None:
    the_lw.WriteFullline("##################################################################################################")
    the_lw.WriteFullline("##################################################################################################")
    the_lw.WriteFullline("##################################################################################################")
    the_lw.WriteFullline("THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR")
    the_lw.WriteFullline("IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,")
    the_lw.WriteFullline("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE")
    the_lw.WriteFullline("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER")
    the_lw.WriteFullline("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,")
    the_lw.WriteFullline("OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE")
    the_lw.WriteFullline("SOFTWARE.")
    the_lw.WriteFullline("##################################################################################################")
    the_lw.WriteFullline("##################################################################################################")
    the_lw.WriteFullline("##################################################################################################")
    the_lw.WriteFullline("                        You have just experienced the power of scripting                          ")
    the_lw.WriteFullline("                             brought to you by theScriptingEngineer                               ")
    the_lw.WriteFullline("                                   www.theScriptingEngineer.com                                   ")
    the_lw.WriteFullline("                                  More journals can be found at:                                  ")
    the_lw.WriteFullline("                        https:#github.com/theScriptingEngineer/NXOpen-CAE                        ")
    the_lw.WriteFullline("##################################################################################################")
    the_lw.WriteFullline("##################################################################################################")
    the_lw.WriteFullline("##################################################################################################")
    the_lw.WriteFullline("                                          Learn NXOpen at                                         ")
    the_lw.WriteFullline("https:#www.udemy.com/course/simcenter3d-basic-nxopen-course/?referralCode=4ABC27CFD7D2C57D220B%20")
    the_lw.WriteFullline("##################################################################################################")
    the_lw.WriteFullline("##################################################################################################")
    the_lw.WriteFullline("##################################################################################################")


def set_camera(camera_name: str) -> None:
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part)
    cameras: List[NXOpen.Display.Camera] = sim_part.Cameras
    camera: NXOpen.Display.Camera = [x for x in cameras if x.Name.lower() == camera_name.lower()][0]
    camera.ApplyToView(sim_part.ModelingViews.WorkView)


def get_solution(solution_name: str) -> NXOpen.CAE.SimSolution:
    """This function returns the SimSolution object with the given name.

    Parameters
    ----------
    solution_name: str
        The name of the solution to return. Case insensitive.

    Returns
    -------
    NXOpen.CAE.SimSolution
        Returns a list of SolutionResult.
    """
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part) # explicit casting makes it clear
    sim_simulation: NXOpen.CAE.SimSimulation = sim_part.Simulation

    sim_solutions: List[NXOpen.CAE.SimSolution] = [item for item in sim_simulation.Solutions if item.Name.lower() == solution_name.lower()]
    if len(sim_solutions) == 0:
        return None
    
    return sim_solutions[0]


def load_results(post_inputs: List[PostInput], reference_type: str = "Structural") -> List[NXOpen.CAE.SolutionResult]:
    """Loads the results for the given list of PostInput and returns a list of SolutionResult.
    An exception is raised if the result does not exist (-> to check if CreateReferenceResult raises error or returns None)

    Parameters
    ----------
    post_inputs: List[PostInput]
        The result of each of the provided solutions is loaded.
    reference_type: str
        The type of SimResultReference eg. Structural. Defaults to structral

    Returns
    -------
    NXOpen.CAE.SolutionResult
        Returns a list of SolutionResult.
    """
    solution_results: List[NXOpen.CAE.SolutionResult] = [NXOpen.CAE.SolutionResult] * len(post_inputs)
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part)

    for i in range(len(post_inputs)):
        sim_solution: NXOpen.CAE.SimSolution = get_solution(post_inputs[i]._solution)
        sim_result_reference: NXOpen.CAE.SimResultReference = cast(NXOpen.CAE.SimResultReference, sim_solution.Find(reference_type))

        try:
            # SolutionResult[filename_solutionname]
            solution_results[i] = cast(NXOpen.CAE.SolutionResult, the_session.ResultManager.FindObject("SolutionResult[" + sys.Path.GetFileName(simPart.FullPath) + "_" + sim_solution.Name + "]"))
        except:
            solution_results[i] = the_session.ResultManager.CreateReferenceResult(sim_result_reference)

    return solution_results


def read_screenshot_definitions(file_path: str) -> List[ScreenShot]:
    if (not os.path.exists(file_path)):
        the_lw.WriteFullline("Error: could not find " + file_path)
    
    with open(file_path, 'r') as file:
        csv_string: List[str] = file.readlines()
    
    screenshots_from_file: List[ScreenShot] = []
    for line in csv_string:
        if line == "" or len(line) == 1: # empty line has length 1...
            continue
        values: List[str] = line.split(",")
        if (len(values) != 10):
            the_lw.WriteFullline("There should be 10 items in each input line, separated by commas. Please check the input and make sure not to use commas in the names.")
            for i in range(len(values)):
                the_lw.WriteFullline("Item " + str(i) + ": " + values[i])
            raise Exception("There should be 10 items in each input line, separated by commas. Please check the input above and make sure not to use commas in the names.")

        entry: ScreenShot = ScreenShot()
        entry._file_name = values[0].strip()
        entry._annotation_text = values[1].strip()
        entry._template_name = values[2].strip()
        entry._group_name = values[3].strip()
        entry._camera_name = values[4].strip()
        entry._solution = values[5].strip()
        entry._subcase = int(values[6].strip())
        entry._iteration = int(values[7].strip())
        entry._resultType = values[8].strip()
        entry._component_name = values[9].strip()
        screenshots_from_file.append(entry)

    # Check if the file is empty
    if len(screenshots_from_file) == 0:
        return None
    
    return screenshots_from_file


def delete_post_groups() -> None:
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part)
    cae_groups: List[NXOpen.CAE.CaeGroup] = sim_part.CaeGroups
    post_groups: List[NXOpen.CAE.CaeGroup] = [x for x in cae_groups if x.Name.find("PostGroup") != -1]

    for item in post_groups:
        the_session.UpdateManager.AddObjectsToDeleteList([cast(NXOpen.NXObject, item)])
    
    undo_mark_id = the_session.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "deletePostGroup")
    the_session.UpdateManager.DoUpdate(undo_mark_id)

def main() -> None:
    the_lw.Open()

    # user feedback
    if not isinstance(base_part, NXOpen.CAE.SimPart):
        the_lw.WriteFullline("ScreenshotGenerator needs to be started from a .sim file!")
        return

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    if file_path == None:
        # user pressed cancel
        return

    # read the input file into an array of ScreenShot
    # it's user input, so errors can occur
    screenshots: List[ScreenShot] = []
    try:
        screenshots = read_screenshot_definitions(file_path)
    except Exception as e:
        the_lw.WriteFullline("Failed to parse file " + file_path + ". Please check the screenshot definitions in the file.")
        the_lw.WriteFullline(str(e))
        return
    
    # check for empty file
    if len(screenshots) == 0:
        the_lw.WriteFullline("The file " + file_path + " is empty.")
        return
    
    # check input and catch errors so that the user doesn't get a error pop-up in SC
    try:
        check_screenshots(screenshots)
    except Exception as e:
        the_lw.WriteFullline("The following error occured while checking the screenshot definitions:")
        the_lw.WriteFullline(str(e))
        return
    
    # sort for performance in NX
    # we don't put requirements on the order of the screen shots,
    # only changing the group to display is very fast, compared to changing the result.
    # Sorting minimizes the amount of switches between solutions and subcases and thus improves performance
    screenshots = sort_screenshots(screenshots)

    # load all results before the loop
    solutionResults: List[NXOpen.CAE.SolutionResult] = load_results(screenshots)

    # turn off antialiasing for sharper edges
    originalLineAntialiasing: bool = the_ui.VisualizationVisualPreferences.LineAntialiasing
    originalFullSceneAntialiasing: bool = the_ui.VisualizationVisualPreferences.FullSceneAntialiasing
    the_ui.VisualizationVisualPreferences.LineAntialiasing = False
    the_ui.VisualizationVisualPreferences.FullSceneAntialiasing = False

    postview_id: int = -1
    # process the screenshots
    # using a for loop with index, so I can compare the current to the previous screenshot
    the_lw.WriteFullline("Generated " + str(len(screenshots)) + " screenshots with the following input:")
    for i in range(len(screenshots)):
        the_lw.WriteFullline(str(screenshots[i]))

        # set the result to be displayed
        # don't change if not required (but need to always display the first time):
        if i != 0:
            if screenshots[i].need_change_result(screenshots[i - 1]):
                postview_id = display_result(screenshots[i], solutionResults[i], screenshots[i]._component_name)
        else:
            postview_id = display_result(screenshots[i], solutionResults[i], screenshots[i]._component_name)

        # set the post template (do this before setting the group, as the template might have group visibility still in it)
        # no need to set if it hasn't changed, but displaying another solution removes the template settings so also need to set the template after changing the solution.
        # Note that you need to delete de definition of the 'result to display' from the template xml file! 
        # Otherwise applying the template changes the displayed result.
        if i != 0:
            if screenshots[i]._template_name != screenshots[i - 1]._template_name or screenshots[i]._solution != screenshots[i - 1]._solution:
                set_post_template(postview_id, screenshots[i]._template_name)
            else:
                set_post_template(postview_id, screenshots[i]._template_name)
        else:
            set_post_template(postview_id, screenshots[i]._template_name)

        # Removing the <component> tag, makes NX used the default component (eg. Magnitude for Displacement, Von-Mises for stress, ...)
        # Therefore setting the correct component again after applying the template
        # postview_id = display_result(screenshots[i], solutionResults[i], screenshots[i]._component_name)
        change_component(postview_id, screenshots[i]._component_name)

        # Set the group to display
        display_elements_in_group(postview_id, screenshots[i]._group_name)

        # Create the annotation but only if one given.
        post_annotation: NXOpen.CAE.PostAnnotation = None
        if not (screenshots[i]._annotation_text == "" or screenshots[i]._annotation_text == None):
            post_annotation = create_annotation(postview_id, screenshots[i]._annotation_text)
        
        # Position the result in the view with the camera.
        # Cameras are created in the GUI
        set_camera(screenshots[i]._camera_name)

        # Save the screenshot to file.
        save_view_to_file(screenshots[i]._file_name)

        # Clean up annotations, otherwise annotations pile up
        if post_annotation != None:
            post_annotation.Delete()
    
    if nx_version == "v12":
        delete_post_groups()

    # reset the visualization setting back to original
    the_ui.VisualizationVisualPreferences.LineAntialiasing = originalLineAntialiasing
    the_ui.VisualizationVisualPreferences.FullSceneAntialiasing = originalFullSceneAntialiasing

    print_message()


if __name__ == '__main__':
    main()