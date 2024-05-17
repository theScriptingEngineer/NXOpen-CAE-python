# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# NXOpen Python Reference Guide:
# https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_python_ref/index.html

# untested

import NXOpen
import NXOpen.UF
import NXOpen.CAE
from typing import List, cast, Optional, Union

the_session: NXOpen.Session = NXOpen.Session.GetSession()
the_uf_session: NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()
base_part = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow


def cross_product_vector3d(vector1: NXOpen.Vector3d, vector2: NXOpen.Vector3d) -> NXOpen.Vector3d:
    """
    Calculate the cross product of two vectors.

    Parameters:
        vector1 (NXOpen.Vector3d): The first vector.
        vector2 (NXOpen.Vector3d): The second vector.

    Returns:
        NXOpen.Vector3d: The cross product of the two vectors.
    """
    x = vector1.Y * vector2.Z - vector2.Y * vector1.Z
    y = vector1.Z * vector2.X - vector2.Z * vector1.X
    z = vector1.X * vector2.Y - vector2.X * vector1.Y
    return NXOpen.Vector3d(x, y, z)


def dot_product_vector3d(vector1: NXOpen.Vector3d, vector2: NXOpen.Vector3d) -> float:
    """
    Calculate the dot product of two vectors.

    Parameters:
        vector1 (NXOpen.Vector3d): The first vector.
        vector2 (NXOpen.Vector3d): The second vector.

    Returns:
        float: The dot product of the two vectors.
    """
    return vector1.X * vector2.X + vector1.Y * vector2.Y + vector1.Z * vector2.Z


def get_associated_cad_part(fem_part: NXOpen.CAE.FemPart) -> NXOpen.Part:
    """Gets the associated cad part for a given FemPart.
       Will load the part if not loaded.
       It assumes that the FemPart has an associated cad part (is not an orphan mesh)

    Parameters
    ----------
    fem_part: NXOpen.CAE.FemPart
        The FemPart for which to return the associated cad part.

    Returns
    -------
    NXOpen.Part
        The associated cad part.
    """
    associated_cad_part: NXOpen.Part = fem_part.AssociatedCadPart
    if associated_cad_part == None:
        # "load" the part (right-click load under fem)
        # error will occur if FemPart has no associated cad part:
        #  fem_part.FullPathForAssociatedCadPart will be None and the open will fail.
        associated_cad_part = cast(NXOpen.Part, the_session.Parts.Open(fem_part.FullPathForAssociatedCadPart))
    
    return associated_cad_part


def get_named_datum_planes(cad_part: NXOpen.Part) -> List[NXOpen.DatumPlane]:
    """Searches the part for all datum planes with a name and returns them.
       Naming a datum plane is done by right-clicking on the plane in the GUI and selecting rename.

    Parameters
    ----------
    cad_part: NXOpen.Part
        The part for which to return the named datum planes.

    Returns
    -------
    List[NXOpen.DatumPlane]
        A list with the named datum planes.
    """
    named_datum_planes: List[NXOpen.DatumPlane] = []
    for item in cad_part.Datums: # type: ignore
        # cad_part.Datums.ToArray() will also contain datum axis (if present)
        if type(item) is NXOpen.DatumPlane:
            # item is a datum plane. Now check if it has a name.
            # Note Feature.Name and not Name
            if cast(NXOpen.DatumPlane, item).Feature.Name != "":
                named_datum_planes.append(cast(NXOpen.DatumPlane, item))
    
    return named_datum_planes


def create_selection_recipe(fem_part: NXOpen.CAE.FemPart, datum_plane: NXOpen.DatumPlane, entity_types: List[NXOpen.CAE.CaeSetGroupFilterType]) -> NXOpen.CAE.SelectionRecipe:
    """This function creates a selection recipe around a given datum plane.
       Since a selection recipe is not infinite, the dimensions are hard coded, but can be easily adjusted.

    Parameters
    ----------
    fem_part: NXOpen.CAE.FemPart
        The part in whcih to create a selection recipe.
    datum_plane: NXOpen.DatumPlane
        A datum plane, which is used to define the selection recipe.
    entity_types: List[NXOpen.CAE.CaeSetGroupFilterType]
        A list of filters for the type of objects to add to the selection recipe.

    Returns
    -------
    NXOpen.CAE.SelectionRecipe
        The created selection recipe.
    """
    recipe_thickness: float = 1
    recipe_size: float = 100000

    # unfortunately NXOpen.VectorArithmetic.Vector3 does not exist in Python.
    # Not using general python libraries for this a this would require additional importing of libraries
    origin: NXOpen.Vector3d = NXOpen.Vector3d(datum_plane.Origin.X, datum_plane.Origin.Y, datum_plane.Origin.Z)
    normal: NXOpen.Vector3d = NXOpen.Vector3d(datum_plane.Normal.X, datum_plane.Normal.Y, datum_plane.Normal.Z)

    global_vector: NXOpen.Vector3d = NXOpen.Vector3d(1.0, 0.0, 0.0)
    projection: float = abs(dot_product_vector3d(normal, global_vector)) # absolute value so only need to check larger than 0.999
    if projection >= 0.999:
        # use global y if plane normal paralell to global x vector
        global_vector = NXOpen.Vector3d(0, 1, 0)
    
    # we first project the global onto the plane normal
    # then subtract to get the component of global IN the plane which will be are local axis in the recipe definition
    projection_magnitude: float = dot_product_vector3d(normal, global_vector)
    global_on_normal: NXOpen.Vector3d = NXOpen.Vector3d(normal.X * projection_magnitude, normal.Y * projection_magnitude, normal.Z * projection_magnitude)
    global_on_plane = NXOpen.Vector3d(global_vector.X - global_on_normal.X, global_vector.Y - global_on_normal.Y, global_vector.Z - global_on_normal.Z)

    # normalize
    global_on_plane_magnitude = global_on_plane.X **2 + global_on_plane.Y **2 + global_on_plane.Z **2
    global_on_plane = NXOpen.Vector3d(global_on_plane.X / global_on_plane_magnitude, global_on_plane.Y / global_on_plane_magnitude, global_on_plane.Z / global_on_plane_magnitude)

    # cross product of globalOnPlane and normal give vector in plane, otrhogonal to globalOnPlane
    global_on_plane_normal: NXOpen.Vector3d = cross_product_vector3d(normal, global_on_plane)
    # normalize
    global_on_plane_normal_magnitude = global_on_plane_normal.X **2 + global_on_plane_normal.Y **2 + global_on_plane_normal.Z **2
    global_on_plane_normal = NXOpen.Vector3d(global_on_plane_normal.X / global_on_plane_normal_magnitude, global_on_plane_normal.Y / global_on_plane_normal_magnitude, global_on_plane_normal.Z / global_on_plane_normal_magnitude)

    # offset origin so the recipe is centered around the origin
    # translate half recipeWidth in negative direction of globalOnPlane
    origin = NXOpen.Vector3d(origin.X - global_on_plane.X * recipe_size / 2, origin.Y - global_on_plane.Y * recipe_size / 2, origin.Z - global_on_plane.Z * recipe_size / 2)

    # translate half recipeWidth in negative direction of globalOnPlaneNormal
    origin = NXOpen.Vector3d(origin.X - global_on_plane_normal.X * recipe_size / 2, origin.Y - global_on_plane_normal.Y * recipe_size / 2, origin.Z - global_on_plane_normal.Z * recipe_size / 2)

    # Translate half the thickness in negative normal direction
    origin = NXOpen.Vector3d(origin.X - normal.X * recipe_thickness / 2, origin.Y - normal.Y * recipe_thickness / 2, origin.Z - normal.Z * recipe_thickness / 2)

    # prepare objects to create selection recipe
    recipe_origin: NXOpen.Point3d = NXOpen.Point3d(origin.X, origin.Y, origin.Z)
    x_direction: NXOpen.Vector3d = NXOpen.Vector3d(global_on_plane.X, global_on_plane.Y, global_on_plane.Z)
    y_direction: NXOpen.Vector3d = NXOpen.Vector3d(global_on_plane_normal.X, global_on_plane_normal.Y, global_on_plane_normal.Z)

    recipe_xform: NXOpen.Xform = fem_part.Xforms.CreateXform(recipe_origin, x_direction, y_direction, NXOpen.SmartObject.UpdateOption.AfterModeling, 1.0)
    recipe_coordinate_system: NXOpen.CartesianCoordinateSystem = fem_part.CoordinateSystems.CreateCoordinateSystem(recipe_xform, NXOpen.SmartObject.UpdateOption.AfterModeling)

    unit_millimeter: NXOpen.Unit = cast(NXOpen.UnitCollection, fem_part.UnitCollection).FindObject("MilliMeter")
    expression_length: NXOpen.Expression = fem_part.Expressions.CreateSystemExpressionWithUnits(str(recipe_size), unit_millimeter)
    expression_width: NXOpen.Expression = fem_part.Expressions.CreateSystemExpressionWithUnits(str(recipe_size), unit_millimeter)
    expression_height: NXOpen.Expression = fem_part.Expressions.CreateSystemExpressionWithUnits(str(recipe_thickness), unit_millimeter)

    # selection_recipe: NXOpen.CAE.SelectionRecipe = fem_part.SelectionRecipes.CreateBoxBoundingVolumeRecipe(datum_plane.Feature.Name, recipe_coordinate_system, expression_length, expression_width, expression_height, entity_types)
    selection_recipe_builder = fem_part.SelectionRecipes.CreateSelRecipeBuilder()
    selection_recipe_builder.AddBoxBoundingVolumeStrategy(recipe_coordinate_system, expression_length, expression_width, expression_height, entity_types, NXOpen.CAE.SelRecipeBuilder.InputFilterType.EntireModel, None)
    selection_recipe_builder.RecipeName = datum_plane.Feature.Name

    selection_recipe = selection_recipe_builder.Commit()
    selection_recipe_builder.Destroy()

    return selection_recipe


def create_groups_from_named_planes(fem_part: NXOpen.CAE.FemPart) -> None:
    """This function creates a group with faces and bodies for each named datum plane in the associated cad part.
       All named datum planes are collected from the associated cad part.
       Then for each datum plane a selection recipe is created, "centered around" the datum plane, with the faces and bodies.
       For each selection recipe a group is created and the selection recipe deleted.
       Groups are created instead of selection recipes because older versions of Simcenter cannot use selection recipes in post-processing.
       Function is idempotent.

    Parameters
    ----------
    fem_part: NXOpen.CAE.FemPart
        The part in which to create the groups.
    """
    # Get the associated cad part
    associated_cad_part: NXOpen.Part = get_associated_cad_part(fem_part)

    # Get an array of all named datum planes
    named_datum_planes: List[NXOpen.DatumPlane] = get_named_datum_planes(associated_cad_part)
    if len(named_datum_planes) == 0:
        the_lw.WriteFullline("No named datum planes found in " + associated_cad_part.Name)
        return
    
    the_lw.WriteFullline("Found the following named datum planes in " + associated_cad_part.Name + ":")
    for item in named_datum_planes:
        the_lw.WriteFullline(item.Feature.Name)

    # Create selection recipe for each named datum plane
    selection_recipes: List[NXOpen.CAE.SelectionRecipe] = []
    entity_types: List[NXOpen.CAE.CaeSetGroupFilterType] = []
    entity_types.append(NXOpen.CAE.CaeSetGroupFilterType.GeomFace)
    entity_types.append(NXOpen.CAE.CaeSetGroupFilterType.GeomBody)
    for item in named_datum_planes:
        selection_recipes.append(create_selection_recipe(fem_part, item, entity_types))

    # Create a group for each recipe
    cae_groups: List[NXOpen.CAE.CaeGroup] = fem_part.CaeGroups
    for i in range(len(named_datum_planes)):
        tagged_objects: List[NXOpen.TaggedObject] = selection_recipes[i].GetEntities()
        if len(tagged_objects) == 0:
            the_lw.WriteFullline("Recipe with name " + selection_recipes[i].Name + " contains no items to put into a group")
            continue # continue to the next datum plane
        
        cae_group: List[NXOpen.CAE.CaeGroup] = [item for item in cae_groups if item.Name.lower() == named_datum_planes[i].Feature.Name.lower()]
        if len(cae_group) == 0:
            # no group found with the feaure name, thus creating
            fem_part.CaeGroups.CreateGroup(named_datum_planes[i].Feature.Name, tagged_objects)
        else:
            cae_group[0].SetEntities(tagged_objects)

    # delete temporary selection recipes
    fem_part.SelectionRecipes.Delete(selection_recipes)


def add_related_nodes_and_elements(cae_part: NXOpen.CAE.CaePart):
    """This function cycles through all cae groups in a CaePart.
       For each group it adds the related nodes and elements for the bodies and faces in the group.
       Practical for repopulating groups after a (partial) remesh.
       Function is idempotent.

    Parameters
    ----------
    fem_part: NXOpen.CAE.FemPart
        The CaePart to perform this operation on.
    """
    cae_groups: List[NXOpen.CAE.CaeGroup] = cae_part.CaeGroups
    for group in cae_groups: # type: ignore
        the_lw.WriteFullline("Processing group " + group.Name)
        seeds_body: List[NXOpen.CAE.CAEBody] = []
        seeds_face: List[NXOpen.CAE.CAEFace] = []

        for tagged_object in group.GetEntities():
            if type(tagged_object) is NXOpen.CAE.CAEBody:
                seeds_body.append(cast(NXOpen.CAE.CAEBody, tagged_object))
            
            elif type(tagged_object) is NXOpen.CAE.CAEFace:
                seeds_face.append(cast(NXOpen.CAE.CAEFace, tagged_object))

        smart_selection_manager: NXOpen.CAE.SmartSelectionManager = cae_part.SmartSelectionMgr

        related_element_method_body: NXOpen.CAE.RelatedElemMethod = smart_selection_manager.CreateRelatedElemMethod(seeds_body, False)
        # related_node_method_body: NXOpen.CAE.RelatedNodeMethod = smart_selection_manager.CreateNewRelatedNodeMethodFromBody(seeds_body, False)
        # comment previous line and uncomment next line for NX version 2007 (release 2022.1) and later
        related_node_method_body: NXOpen.CAE.RelatedElemMethod = smart_selection_manager.CreateNewRelatedNodeMethodFromBodies(seeds_body, False, False)

        group.AddEntities(related_element_method_body.GetElements())
        group.AddEntities(related_node_method_body.GetNodes())

        related_element_method_face: NXOpen.CAE.RelatedElemMethod = smart_selection_manager.CreateRelatedElemMethod(seeds_face, False)
        # related_node_method_face: NXOpen.CAE.RelatedElemMethod = smart_selection_manager.CreateRelatedNodeMethod(seeds_face, False)
        # comment previous line and uncomment next line for NX version 2007 (release 2022.1) and later
        related_node_method_face: NXOpen.CAE.RelatedElemMethod = smart_selection_manager.CreateNewRelatedNodeMethodFromFaces(seeds_face, False, False)

        group.AddEntities(related_element_method_face.GetElements())
        group.AddEntities(related_node_method_face.GetNodes())


def main():
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)

    fem_part: NXOpen.CAE.FemPart = None
    if type(base_part) is NXOpen.CAE.SimPart:
        # started from a sim file.
        sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part)
        # switch to the fem or afem
        cae_part: NXOpen.CAE.CaePart = sim_part.FemPart
        if type(base_part) is NXOpen.CAE.AssyFemPart:
            the_lw.WriteFullline("Create groups from CAD does not support .afem files yet.")
            return
        
        fem_part = cast(NXOpen.CAE.FemPart, cae_part)
    
    elif type(base_part) is NXOpen.CAE.AssyFemPart:
        # started from an .afem file
        the_lw.WriteFullline("Create groups from CAD does not support .afem files yet.")
        return

    elif type(base_part) is NXOpen.CAE.FemPart:
        # started from a .fem file
        fem_part = cast(NXOpen.CAE.FemPart, base_part)
    
    else:
        # not started from a base fem part
        the_lw.WriteFullline("Create groups does not work on non-cae parts")
        return

    create_groups_from_named_planes(fem_part)
    add_related_nodes_and_elements(fem_part)

if __name__ == '__main__':
    main()
