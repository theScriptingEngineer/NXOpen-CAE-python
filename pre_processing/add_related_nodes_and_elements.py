# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# NXOpen Python Reference Guide:
# https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_python_ref/index.html

# This file is used to demonstrate a working intellisense (code completion) for 
# writing NXOpen journals using Python

import sys
import math
import NXOpen
import NXOpen.CAE
import NXOpen.UF
from typing import List, cast, Optional, Union

the_session: NXOpen.Session = NXOpen.Session.GetSession()
base_part = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow

the_uf_session: NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()


def add_related_nodes_and_elements(cae_part: NXOpen.CAE.CaePart) -> None:
    """ This function cycles through all cae groups in a CaePart.
    For each group it adds the related nodes and elements for the bodies and faces in the group.
    Practical for repopulating groups after a (partial) remesh.
    Function is idempotent.

    Parameters
    ----------
    cae_part: NXOpen.CAE.CaePart
        The CaePart to perform this operation on.
    
    Notes
    -----
    Tested in SC2306
    """
    cae_groups: List[NXOpen.CAE.CaeGroupCollection] = cae_part.CaeGroups
    for group in cae_groups: # a CaeGroupCollection is iterable. # type: ignore
        the_lw.WriteFullline("Processing group " + group.Name)
        seeds_body: List[NXOpen.CAE.CAEBody] = []
        seeds_face: List[NXOpen.CAE.CAEFace] = []

        for tagged_object in group.GetEntities():
            if isinstance(tagged_object, NXOpen.CAE.CAEBody):
                seeds_body.append(cast(NXOpen.CAE.CAEBody, tagged_object))
            elif isinstance(tagged_object, NXOpen.CAE.CAEFace):
                seeds_face.append(cast(NXOpen.CAE.CAEFace, tagged_object))

        smart_selection_manager: NXOpen.CAE.SmartSelectionManager = cae_part.SmartSelectionMgr

        related_element_method_body: NXOpen.CAE.RelatedElemMethod = smart_selection_manager.CreateRelatedElemMethod(seeds_body, False)
        # related_node_method_body: NXOpen.CAE.RelatedNodeMethod = smart_selection_manager.CreateNewRelatedNodeMethodFromBody(seeds_body, False)
        # For NX version 2007 (release 2022.1) and later
        related_node_method_body: NXOpen.CAE.RelatedElemMethod = smart_selection_manager.CreateNewRelatedNodeMethodFromBodies(seeds_body, False, False)

        group.AddEntities(related_element_method_body.GetElements())
        group.AddEntities(related_node_method_body.GetNodes())

        related_element_method_face: NXOpen.CAE.RelatedElemMethod = smart_selection_manager.CreateRelatedElemMethod(seeds_face, False)
        # related_node_method_face: NXOpen.CAE.RelatedElemMethod = smart_selection_manager.CreateRelatedNodeMethod(seeds_face, False)
        # For NX version 2007 (release 2022.1) and later
        related_node_method_face: NXOpen.CAE.RelatedElemMethod = smart_selection_manager.CreateNewRelatedNodeMethodFromFaces(seeds_face, False, False)

        group.AddEntities(related_element_method_face.GetElements())
        group.AddEntities(related_node_method_face.GetNodes())


def main():
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)

    add_related_nodes_and_elements(cast(NXOpen.CAE.CaePart, base_part))
    

if __name__ == '__main__':
    main()