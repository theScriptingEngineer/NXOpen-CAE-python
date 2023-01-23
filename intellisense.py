# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# NXOpen Python Reference Guide:
# https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_python_ref/index.html

# This file is used to demonstrate a working intellisense (code completion) for 
# writing NXOpen journals using Python

import sys
import math
import NXOpen
import NXOpen.CAE
from typing import List, cast, Optional, Union

theSession: NXOpen.Session = NXOpen.Session.GetSession()
basePart = theSession.Parts.BaseWork
theLW: NXOpen.ListingWindow = theSession.ListingWindow

theUFSession: NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()
assem = theUFSession.Assem

def get_solution(solution_name: str) -> Union[NXOpen.CAE.SimSolution, None]:
    """This function returns the SimSolution object with the given name.
    Returns None if not found, so the user can check and act accordingly

    Parameters
    ----------
    solution_name: int
        The name of the solution to return, case insensitive

    Returns
    -------
    NXOpen.CAE.SimSolution or None
        The FIRST solution object with the given name if found, None otherwise
    """
    # The next commented block is an extended example where each object is typed.
    # sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, basePart)  # explicit casting makes it clear
    # sim_simulation: NXOpen.CAE.SimSimulation = sim_part.Simulation
    # sim_solution_collection: NXOpen.CAE.SimSolutionCollection = sim_simulation.Solutions
    # sim_solutions: List[NXOpen.CAE.SimSolution] = sim_solution_collection.ToArray()
    # sim_solution: List[NXOpen.CAE.SimSolution] = [item for item in sim_solutions if item.Name.lower == solution_name.lower()]

    # # minimal working example PyCharm
    # sim_part: NXOpen.CAE.SimPart = basePart  # simply typing the sim_part provides intellisense.
    # sim_solutions: List[NXOpen.CAE.SimSolution] = sim_part.Simulation.Solutions.ToArray()

    # # minimal working example Visual Studio Code
    sim_part = cast(NXOpen.CAE.SimPart, basePart)  # explicit casting required in Visual Studio Code
    sim_solutions = sim_part.Simulation.Solutions.ToArray()

    sim_solution = [item for item in sim_solutions if item.Name.lower() == solution_name.lower()]
    if len(sim_solution) == 0:
        # solution with given name not found
        return None

    # return the first solution with the requested name
    return sim_solution[0]


def main():
    theLW.Open()
    theLW.WriteFullline("Starting Main() in " + theSession.ExecutingJournal)

    my_solution: NXOpen.CAE.SimSolution = get_solution("my_solution_name")
    if my_solution is not None:
        print(my_solution.JournalIdentifier)


if __name__ == '__main__':
    main()
