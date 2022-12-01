# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# NXOpen Python Reference Guide:
# https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_python_ref/index.html
import math
import sys
import NXOpen
import NXOpen.CAE
import NXOpen.Fields
from typing import List, cast, Optional, Union

theSession = NXOpen.Session.GetSession()
basePart: NXOpen.BasePart = theSession.Parts.BaseWork
theLW: NXOpen.ListingWindow = theSession.ListingWindow

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
    simSimulation: NXOpen.CAE.SimSimulation = simPart.Simulation
    simSolutions: List[NXOpen.CAE.SimSolution] = simSimulation.Solutions.ToArray()

    simSolution: List[NXOpen.CAE.SimSolution] = [item for item in simSolutions if item.Name.lower() == solutionName.lower()]
    if len(simSolution) == 0:
        # solution not found
        return None
    
    # return the first simSolution with the requested name
    return simSolution[0]


def main() :
    theLW.Open()
    theLW.WriteFullline("Starting Main() in " + theSession.ExecutingJournal)

if __name__ == '__main__':
    main()