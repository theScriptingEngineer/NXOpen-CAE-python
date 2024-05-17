# intellisense by theScriptingEngineer
import NXOpen
import NXOpen.CAE
import NXOpen.Fields
from typing import List, cast

the_session = NXOpen.Session.GetSession()
base_part: NXOpen.BasePart = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow

def create_nodal_constraint(node_label: int, dx: float, dy : float, dz: float, rx: float, ry: float, rz: float, constraint_name: str) -> NXOpen.CAE.SimBC:
    """This function creates a constraint on a node. For free, set the value to -777777
        THis is minus 7, six times. Which equals 42 ;) You got to love the NX developers humor.
    
    Parameters
    ----------
    node_label: int
        The node label to appy the constraint to.
    dx: float
        the displacement in global x-direction.
    dy: float
        the displacement in global y-direction.
    dz: float
        the displacement in global z-direction.
    rx: float
        the rotation in global x-direction.
    ry: float
        the rotation in global y-direction.
    rz: float
        the rotation in global z-direction.
    constraint_name: str
        The name of the constraint for the GUI.

    Returns
    -------
    NXOpen.CAE.SimBC
        Returns the created constraint.

    Notes
    -----
    Tested in SC2212

    """
    # check if started from a SimPart, returning othwerwise
    base_part: NXOpen.BasePart = the_session.Parts.BaseWork
    if not isinstance(base_part, NXOpen.CAE.SimPart):
        the_lw.WriteFullline("CreateConstraint needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part) # explicit casting makes it clear
    
    sim_simulation: NXOpen.CAE.SimSimulation = sim_part.Simulation
    # make the active solution inactive, so bondary condition is not automatically added to active subcase
    sim_simulation.ActiveSolution = NXOpen.CAE.SimSolution.Null

    # check if constaint already exists
    sim_constraints: List[NXOpen.CAE.SimConstraint] = [item for item in sim_simulation.Constraints]
    sim_constraint: List[NXOpen.CAE.SimConstraint] = [item for item in sim_constraints if item.Name.lower() == constraint_name.lower()]
    sim_bc_builder: NXOpen.CAE.SimBCBuilder
    if len(sim_constraint) == 0:
        # no constraint with the given name, thus creating the constrain
        sim_bc_builder = sim_simulation.CreateBcBuilderForConstraintDescriptor("UserDefinedDisplacementConstraint", constraint_name, 0)
    elif len(sim_constraint) == 1:
        the_lw.WriteFullline(f'A constraint with the name {constraint_name} already exists therefore editing the constraint.')
        sim_bc_builder = sim_simulation.CreateBcBuilderForBc(sim_constraint[0])
    else:
        the_lw.WriteFullline(f'Multiple constraints with the name {constraint_name} exist. This function requires unique names and is not case sensitive.')
        raise ValueError(f'Multiple constraints with the name {constraint_name} exist.')

    property_table: NXOpen.CAE.PropertyTable = sim_bc_builder.PropertyTable
    field_expression1: NXOpen.Fields.FieldExpression = property_table.GetScalarFieldPropertyValue("DOF1")
    field_expression2: NXOpen.Fields.FieldExpression = property_table.GetScalarFieldPropertyValue("DOF2")
    field_expression3: NXOpen.Fields.FieldExpression = property_table.GetScalarFieldPropertyValue("DOF3")
    field_expression4: NXOpen.Fields.FieldExpression = property_table.GetScalarFieldPropertyValue("DOF4")
    field_expression5: NXOpen.Fields.FieldExpression = property_table.GetScalarFieldPropertyValue("DOF5")
    field_expression6: NXOpen.Fields.FieldExpression = property_table.GetScalarFieldPropertyValue("DOF6")
    
    unit_millimeter: NXOpen.Unit = cast(NXOpen.Unit, sim_part.UnitCollection.FindObject("MilliMeter"))
    indep_var_array1: List[NXOpen.Fields.FieldVariable] = []
    field_expression1.EditFieldExpression(str(dx), unit_millimeter, indep_var_array1, False)
    property_table.SetScalarFieldPropertyValue("DOF1", field_expression1)

    indep_var_array2: List[NXOpen.Fields.FieldVariable] = []
    field_expression2.EditFieldExpression(str(dy), unit_millimeter, indep_var_array2, False)
    property_table.SetScalarFieldPropertyValue("DOF2", field_expression2)

    indep_var_array3: List[NXOpen.Fields.FieldVariable] = []
    field_expression3.EditFieldExpression(str(dz), unit_millimeter, indep_var_array3, False)
    property_table.SetScalarFieldPropertyValue("DOF3", field_expression3)

    unit_degrees: NXOpen.Unit = cast(NXOpen.Unit, sim_part.UnitCollection.FindObject("Degrees"))
    indep_var_array4: List[NXOpen.Fields.FieldVariable] = []
    field_expression4.EditFieldExpression(str(rx), unit_degrees, indep_var_array4, False)
    property_table.SetScalarFieldPropertyValue("DOF4", field_expression4)

    indep_var_array5: List[NXOpen.Fields.FieldVariable] = []
    field_expression5.EditFieldExpression(str(ry), unit_degrees, indep_var_array5, False)
    property_table.SetScalarFieldPropertyValue("DOF5", field_expression5)

    indep_var_array6: List[NXOpen.Fields.FieldVariable] = []
    field_expression6.EditFieldExpression(str(rz), unit_degrees, indep_var_array6, False)
    property_table.SetScalarFieldPropertyValue("DOF6", field_expression6)

    # select the node via the label to assign the constraint to
    set_manager: NXOpen.CAE.SetManager = sim_bc_builder.TargetSetManager
    
    objects: List[NXOpen.CAE.SetObject] = [NXOpen.CAE.SetObject.Obj] * 1
    objects[0] = NXOpen.CAE.SetObject()
    fe_model_ccurrence: NXOpen.CAE.FEModelOccurrence = sim_part.Simulation.Femodel
    fe_node: NXOpen.CAE.FENode = fe_model_ccurrence.FenodeLabelMap.GetNode(node_label)
    if fe_node is None:
        the_lw.WriteFullline("CreateConstraint: node with label " + str(node_label) + " not found in the model. Constaint not created.")
        return

    objects[0].Obj = fe_node
    objects[0].SubType = NXOpen.CAE.CaeSetObjectSubType.NotSet
    objects[0].SubId = 0
    set_manager.SetTargetSetMembers(0, NXOpen.CAE.CaeSetGroupFilterType.Node, objects)
    
    sim_bc: NXOpen.CAE.SimBC = sim_bc_builder.CommitAddBc()
    sim_bc_builder.Destroy()
    
    return sim_bc
def create_nodal_force_default_name(node_label: int, fx: float, fy : float, fz: float):
    defaultName: str = "Nodalforce_" + str(node_label)
    create_nodal_force(node_label, fx, fy, fz, defaultName)


def create_nodal_force(node_label: int, fx: float, fy: float, fz: float, force_name: str):
    # check if started from a SimPart, returning othwerwise
    if not isinstance(base_part, NXOpen.CAE.SimPart):
        the_lw.WriteFullline("CreateNodalForce needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part) # explicit casting makes it clear
    
    sim_simulation: NXOpen.CAE.SimSimulation = sim_part.Simulation
    # make the active solution inactive, so load is not automatically added to active subcase
    sim_simulation.ActiveSolution = NXOpen.CAE.SimSolution.Null

    # check if a nodal force with that name already exists. If it does, update, if not create it
    sim_loads: List[NXOpen.CAE.SimLoad] = sim_part.Simulation.Loads
    sim_load: NXOpen.CAE.SimLoad = [item for item in sim_loads if item.Name.lower() == force_name.lower()]
    if len(sim_load) == 0:
        # load not found
        sim_bc_builder: NXOpen.CAE.SimBCBuilder = sim_simulation.CreateBcBuilderForLoadDescriptor("ComponentForceField", force_name, 0) # overloaded function is unknow to intellisense
    else:
        sim_bc_builder: NXOpen.CAE.SimBCBuilder = sim_simulation.CreateBcBuilderForBc(sim_load[0])
    
    # define the force
    property_table: NXOpen.CAE.PropertyTable = sim_bc_builder.PropertyTable
    set_manager: NXOpen.CAE.SetManager = sim_bc_builder.TargetSetManager
    
    objects: List[NXOpen.CAE.SetObject] = [NXOpen.CAE.SetObject.Obj] * 1
    objects[0] = NXOpen.CAE.SetObject()
    fe_node: NXOpen.CAE.FENode = sim_part.Simulation.Femodel.FenodeLabelMap.GetNode(node_label)
    if fe_node is None:
        the_lw.WriteFullline("CreateNodalForce: node with label " + str(node_label) + " not found in the model. Force not created.")
        return

    objects[0].Obj = fe_node
    objects[0].SubType = NXOpen.CAE.CaeSetObjectSubType.NotSet
    objects[0].SubId = 0
    set_manager.SetTargetSetMembers(0, NXOpen.CAE.CaeSetGroupFilterType.Node, objects)
    
    unit1: NXOpen.Unit = sim_part.UnitCollection.FindObject("Newton")
    expression1: NXOpen.Expression = sim_part.Expressions.CreateSystemExpressionWithUnits(str(fx), unit1)
    expression2: NXOpen.Expression = sim_part.Expressions.CreateSystemExpressionWithUnits(str(fy), unit1)
    expression3: NXOpen.Expression = sim_part.Expressions.CreateSystemExpressionWithUnits(str(fz), unit1)

    field_manager: NXOpen.Fields.FieldManager = cast(NXOpen.Fields.FieldManager, sim_part.FindObject("FieldManager"))
    expressions: List[NXOpen.Expression] = [NXOpen.Expression.Null] * 3 
    expressions[0] = expression1
    expressions[1] = expression2
    expressions[2] = expression3
    vector_field_wrapper: NXOpen.Fields.VectorFieldWrapper = field_manager.CreateVectorFieldWrapperWithExpressions(expressions)
    
    property_table.SetVectorFieldWrapperPropertyValue("CartesianMagnitude", vector_field_wrapper)
    property_table.SetTablePropertyWithoutValue("CylindricalMagnitude")
    property_table.SetVectorFieldWrapperPropertyValue("CylindricalMagnitude", NXOpen.Fields.VectorFieldWrapper.Null)
    property_table.SetTablePropertyWithoutValue("SphericalMagnitude")
    property_table.SetVectorFieldWrapperPropertyValue("SphericalMagnitude", NXOpen.Fields.VectorFieldWrapper.Null)
    property_table.SetTablePropertyWithoutValue("DistributionField")
    property_table.SetScalarFieldWrapperPropertyValue("DistributionField", NXOpen.Fields.ScalarFieldWrapper.Null)
    property_table.SetTablePropertyWithoutValue("ComponentsDistributionField")
    property_table.SetVectorFieldWrapperPropertyValue("ComponentsDistributionField", NXOpen.Fields.VectorFieldWrapper.Null)
    
    sim_bc: NXOpen.CAE.SimBC = sim_bc_builder.CommitAddBc()
    
    sim_bc_builder.Destroy()

def main() :
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)

    # create_nodal_force(1871, 0, 0, -9810, "DeckLoadPS1")
    # create_nodal_force(1948, 0, 0, -9810, "DeckLoadPS2")
    # create_nodal_force(1908, 0, 0, -9810, "DeckLoadPS3")

    # create_nodal_force(1870, 0, 0, -9810, "DeckLoadSB1")
    # create_nodal_force(1938, 0, 0, -9810, "DeckLoadSB2")
    # create_nodal_force(1907, 0, 0, -9810, "DeckLoadSB3")

    # create_nodal_force(1882, 0, 0, -9810, "DeckLoadCenter1")
    # create_nodal_force(1927, 0, 0, -9810, "DeckLoadCenter2")
    # create_nodal_force(1918, 0, 0, -9810, "DeckLoadCenter3")

    # create_nodal_force(3810, 0, 0, 9810, "BottomLoadPS1")
    # create_nodal_force(3692, 0, 0, 9810, "BottomLoadPS2")
    # create_nodal_force(3739, 0, 0, 9810, "BottomLoadPS3")

    # create_nodal_force(3649, 0, 0, 9810, "BottomLoadSB1")
    # create_nodal_force(3684, 0, 0, 9810, "BottomLoadSB2")
    # create_nodal_force(3710, 0, 0, 9810, "BottomLoadSB3")

    # create_nodal_force(3773, 0, 0, 9810, "BottomLoadCenter1")
    # create_nodal_force(3668, 0, 0, 9810, "BottomLoadCenter2")
    # create_nodal_force(3705, 0, 0, 9810, "BottomLoadCenter3")

    # create_nodal_constraint(1969, 0, 0, 0, -777777, -777777, -777777, "XYZ_Fixed")
    # create_nodal_constraint(2010, -777777, 0, 0, -777777, -777777, -777777, "YZ_Fixed")
    # create_nodal_constraint(2012, -777777, -777777, 0, -777777, -777777, -777777, "Z_Fixed")

    create_nodal_force(20232, 0, 0, -9810, "DeckLoadPS1")
    create_nodal_force(20232, 0, 0, -9810, "DeckLoadPS2")
    create_nodal_force(20232, 0, 0, -9810, "DeckLoadPS3")

    create_nodal_force(20232, 0, 0, -9810, "DeckLoadSB1")
    create_nodal_force(20232, 0, 0, -9810, "DeckLoadSB2")
    create_nodal_force(20232, 0, 0, -9810, "DeckLoadSB3")

    create_nodal_force(20232, 0, 0, -9810, "DeckLoadCenter1")
    create_nodal_force(20232, 0, 0, -9810, "DeckLoadCenter2")
    create_nodal_force(20232, 0, 0, -9810, "DeckLoadCenter3")

    create_nodal_force(20232, 0, 0, 9810, "BottomLoadPS1")
    create_nodal_force(20232, 0, 0, 9810, "BottomLoadPS2")
    create_nodal_force(20232, 0, 0, 9810, "BottomLoadPS3")

    create_nodal_force(20232, 0, 0, 9810, "BottomLoadSB1")
    create_nodal_force(20232, 0, 0, 9810, "BottomLoadSB2")
    create_nodal_force(20232, 0, 0, 9810, "BottomLoadSB3")

    create_nodal_force(20232, 0, 0, 9810, "BottomLoadCenter1")
    create_nodal_force(20232, 0, 0, 9810, "BottomLoadCenter2")
    create_nodal_force(20232, 0, 0, 9810, "BottomLoadCenter3")

    create_nodal_constraint(30203, 0, 0, 0, -777777, -777777, -777777, "XYZ_Fixed")
    create_nodal_constraint(32963, -777777, 0, 0, -777777, -777777, -777777, "YZ_Fixed")
    create_nodal_constraint(32964, -777777, -777777, 0, -777777, -777777, -777777, "Z_Fixed")
    
if __name__ == '__main__':
    main()
