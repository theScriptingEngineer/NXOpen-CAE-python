# intellisense by theScriptingEngineer

import math
import sys
import NXOpen
import NXOpen.CAE
import NXOpen.Fields
from typing import List, cast, Optional, Union
from multipledispatch import dispatch

theSession = NXOpen.Session.GetSession()
basePart: NXOpen.BasePart = theSession.Parts.BaseWork
theLW: NXOpen.ListingWindow = theSession.ListingWindow


def AddSolverSetToSubcase(solutionName: str, subcaseName: str, solverSetName: str) -> None:
    """This function adds a given SolverSet to a given solution and subcase."""
    # check if started from a SimPart, returning othwerwise
    if not isinstance(basePart, NXOpen.CAE.SimPart):
        theLW.WriteFullline("AddSolverSetToSubcase needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart) # explicit casting makes it clear
    simSimulation: NXOpen.CAE.SimSimulation = simPart.Simulation

    # get the requested solution if it exists
    simSolution: NXOpen.CAE.SimSolution = GetSolution(solutionName)
    if simSolution == None:
        # Solution not found
        theLW.WriteFullline("AddSolverSetToSubcase: Solution with name " + solutionName + " not found!")
        return
    
    # check if the subcase exists in the given solution
    simSolutionStep: Optional[NXOpen.CAE.SimSolutionStep] = None
    for i in range(simSolution.StepCount):
        if simSolution.GetStepByIndex(i).Name.lower() == subcaseName.lower():
            # subcase exists
            simSolutionStep = simSolution.GetStepByIndex(i)
    
    if simSolutionStep == None:
        theLW.WriteFullline("AddSolverSetToSubcase: subcase with name " + subcaseName + " not found in solution " + solutionName + "!")
        return

    # check if SolverSet exists
    simLoadSet: List[NXOpen.CAE.SimLoadSet] = [item for item in simSimulation.LoadSets if item.Name.lower() == solverSetName.lower()]
    if len(simLoadSet) == 0:
        # SolverSet not found
        theLW.WriteFullline("AddSolverSetToSubcase: solver set with name " + solverSetName + " not found!")
        return

    simLoadGroup: NXOpen.CAE.SimLoadGroup = cast(NXOpen.CAE.SimLoadGroup, simSolutionStep.Find("Loads"))
    # commented code only for reference
    # simBcGroups: List[NXOpen.CAE.SimBcGroup] = simSolutionStep.GetGroups()
    # simLoadGroup: NXOpen.CAE.SimLoadGroup = cast(NXOpen.CAE.SimLoadGroup, simBcGroups[0])
    simLoadGroup.AddLoadSet(simLoadSet[0])

def AddLoadToSolverSet(solverSetName: str, loadName: str) -> None:
    """This function adds a load with a given name to a SolverSet with a given name."""
    # check if started from a SimPart, returning othwerwise
    if not isinstance(basePart, NXOpen.CAE.SimPart):
        theLW.WriteFullline("AddLoadToSolverSet needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart) # explicit casting makes it clear
    simSimulation: NXOpen.CAE.SimSimulation = simPart.Simulation

    # check if SolverSet exists
    simLoadSet: List[NXOpen.CAE.SimLoadSet] = [item for item in simSimulation.LoadSets if item.Name.lower() == solverSetName.lower()]
    if len(simLoadSet) == 0:
        # SolverSet not found
        theLW.WriteFullline("AddLoadToSolverSet: solver set with name " + solverSetName + " not found!")
        return None

    # get the requested load if it exists
    simLoad: List[NXOpen.CAE.SimLoad] = [item for item in simSimulation.Loads if item.Name.lower() == loadName.lower()]
    if len(simLoad) == 0:
        # Load not found
        theLW.WriteFullline("AddLoadToSolverSet: Load with name " + loadName + " not found!")
        return

    # add the found load to the found solverSet
    loadSetMembers: List[NXOpen.CAE.SimLoad] = [NXOpen.CAE.SimLoad] * 1
    loadSetMembers[0] = simLoad[0]
    simLoadSet[0].AddMemberLoads(loadSetMembers)

def CreateSolverSet(solverSetName: str) -> Optional[NXOpen.CAE.SimLoadSet]:
    """This function creates a SolverSet with the given name.
    Does not create if one with the given name already exists."""
    # check if started from a SimPart, returning othwerwise
    if not isinstance(basePart, NXOpen.CAE.SimPart):
        theLW.WriteFullline("CreateSolverSet needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart) # explicit casting makes it clear
    simSimulation: NXOpen.CAE.SimSimulation = simPart.Simulation

    # check if solverSet already exists
    simLoadSets: List[NXOpen.CAE.SimLoadSet] = [item for item in simSimulation.LoadSets if item.Name.lower() == solverSetName.lower()]
    if len(simLoadSets) != 0:
        # SolverSet already exists
        theLW.WriteFullline("CreateSolverSet: solver set with name " + solverSetName + " already exists!")
        return None

    nullSimLoadSet: Optional[NXOpen.CAE.SimLoadSet] = None
    simLoadSetBuilder: NXOpen.CAE.SimLoadSetBuilder = simSimulation.CreateLoadSetBuilder("StaticLoadSetAppliedLoad", solverSetName, nullSimLoadSet, 0)
    simLoadSet: NXOpen.CAE.SimLoadSet = cast(NXOpen.CAE.SimLoadSet, simLoadSetBuilder.Commit())
    simLoadSetBuilder.Destroy()
    return simLoadSet


def AddLoadToSubcase(solutionName: str, subcaseName: str, loadName: str) -> None:
    """This function adds a given load to a given solution and subcase."""
    # check if started from a SimPart, returning othwerwise
    if not isinstance(basePart, NXOpen.CAE.SimPart):
        theLW.WriteFullline("AddLoadToSubcase needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart) # explicit casting makes it clear
    simSimulation: NXOpen.CAE.SimSimulation = simPart.Simulation

    # get the requested solution if it exists
    simSolution: NXOpen.CAE.SimSolution = GetSolution(solutionName)
    if simSolution == None:
        # Solution not found
        theLW.WriteFullline("AddLoadToSubcase: Solution with name " + solutionName + " not found!")
        return
    
    # check if the subcase exists in the given solution
    simSolutionStep: Optional[NXOpen.CAE.SimSolutionStep] = None
    for i in range(simSolution.StepCount):
        if simSolution.GetStepByIndex(i).Name.lower() == subcaseName.lower():
            # subcase exists
            simSolutionStep = simSolution.GetStepByIndex(i)
    
    if simSolutionStep == None:
        theLW.WriteFullline("AddLoadToSubcase: subcase with name " + subcaseName + " not found in solution " + solutionName + "!")
        return

    # get the requested load if it exists
    simLoad: List[NXOpen.CAE.SimLoad] = [item for item in simSimulation.Loads if item.Name.lower() == loadName.lower()]
    if len(simLoad) == 0:
        # Load not found
        theLW.WriteFullline("AddLoadToSubcase: Load with name " + loadName + " not found!")
        return
    
    simSolutionStep.AddBc(simLoad[0])


def AddConstraintToSolution(solutionName: str, constraintName: str) -> None:
    """This function adds a constraint with the given name to the solution with the given name."""
    # check if started from a SimPart, returning othwerwise
    if not isinstance(basePart, NXOpen.CAE.SimPart):
        theLW.WriteFullline("AddConstraintToSolution needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart) # explicit casting makes it clear
    simSimulation: NXOpen.CAE.SimSimulation = simPart.Simulation

    # get the requested solution if it exists
    simSolution: NXOpen.CAE.SimSolution = GetSolution(solutionName)
    if simSolution == None:
        # Solution with the given name not found
        theLW.WriteFullline("AddConstraintToSolution: Solution with name " + solutionName + " not found!")
        return

    # get the requested Constraint if it exists
    simConstraint: List[NXOpen.CAE.SimSolution] = [item for item in simSimulation.Solutions if item.Name.lower() == solutionName.lower()]
    if len(simConstraint) == 0:
        # Constraint with the given name not found
        theLW.WriteFullline("AddConstraintToSolution: constraint with name " + constraintName + " not found!")
        return

    # add constraint to solution
    simSolution[0].AddBc(simConstraint[0])


def CreateSubcase(solutionName: str, subcaseName: str) -> Optional[NXOpen.CAE.SimSolutionStep]:
    """This function creates a subcase with a given name under the given solution.
    Does not create if already exists.
    """
    # check if started from a SimPart, returning othwerwise
    if not isinstance(basePart, NXOpen.CAE.SimPart):
        theLW.WriteFullline("CreateSubcase needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart) # explicit casting makes it clear
    simSimulation: NXOpen.CAE.SimSimulation = simPart.Simulation

    # get the requested solution if it exists
    simSolution: NXOpen.CAE.SimSolution = GetSolution(solutionName)
    if simSolution == None:
        # Solution not found
        theLW.WriteFullline("CreateSubcase: Solution with name " + solutionName + " not found!")
        return
    
    # check if the subcase already exists in the given solution
    for i in range(simSolution.StepCount):
        if simSolution.GetStepByIndex(i).Name.lower() == subcaseName.lower():
            # subcase already exists
            theLW.WriteFullline("CreateSubcase: subcase with name " + subcaseName + " already exists in solution " + solutionName + "!")
            return simSolution.GetStepByIndex(i)
    
    # create the subcase with the given name but don't activate it
    return simSolution[0].CreateStep(0, False, subcaseName)


def CreateSolution(solutionName: str, outputRequests: str = "Structural Output Requests1", bulkDataEchoRequest: str = "Bulk Data Echo Request1") -> Optional[NXOpen.CAE.SimSolution]:
    """This function creates a solution with the given name.
    An optional output requests and bulk data echo request can be provided as parameters.
    If not provided or the provided is not found the defaults are applied.
    """
    # check if started from a SimPart, returning othwerwise
    if not isinstance(basePart, NXOpen.CAE.SimPart):
        theLW.WriteFullline("CreateSolution needs to start from a .sim file. Exiting")
        return
    # we are now sure that basePart is a SimPart
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart) # explicit casting makes it clear
    simSimulation: NXOpen.CAE.SimSimulation = simPart.Simulation

    simSolution: NXOpen.CAE.SimSolution = GetSolution(solutionName)
    if simSolution == None:
        # create the solution
        theLW.WriteFullline("Creating solution " + solutionName)
        simSolution = simSimulation.CreateSolution("NX NASTRAN", "Structural", "SESTATIC 101 - Single Constraint", solutionName, NXOpen.CAE.SimSimulation.AxisymAbstractionType.NotSet)


    propertyTable: NXOpen.CAE.PropertyTable = simSolution.PropertyTable

    # Look for a ModelingObjectPropertyTable with the given name or the default name "Bulk Data Echo Request1"
    bulkDataPropertyTable: List[NXOpen.CAE.ModelingObjectPropertyTable] = [item for item in simPart.ModelingObjectPropertyTables if item.Name.lower() == bulkDataEchoRequest.lower()]
    if len(bulkDataPropertyTable) == 0:
        # did not find ModelinObjectPropertyTable with name "Bulk Data Echo REquest1"
        theLW.WriteFullline("Warning: could not find Bulk Data Echo Request with name " + bulkDataEchoRequest + ". Applying default one.")
        # check if default exists
        bulkDataPropertyTable: List[NXOpen.CAE.ModelingObjectPropertyTable] = [item for item in simPart.ModelingObjectPropertyTables if item.Name.lower() == "Bulk Data Echo Request1".lower()]
        if len(bulkDataPropertyTable) == 0:
            # default does also not exist. Create it
            bulkDataPropertyTable = simPart.ModelingObjectPropertyTables.CreateModelingObjectPropertyTable("Bulk Data Echo Request", "NX NASTRAN - Structural", "NX NASTRAN", "Bulk Data Echo Request1", 1000)

    propertyTable.SetNamedPropertyTablePropertyValue("Bulk Data Echo Request", bulkDataPropertyTable)

    # Look for a ModelingObjectPropertyTable with the given name or the default name "Structural Output Requests1"
    outputRequestsPropertyTable: List[NXOpen.CAE.ModelingObjectPropertyTable] = [item for item in simPart.ModelingObjectPropertyTables if item.Name.lower() == outputRequests.lower()]
    if len(outputRequestsPropertyTable) == 0:
        # did not find ModelinObjectPropertyTable with name "Bulk Data Echo REquest1"
        theLW.WriteFullline("Warning: could not find Output Requests with name " + outputRequests + ". Applying default one.")
        # check if default exists
        outputRequestsPropertyTable = [item for item in simPart.ModelingObjectPropertyTables if item.Name.lower() == "Structural Output Requests1".lower()]
        if len(outputRequestsPropertyTable) == 0:
            # default does also not exist. Create it
            outputRequestsPropertyTable = simPart.ModelingObjectPropertyTables.CreateModelingObjectPropertyTable("Structural Output Requests", "NX NASTRAN - Structural", "NX NASTRAN", "Bulk Data Echo Request1", 1001)
            # set Von Mises stress location to corner
            outputRequestsPropertyTable.PropertyTable.SetIntegerPropertyValue("Stress - Location", 1)


    propertyTable.SetNamedPropertyTablePropertyValue("Output Requests", outputRequestsPropertyTable)

    return simSolution


def GetSolution(solutionName: str) -> Union[NXOpen.CAE.SimSolution, None]:
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
    simPart: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart) # explicit casting makes it clear
    simSimulation = simPart.Simulation
    simSolutions: List[NXOpen.CAE.SimSolution] = simSimulation.Solutions.ToArray()

    simSolution: List[NXOpen.CAE.SimSolution] = [item for item in simSolutions if item.Name.lower() == solutionName.lower()]
    if len(simSolution) == 0:
        # solution with the given name not found
        return None
    
    # return the first simSolution with the requested name
    return simSolution[0]


def main() :
    theLW.Open()
    theLW.WriteFullline("Starting Main() in " + theSession.ExecutingJournal)

    mySolution: NXOpen.CAE.SimSolution = GetSolution("SolutionName")

    CreateSolverSet("DeckLoadPS")
    AddLoadToSolverSet("DeckLoadPS", "DeckLoadPS1")
    AddLoadToSolverSet("DeckLoadPS", "DeckLoadPS2")
    AddLoadToSolverSet("DeckLoadPS", "DeckLoadPS3")

    CreateSolverSet("DeckLoadSB")
    AddLoadToSolverSet("DeckLoadSB", "DeckLoadSB1")
    AddLoadToSolverSet("DeckLoadSB", "DeckLoadSB2")
    AddLoadToSolverSet("DeckLoadSB", "DeckLoadSB3")

    CreateSolverSet("DeckLoadCenter")
    AddLoadToSolverSet("DeckLoadCenter", "DeckLoadCenter1")
    AddLoadToSolverSet("DeckLoadCenter", "DeckLoadCenter2")
    AddLoadToSolverSet("DeckLoadCenter", "DeckLoadCenter3")

    CreateSolverSet("BottomLoadPS")
    AddLoadToSolverSet("BottomLoadPS", "BottomLoadPS1")
    AddLoadToSolverSet("BottomLoadPS", "BottomLoadPS2")
    AddLoadToSolverSet("BottomLoadPS", "BottomLoadPS3")

    CreateSolverSet("BottomLoadSB")
    AddLoadToSolverSet("BottomLoadSB", "BottomLoadSB1")
    AddLoadToSolverSet("BottomLoadSB", "BottomLoadSB2")
    AddLoadToSolverSet("BottomLoadSB", "BottomLoadSB3")

    CreateSolverSet("BottomLoadCenter")
    AddLoadToSolverSet("BottomLoadCenter", "BottomLoadCenter1")
    AddLoadToSolverSet("BottomLoadCenter", "BottomLoadCenter2")
    AddLoadToSolverSet("BottomLoadCenter", "BottomLoadCenter3")

    CreateSolverSet("DeckLoadAft")
    AddLoadToSolverSet("DeckLoadAft", "DeckLoadPS1")
    AddLoadToSolverSet("DeckLoadAft", "DeckLoadSB1")
    AddLoadToSolverSet("DeckLoadAft", "DeckLoadCenter1")

    CreateSolverSet("DeckLoadMiddle")
    AddLoadToSolverSet("DeckLoadMiddle", "DeckLoadPS2")
    AddLoadToSolverSet("DeckLoadMiddle", "DeckLoadSB2")
    AddLoadToSolverSet("DeckLoadMiddle", "DeckLoadCenter2")

    CreateSolverSet("DeckLoadFore")
    AddLoadToSolverSet("DeckLoadFore", "DeckLoadPS3")
    AddLoadToSolverSet("DeckLoadFore", "DeckLoadSB3")
    AddLoadToSolverSet("DeckLoadFore", "DeckLoadCenter3")

    CreateSolverSet("BottomLoadAft")
    AddLoadToSolverSet("BottomLoadAft", "BottomLoadPS1")
    AddLoadToSolverSet("BottomLoadAft", "BottomLoadSB1")
    AddLoadToSolverSet("BottomLoadAft", "BottomLoadCenter1")

    CreateSolverSet("BottomLoadMiddle")
    AddLoadToSolverSet("BottomLoadMiddle", "BottomLoadPS2")
    AddLoadToSolverSet("BottomLoadMiddle", "BottomLoadSB2")
    AddLoadToSolverSet("BottomLoadMiddle", "BottomLoadCenter2")

    CreateSolverSet("BottomLoadFore")
    AddLoadToSolverSet("BottomLoadFore", "BottomLoadPS3")
    AddLoadToSolverSet("BottomLoadFore", "BottomLoadSB3")
    AddLoadToSolverSet("BottomLoadFore", "BottomLoadCenter3")
    ########################################################################
    ########################################################################
    ########################################################################

    theLW.WriteFullline("Creating solution: Transverse")
    CreateSolution("Transverse")
    CreateSubcase("Transverse", "PS")
    CreateSubcase("Transverse", "Center")
    CreateSubcase("Transverse", "SB")

    AddConstraintToSolution("Transverse","XYZ_Fixed")
    AddConstraintToSolution("Transverse","YZ_Fixed")
    AddConstraintToSolution("Transverse","Z_Fixed")

    AddSolverSetToSubcase("Transverse", "PS", "DeckLoadPS")
    AddSolverSetToSubcase("Transverse", "PS", "BottomLoadPS")

    AddSolverSetToSubcase("Transverse", "Center", "DeckLoadCenter")
    AddSolverSetToSubcase("Transverse", "Center", "BottomLoadCenter")

    AddSolverSetToSubcase("Transverse", "SB", "DeckLoadSB")
    AddSolverSetToSubcase("Transverse", "SB", "BottomLoadSB")
    ########################################################################
    ########################################################################
    ########################################################################
    
    theLW.WriteFullline("Creating solution: Longitudinal")
    CreateSolution("Longitudinal")
    CreateSubcase("Longitudinal", "Aft")
    CreateSubcase("Longitudinal", "Middle")
    CreateSubcase("Longitudinal", "Fwd")

    AddConstraintToSolution("Longitudinal","XYZ_Fixed")
    AddConstraintToSolution("Longitudinal","YZ_Fixed")
    AddConstraintToSolution("Longitudinal","Z_Fixed")

    AddSolverSetToSubcase("Longitudinal", "Aft", "DeckLoadAft")
    AddSolverSetToSubcase("Longitudinal", "Aft", "BottomLoadAft")

    AddSolverSetToSubcase("Longitudinal", "Middle", "DeckLoadMiddle")
    AddSolverSetToSubcase("Longitudinal", "Middle", "BottomLoadMiddle")

    AddSolverSetToSubcase("Longitudinal", "Fwd", "DeckLoadFore")
    AddSolverSetToSubcase("Longitudinal", "Fwd", "BottomLoadFore")
    ########################################################################
    ########################################################################
    ########################################################################

    theLW.WriteFullline("Creating solution: Combined")
    CreateSolution("Combined")
    for i in range(3):
        CreateSubcase("Combined", "Subcase" + str(i + 1))

    AddConstraintToSolution("Combined","XYZ_Fixed")
    AddConstraintToSolution("Combined","YZ_Fixed")
    AddConstraintToSolution("Combined","Z_Fixed")

    AddSolverSetToSubcase("Combined", "Subcase1", "DeckLoadPS")
    AddSolverSetToSubcase("Combined", "Subcase1", "DeckLoadSB")
    AddSolverSetToSubcase("Combined", "Subcase1", "BottomLoadPS")
    AddSolverSetToSubcase("Combined", "Subcase1", "BottomLoadSB")

    AddSolverSetToSubcase("Combined", "Subcase2", "DeckLoadAft")
    AddSolverSetToSubcase("Combined", "Subcase2", "DeckLoadFore")
    AddSolverSetToSubcase("Combined", "Subcase2", "BottomLoadAft")
    AddSolverSetToSubcase("Combined", "Subcase2", "BottomLoadFore")

    AddSolverSetToSubcase("Combined", "Subcase3", "DeckLoadMiddle")
    AddSolverSetToSubcase("Combined", "Subcase3", "BottomLoadMiddle")
    AddLoadToSubcase("Combined", "Subcase3", "DeckLoadCenter1")
    AddLoadToSubcase("Combined", "Subcase3", "DeckLoadCenter2")
    AddLoadToSubcase("Combined", "Subcase3", "DeckLoadCenter3")
    AddLoadToSubcase("Combined", "Subcase3", "BottomLoadCenter1")
    AddLoadToSubcase("Combined", "Subcase3", "BottomLoadCenter2")
    AddLoadToSubcase("Combined", "Subcase3", "BottomLoadCenter3")

if __name__ == '__main__':
    main()
