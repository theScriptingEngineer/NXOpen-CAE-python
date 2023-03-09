# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# NXOpen Python Reference Guide:
# https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_python_ref/index.html

# untested

import NXOpen
import NXOpen.CAE
from typing import List, cast, Optional, Union

the_session: NXOpen.Session = NXOpen.Session.GetSession()
the_uf_session: NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()
the_lw: NXOpen.ListingWindow = the_session.ListingWindow


def indentation(level: int) -> str:
    """Helper method to create indentations (eg tabs) with a given length.
       Can be used in print strings in a tree like structure

    Parameters
    ----------
    level: int
        The depth of the indentations.

    Returns
    -------
    str
        The indentation
    """
    indentation: str = ""
    for i in range(level + 1):
        indentation += "\t"
    
    return indentation


def print_component_tree(component: NXOpen.Assemblies.Component, requested_level: int = 0) -> None:
    """Prints the component tree for the given component to the listing window.
       Recursive function

    Parameters
    ----------
    component: NXOpen.Assemblies.Component
        The component for whch to print the component tree
    requested_level: int
        Optional parameter used for creating indentations.
    """
    level: int = requested_level
    the_lw.WriteFullline(indentation(level) + "| " + component.JournalIdentifier + " is a compont(instance) of " + component.Prototype.OwningPart.Name + " located in " + component.OwningPart.Name)
    children: List[NXOpen.Assemblies.Component] = component.GetChildren()
    for i in range(len(children) -1, -1, -1):
        print_component_tree(children[i], level + 1)


def print_part_tree(base_part: NXOpen.BasePart, requested_level: int = 0) -> None:
    """Prints the part tree for the given BasePart to the listing window.
       Recursive function

    Parameters
    ----------
    base_part: NXOpen.BasePart
        The BasePart to print the tree for.
    requested_level: int
        Optional parameter used for creating indentations.
    """
    level: int = requested_level
    if isinstance(NXOpen.CAE.SimPart, base_part):
        # it's a .sim part
        sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part)
        the_lw.WriteFullline(sim_part.Name)

        # both are equal:
        # print_part_tree(sim_part.ComponentAssembly.RootComponent.GetChildren()[0].Prototype.OwningPart)
        print_part_tree(sim_part.FemPart)
    
    elif isinstance(NXOpen.CAE.AssyFemPart, base_part):
        # it's a .afem part
        assy_fem_part: NXOpen.CAE.AssyFemPart = cast(NXOpen.CAE.AssyFemPart, base_part)
        the_lw.WriteFullline(indentation(level) + "| " + assy_fem_part.Name + " located in " + assy_fem_part.FullPath + " linked to part " + assy_fem_part.FullPathForAssociatedCadPart)
        children: List[NXOpen.Assemblies.Component] = cast(NXOpen.Assemblies.ComponentAssembly, assy_fem_part.ComponentAssembly).RootComponent.GetChildren()
        for i in range(len(children) - 1):
            print_part_tree(children[i].Prototype.OwningPart, level + 1)
    
    elif isinstance(NXOpen.CAE.FemPart, base_part):
        # it's a .fem part
        fem_part: NXOpen.CAE.FemPart = cast(NXOpen.CAE.FemPart, base_part)
        # try except since calling femPart.FullPathForAssociatedCadPart on a part which has no cad part results in an error
        try:
            # femPart.MasterCadPart returns the actual part, but is null if the part is not loaded.
            the_lw.WriteFullline(indentation(level) + "| " + fem_part.Name + " which is linked to part " + fem_part.FullPathForAssociatedCadPart)
        except:
            # femPart has no associated cad part
            the_lw.WriteFullline(indentation(level) + "| " + fem_part.Name + " not linked to a part.")
    
    else:
        # it's a .prt part, but can still contain components
        the_lw.WriteFullline(indentation(level) + "| " + base_part.Name + " located in " + base_part.FullPath)
        children: List[NXOpen.Assemblies.Component] = cast(NXOpen.Assemblies.ComponentAssembly, base_part.ComponentAssembly).RootComponent.GetChildren()
        for i in range(len(children) - 1):
            print_part_tree(children[i].Prototype.OwningPart, level + 1)


def main():
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)

    all_parts_in_session: List[NXOpen.BasePart] = the_session.Parts.ToArray()
    the_lw.WriteFullline("The following parts are loaded in the session: ")
    for part in all_parts_in_session:
        the_lw.WriteFullline("{:<50}{:<128}".format(part.Name, part.FullPath))
    the_lw.WriteFullline("")

    base_part: NXOpen.BasePart = the_session.Parts.BaseWork
    base_display_part: NXOpen.BasePart = the_session.Parts.BaseDisplay
    the_lw.WriteFullline("The current workpart is: " + base_part.Name + " located in " + base_part.FullPath)
    the_lw.WriteFullline("The current displaypart is: " + base_display_part.Name + " located in " + base_display_part.FullPath)
    the_lw.WriteFullline("")


if __name__ == '__main__':
    main()
