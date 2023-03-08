# intellisense by theScriptingEngineer

import math
import sys
import NXOpen
import NXOpen.CAE
import NXOpen.Fields
from typing import List, cast, Optional, Union

the_session = NXOpen.Session.GetSession()
base_part: NXOpen.BasePart = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow


def add_solver_set_to_subcase(solution_name: str, subcase_name: str, solver_set_name: str) -> None:
    """This function adds a given SolverSet to a given solution and subcase.

    Parameters
    ----------
    solution_name: str
        The name of the solution containing the subcase.
    subcase_name: str
        The name of the subcase to add the solver set to.
    solver_set_name: str
        The name of the solver set to add.
    """
    # check if started from a SimPart, returning othwerwise
    if not isinstance(base_part, NXOpen.CAE.SimPart):
        the_lw.WriteFullline("AddSolverSetToSubcase needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part) # explicit casting makes it clear
    sim_simulation: NXOpen.CAE.SimSimulation = sim_part.Simulation

    # get the requested solution if it exists
    sim_solution: NXOpen.CAE.SimSolution = get_solution(solution_name)
    if sim_solution == None:
        # Solution not found
        the_lw.WriteFullline("AddSolverSetToSubcase: Solution with name " + solution_name + " not found!")
        return
    
    # check if the subcase exists in the given solution
    sim_solution_step: Optional[NXOpen.CAE.SimSolutionStep] = None
    for i in range(sim_solution.StepCount):
        if sim_solution.GetStepByIndex(i).Name.lower() == subcase_name.lower():
            # subcase exists
            sim_solution_step = sim_solution.GetStepByIndex(i)
    
    if sim_solution_step == None:
        the_lw.WriteFullline("AddSolverSetToSubcase: subcase with name " + subcase_name + " not found in solution " + solution_name + "!")
        return

    # check if SolverSet exists
    sim_load_set: List[NXOpen.CAE.SimLoadSet] = [item for item in sim_simulation.LoadSets if item.Name.lower() == solver_set_name.lower()]
    if len(sim_load_set) == 0:
        # SolverSet not found
        the_lw.WriteFullline("AddSolverSetToSubcase: solver set with name " + solver_set_name + " not found!")
        return

    simLoad_group: NXOpen.CAE.SimLoadGroup = cast(NXOpen.CAE.SimLoadGroup, sim_solution_step.Find("Loads"))
    # commented code only for reference
    # simBcGroups: List[NXOpen.CAE.SimBcGroup] = simSolutionStep.GetGroups()
    # simLoadGroup: NXOpen.CAE.SimLoadGroup = cast(NXOpen.CAE.SimLoadGroup, simBcGroups[0])
    simLoad_group.AddLoadSet(sim_load_set[0])

def add_load_to_solver_set(solver_set_name: str, load_name: str) -> None:
    """This function adds a load with a given name to a SolverSet with a given name.

    Parameters
    ----------
    solver_set_name: str
        The name of the solver set to add the load to.
    load_name: str
        The name of the load to add to the solver set.
    """
    # check if started from a SimPart, returning othwerwise
    if not isinstance(base_part, NXOpen.CAE.SimPart):
        the_lw.WriteFullline("AddLoadToSolverSet needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part) # explicit casting makes it clear
    sim_simulation: NXOpen.CAE.SimSimulation = sim_part.Simulation

    # check if SolverSet exists
    sim_load_set: List[NXOpen.CAE.SimLoadSet] = [item for item in sim_simulation.LoadSets if item.Name.lower() == solver_set_name.lower()]
    if len(sim_load_set) == 0:
        # SolverSet not found
        the_lw.WriteFullline("AddLoadToSolverSet: solver set with name " + solver_set_name + " not found!")
        return None

    # get the requested load if it exists
    sim_load: List[NXOpen.CAE.SimLoad] = [item for item in sim_simulation.Loads if item.Name.lower() == load_name.lower()]
    if len(sim_load) == 0:
        # Load not found
        the_lw.WriteFullline("AddLoadToSolverSet: Load with name " + load_name + " not found!")
        return

    # add the found load to the found solverSet
    load_set_members: List[NXOpen.CAE.SimLoad] = [NXOpen.CAE.SimLoad] * 1
    load_set_members[0] = sim_load[0]
    sim_load_set[0].AddMemberLoads(load_set_members)


def create_solver_set(solver_set_name: str) -> Optional[NXOpen.CAE.SimLoadSet]:
    """This function creates a SolverSet with the given name.
    Does not create if one with the given name already exists.
    
    Parameters
    ----------
    solver_set_name: str
        The name of the solver set to create
    
    Returns
    -------
    NXOpen.CAE.SimLoadSet or None
        Returns the created solver set if created. None otherwise
    """
    # check if started from a SimPart, returning othwerwise
    if not isinstance(base_part, NXOpen.CAE.SimPart):
        the_lw.WriteFullline("CreateSolverSet needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part) # explicit casting makes it clear
    sim_simulation: NXOpen.CAE.SimSimulation = sim_part.Simulation

    # check if solverSet already exists
    sim_load_sets: List[NXOpen.CAE.SimLoadSet] = [item for item in sim_simulation.LoadSets if item.Name.lower() == solver_set_name.lower()]
    if len(sim_load_sets) != 0:
        # SolverSet already exists
        the_lw.WriteFullline("CreateSolverSet: solver set with name " + solver_set_name + " already exists!")
        return

    null_sim_load_set: Optional[NXOpen.CAE.SimLoadSet] = None
    sim_load_set_builder: NXOpen.CAE.SimLoadSetBuilder = sim_simulation.CreateLoadSetBuilder("StaticLoadSetAppliedLoad", solver_set_name, null_sim_load_set, 0)
    sim_load_set: NXOpen.CAE.SimLoadSet = cast(NXOpen.CAE.SimLoadSet, sim_load_set_builder.Commit())
    
    sim_load_set_builder.Destroy()
    
    return sim_load_set


def add_load_to_subcase(solution_name: str, subcase_name: str, load_name: str) -> None:
    """This function adds a given load to a given solution and subcase.
    
    Parameters
    ----------
    solution_name: str
        The name of the solution containing the subcase.
    subcase_name: str
        The name of the subcase to add the load to.
    load_name: str
        The name of the load to add
    """
    # check if started from a SimPart, returning othwerwise
    if not isinstance(base_part, NXOpen.CAE.SimPart):
        the_lw.WriteFullline("AddLoadToSubcase needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part) # explicit casting makes it clear
    sim_simulation: NXOpen.CAE.SimSimulation = sim_part.Simulation

    # get the requested solution if it exists
    sim_solution: NXOpen.CAE.SimSolution = get_solution(solution_name)
    if sim_solution == None:
        # Solution not found
        the_lw.WriteFullline("AddLoadToSubcase: Solution with name " + solution_name + " not found!")
        return
    
    # check if the subcase exists in the given solution
    sim_solution_step: Optional[NXOpen.CAE.SimSolutionStep] = None
    for i in range(sim_solution.StepCount):
        if sim_solution.GetStepByIndex(i).Name.lower() == subcase_name.lower():
            # subcase exists
            sim_solution_step = sim_solution.GetStepByIndex(i)
    
    if sim_solution_step == None:
        the_lw.WriteFullline("AddLoadToSubcase: subcase with name " + subcase_name + " not found in solution " + solution_name + "!")
        return

    # get the requested load if it exists
    sim_load: List[NXOpen.CAE.SimLoad] = [item for item in sim_simulation.Loads if item.Name.lower() == load_name.lower()]
    if len(sim_load) == 0:
        # Load not found
        the_lw.WriteFullline("AddLoadToSubcase: Load with name " + load_name + " not found!")
        return
    
    sim_solution_step.AddBc(sim_load[0])


def add_constraint_to_solution(solution_name: str, constraint_name: str) -> None:
    """This function adds a constraint with the given name to the solution with the given name.
    
    Parameters
    ----------
    solution_name: str
        The name of the solution to add the constraint to
    constraint_name: str
        The name of the constraint to add
    """
    # check if started from a SimPart, returning othwerwise
    if not isinstance(base_part, NXOpen.CAE.SimPart):
        the_lw.WriteFullline("AddConstraintToSolution needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    sim_sart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part) # explicit casting makes it clear
    sim_simulation: NXOpen.CAE.SimSimulation = sim_sart.Simulation

    # get the requested solution if it exists
    sim_solution: NXOpen.CAE.SimSolution = get_solution(solution_name)
    if sim_solution == None:
        # Solution with the given name not found
        the_lw.WriteFullline("AddConstraintToSolution: Solution with name " + solution_name + " not found!")
        return

    # get the requested Constraint if it exists
    sim_constraint: List[NXOpen.CAE.SimSolution] = [item for item in sim_simulation.Solutions if item.Name.lower() == solution_name.lower()]
    if len(sim_constraint) == 0:
        # Constraint with the given name not found
        the_lw.WriteFullline("AddConstraintToSolution: constraint with name " + constraint_name + " not found!")
        return

    # add constraint to solution
    sim_solution[0].AddBc(sim_constraint[0])


def create_subcase(solution_name: str, subcase_name: str) -> Optional[NXOpen.CAE.SimSolutionStep]:
    """This function creates a subcase with a given name under the given solution.
    Does not create if already exists.
    
    Parameters
    ----------
    solution_name: str
        The name of the solution to create the subcase under
    subcase_name: str
        The name of the subcase to create
    
    Returns
    -------
    NXOpen.CAE.SimSolutionStep or None
        Returns the created subcase if created. None otherwise
    """
    # check if started from a SimPart, returning othwerwise
    if not isinstance(base_part, NXOpen.CAE.SimPart):
        the_lw.WriteFullline("CreateSubcase needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part) # explicit casting makes it clear

    # get the requested solution if it exists
    sim_solution: NXOpen.CAE.SimSolution = get_solution(solution_name)
    if sim_solution == None:
        # Solution not found
        the_lw.WriteFullline("CreateSubcase: Solution with name " + solution_name + " not found!")
        return
    
    # check if the subcase already exists in the given solution
    for i in range(sim_solution.StepCount):
        if sim_solution.GetStepByIndex(i).Name.lower() == subcase_name.lower():
            # subcase already exists
            the_lw.WriteFullline("CreateSubcase: subcase with name " + subcase_name + " already exists in solution " + solution_name + "!")
            return sim_solution.GetStepByIndex(i)
    
    # create the subcase with the given name but don't activate it
    return sim_solution[0].CreateStep(0, False, subcase_name)


def create_solution(solution_name: str, output_requests: str = "Structural Output Requests1", bulk_data_echo_request: str = "Bulk Data Echo Request1") -> Optional[NXOpen.CAE.SimSolution]:
    """This function creates a solution with the given name, updated an existing if one already exists with that name.
    An optional output requests and bulk data echo request can be provided as parameters.
    If not provided or the provided is not found the defaults are applied.
    
    Parameters
    ----------
    solution_name: str
        The name of the solution to create
    optional output_requests: str
        The name of the structural ouput request to set for the solution
    optional bulk_data_echo_request: str
        The name of the bulk data echo request to set for the solution

    Returns
    -------
    NXOpen.CAE.SimSolution or None
        Returns the created subcase if created. The existing one with this name and updated if it exists
    """
    # check if started from a SimPart, returning othwerwise
    if not isinstance(base_part, NXOpen.CAE.SimPart):
        the_lw.WriteFullline("CreateSolution needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part) # explicit casting makes it clear
    sim_simulation: NXOpen.CAE.SimSimulation = sim_part.Simulation

    sim_solution: NXOpen.CAE.SimSolution = get_solution(solution_name)
    if sim_solution == None:
        # create the solution
        the_lw.WriteFullline("Creating solution " + solution_name)
        sim_solution = sim_simulation.CreateSolution("NX NASTRAN", "Structural", "SESTATIC 101 - Single Constraint", solution_name, NXOpen.CAE.SimSimulation.AxisymAbstractionType.NotSet)


    property_table: NXOpen.CAE.PropertyTable = sim_solution.PropertyTable

    # Look for a ModelingObjectPropertyTable with the given name or the default name "Bulk Data Echo Request1"
    bulk_data_property_table: List[NXOpen.CAE.ModelingObjectPropertyTable] = [item for item in sim_part.ModelingObjectPropertyTables if item.Name.lower() == bulk_data_echo_request.lower()]
    if len(bulk_data_property_table) == 0:
        # did not find ModelinObjectPropertyTable with name "Bulk Data Echo REquest1"
        the_lw.WriteFullline("Warning: could not find Bulk Data Echo Request with name " + bulk_data_echo_request + ". Applying default one.")
        # check if default exists
        bulk_data_property_table: List[NXOpen.CAE.ModelingObjectPropertyTable] = [item for item in sim_part.ModelingObjectPropertyTables if item.Name.lower() == "Bulk Data Echo Request1".lower()]
        if len(bulk_data_property_table) == 0:
            # default does also not exist. Create it
            bulk_data_property_table = sim_part.ModelingObjectPropertyTables.CreateModelingObjectPropertyTable("Bulk Data Echo Request", "NX NASTRAN - Structural", "NX NASTRAN", "Bulk Data Echo Request1", 1000)

    property_table.SetNamedPropertyTablePropertyValue("Bulk Data Echo Request", bulk_data_property_table)

    # Look for a ModelingObjectPropertyTable with the given name or the default name "Structural Output Requests1"
    output_requests_property_table: List[NXOpen.CAE.ModelingObjectPropertyTable] = [item for item in sim_part.ModelingObjectPropertyTables if item.Name.lower() == output_requests.lower()]
    if len(output_requests_property_table) == 0:
        # did not find ModelinObjectPropertyTable with name "Bulk Data Echo REquest1"
        the_lw.WriteFullline("Warning: could not find Output Requests with name " + output_requests + ". Applying default one.")
        # check if default exists
        output_requests_property_table = [item for item in sim_part.ModelingObjectPropertyTables if item.Name.lower() == "Structural Output Requests1".lower()]
        if len(output_requests_property_table) == 0:
            # default does also not exist. Create it
            output_requests_property_table = sim_part.ModelingObjectPropertyTables.CreateModelingObjectPropertyTable("Structural Output Requests", "NX NASTRAN - Structural", "NX NASTRAN", "Bulk Data Echo Request1", 1001)
            # set Von Mises stress location to corner
            output_requests_property_table.PropertyTable.SetIntegerPropertyValue("Stress - Location", 1)


    property_table.SetNamedPropertyTablePropertyValue("Output Requests", output_requests_property_table)

    return sim_solution


def get_solution(solution_name: str) -> Union[NXOpen.CAE.SimSolution, None]:
    """This function returns the SimSolution object with the given name.
    Returns None if not found, so the user can check and act accordingly

    Parameters
    ----------
    solutionName: int
        The name of the solution to return, case insensitive
    
    Returns
    -------
    NXOpen.CAE.SimSolution or None
        The FIRST solution object with the given name if found, None otherwise
    """
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part) # explicit casting makes it clear
    sim_simulation = sim_part.Simulation
    sim_solutions: List[NXOpen.CAE.SimSolution] = sim_simulation.Solutions.ToArray()

    sim_solution: List[NXOpen.CAE.SimSolution] = [item for item in sim_solutions if item.Name.lower() == solution_name.lower()]
    if len(sim_solution) == 0:
        # solution with the given name not found
        return None
    
    # return the first simSolution with the requested name
    return sim_solution[0]


def main() :
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)

    mySolution: NXOpen.CAE.SimSolution = get_solution("SolutionName")

    create_solver_set("DeckLoadPS")
    add_load_to_solver_set("DeckLoadPS", "DeckLoadPS1")
    add_load_to_solver_set("DeckLoadPS", "DeckLoadPS2")
    add_load_to_solver_set("DeckLoadPS", "DeckLoadPS3")

    create_solver_set("DeckLoadSB")
    add_load_to_solver_set("DeckLoadSB", "DeckLoadSB1")
    add_load_to_solver_set("DeckLoadSB", "DeckLoadSB2")
    add_load_to_solver_set("DeckLoadSB", "DeckLoadSB3")

    create_solver_set("DeckLoadCenter")
    add_load_to_solver_set("DeckLoadCenter", "DeckLoadCenter1")
    add_load_to_solver_set("DeckLoadCenter", "DeckLoadCenter2")
    add_load_to_solver_set("DeckLoadCenter", "DeckLoadCenter3")

    create_solver_set("BottomLoadPS")
    add_load_to_solver_set("BottomLoadPS", "BottomLoadPS1")
    add_load_to_solver_set("BottomLoadPS", "BottomLoadPS2")
    add_load_to_solver_set("BottomLoadPS", "BottomLoadPS3")

    create_solver_set("BottomLoadSB")
    add_load_to_solver_set("BottomLoadSB", "BottomLoadSB1")
    add_load_to_solver_set("BottomLoadSB", "BottomLoadSB2")
    add_load_to_solver_set("BottomLoadSB", "BottomLoadSB3")

    create_solver_set("BottomLoadCenter")
    add_load_to_solver_set("BottomLoadCenter", "BottomLoadCenter1")
    add_load_to_solver_set("BottomLoadCenter", "BottomLoadCenter2")
    add_load_to_solver_set("BottomLoadCenter", "BottomLoadCenter3")

    create_solver_set("DeckLoadAft")
    add_load_to_solver_set("DeckLoadAft", "DeckLoadPS1")
    add_load_to_solver_set("DeckLoadAft", "DeckLoadSB1")
    add_load_to_solver_set("DeckLoadAft", "DeckLoadCenter1")

    create_solver_set("DeckLoadMiddle")
    add_load_to_solver_set("DeckLoadMiddle", "DeckLoadPS2")
    add_load_to_solver_set("DeckLoadMiddle", "DeckLoadSB2")
    add_load_to_solver_set("DeckLoadMiddle", "DeckLoadCenter2")

    create_solver_set("DeckLoadFore")
    add_load_to_solver_set("DeckLoadFore", "DeckLoadPS3")
    add_load_to_solver_set("DeckLoadFore", "DeckLoadSB3")
    add_load_to_solver_set("DeckLoadFore", "DeckLoadCenter3")

    create_solver_set("BottomLoadAft")
    add_load_to_solver_set("BottomLoadAft", "BottomLoadPS1")
    add_load_to_solver_set("BottomLoadAft", "BottomLoadSB1")
    add_load_to_solver_set("BottomLoadAft", "BottomLoadCenter1")

    create_solver_set("BottomLoadMiddle")
    add_load_to_solver_set("BottomLoadMiddle", "BottomLoadPS2")
    add_load_to_solver_set("BottomLoadMiddle", "BottomLoadSB2")
    add_load_to_solver_set("BottomLoadMiddle", "BottomLoadCenter2")

    create_solver_set("BottomLoadFore")
    add_load_to_solver_set("BottomLoadFore", "BottomLoadPS3")
    add_load_to_solver_set("BottomLoadFore", "BottomLoadSB3")
    add_load_to_solver_set("BottomLoadFore", "BottomLoadCenter3")
    ########################################################################
    ########################################################################
    ########################################################################

    the_lw.WriteFullline("Creating solution: Transverse")
    create_solution("Transverse")
    create_subcase("Transverse", "PS")
    create_subcase("Transverse", "Center")
    create_subcase("Transverse", "SB")

    add_constraint_to_solution("Transverse","XYZ_Fixed")
    add_constraint_to_solution("Transverse","YZ_Fixed")
    add_constraint_to_solution("Transverse","Z_Fixed")

    add_solver_set_to_subcase("Transverse", "PS", "DeckLoadPS")
    add_solver_set_to_subcase("Transverse", "PS", "BottomLoadPS")

    add_solver_set_to_subcase("Transverse", "Center", "DeckLoadCenter")
    add_solver_set_to_subcase("Transverse", "Center", "BottomLoadCenter")

    add_solver_set_to_subcase("Transverse", "SB", "DeckLoadSB")
    add_solver_set_to_subcase("Transverse", "SB", "BottomLoadSB")
    ########################################################################
    ########################################################################
    ########################################################################
    
    the_lw.WriteFullline("Creating solution: Longitudinal")
    create_solution("Longitudinal")
    create_subcase("Longitudinal", "Aft")
    create_subcase("Longitudinal", "Middle")
    create_subcase("Longitudinal", "Fwd")

    add_constraint_to_solution("Longitudinal","XYZ_Fixed")
    add_constraint_to_solution("Longitudinal","YZ_Fixed")
    add_constraint_to_solution("Longitudinal","Z_Fixed")

    add_solver_set_to_subcase("Longitudinal", "Aft", "DeckLoadAft")
    add_solver_set_to_subcase("Longitudinal", "Aft", "BottomLoadAft")

    add_solver_set_to_subcase("Longitudinal", "Middle", "DeckLoadMiddle")
    add_solver_set_to_subcase("Longitudinal", "Middle", "BottomLoadMiddle")

    add_solver_set_to_subcase("Longitudinal", "Fwd", "DeckLoadFore")
    add_solver_set_to_subcase("Longitudinal", "Fwd", "BottomLoadFore")
    ########################################################################
    ########################################################################
    ########################################################################

    the_lw.WriteFullline("Creating solution: Combined")
    create_solution("Combined")
    for i in range(3):
        create_subcase("Combined", "Subcase" + str(i + 1))

    add_constraint_to_solution("Combined","XYZ_Fixed")
    add_constraint_to_solution("Combined","YZ_Fixed")
    add_constraint_to_solution("Combined","Z_Fixed")

    add_solver_set_to_subcase("Combined", "Subcase1", "DeckLoadPS")
    add_solver_set_to_subcase("Combined", "Subcase1", "DeckLoadSB")
    add_solver_set_to_subcase("Combined", "Subcase1", "BottomLoadPS")
    add_solver_set_to_subcase("Combined", "Subcase1", "BottomLoadSB")

    add_solver_set_to_subcase("Combined", "Subcase2", "DeckLoadAft")
    add_solver_set_to_subcase("Combined", "Subcase2", "DeckLoadFore")
    add_solver_set_to_subcase("Combined", "Subcase2", "BottomLoadAft")
    add_solver_set_to_subcase("Combined", "Subcase2", "BottomLoadFore")

    add_solver_set_to_subcase("Combined", "Subcase3", "DeckLoadMiddle")
    add_solver_set_to_subcase("Combined", "Subcase3", "BottomLoadMiddle")
    add_load_to_subcase("Combined", "Subcase3", "DeckLoadCenter1")
    add_load_to_subcase("Combined", "Subcase3", "DeckLoadCenter2")
    add_load_to_subcase("Combined", "Subcase3", "DeckLoadCenter3")
    add_load_to_subcase("Combined", "Subcase3", "BottomLoadCenter1")
    add_load_to_subcase("Combined", "Subcase3", "BottomLoadCenter2")
    add_load_to_subcase("Combined", "Subcase3", "BottomLoadCenter3")

if __name__ == '__main__':
    main()
