# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# NXOpen Python Reference Guide:
# https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_python_ref/index.html

import sys
import os
import subprocess
import NXOpen
import NXOpen.CAE
from typing import List, cast, Optional, Union

the_session: NXOpen.Session = NXOpen.Session.GetSession()
the_uf_session: NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()
base_part = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow


def solve_solution(solution_name: str):
    """This function solves a solution with the given name, in the active sim file

    Parameters
    ----------
    solution_name: str
        Name of the solution to solve
    """
    the_lw.WriteFullline("Solving " + solution_name)
    sim_part: NXOpen.CAE.SimPart = cast(NXOpen.CAE.SimPart, base_part)

    # get the requested solution
    sim_solutions: List[NXOpen.CAE.SimSolution] = sim_part.Simulation.Solutions.ToArray()
    sim_solution: List[NXOpen.CAE.SimSolution] = [item for item in sim_solutions if item.Name.lower() == solution_name.lower()]
    if sim_solution == None:
        the_lw.WriteFullline("Solution with name " + solution_name + " could not be found in " + sim_part.FullPath)
        return
    else:
        sim_solution = sim_solution[0]

    # solve the solution
    chain: List[NXOpen.CAE.SimSolution] = [sim_solution]
    sim_solve_manager: NXOpen.CAE.SimSolveManager = NXOpen.CAE.SimSolveManager.GetSimSolveManager(the_session)
    # Not sure if the following returns a tuple in Python. In C#, additional parameters are returned through pass by reference using the out keyword
    sim_solve_manager.SolveChainOfSolutions(chain, NXOpen.CAE.SimSolution.SolveOption.Solve, NXOpen.CAE.SimSolution.SetupCheckOption.DoNotCheck, NXOpen.CAE.SimSolution.SolveMode.Foreground)

    # user feedback
    the_lw.WriteFullline("Solved solution " + solution_name)
    sim_solve_manager.SolveChainOfSolutions(chain, NXOpen.CAE.SimSolution.SolveOption.Solve, NXOpen.CAE.SimSolution.SetupCheckOption.DoNotCheck, NXOpen.CAE.SimSolution.SolveMode.Foreground)

def solve_all_solutions():
    """This function solves all solutions in the active sim file
    """
    # Note: don't loop over the solutions and solve. This will give a memory access violation error, but will still solve.
    # The error can be avoided by making the simSolveManager a global variable, so it's not on each call.
    the_lw.WriteFullline("Solving all solutions:")
    sim_solve_manager: NXOpen.CAE.SimSolveManager = NXOpen.CAE.SimSolveManager.GetSimSolveManager(the_session)
    sim_solve_manager.SolveAllSolutions(NXOpen.CAE.SimSolution.SolveOption.Solve, NXOpen.CAE.SimSolution.SetupCheckOption.DoNotCheck, NXOpen.CAE.SimSolution.SolveMode.Foreground)


def solve_dat_file(dat_file: str):
    """This function solves a .dat file by directly calling the nastran.exe executable.
        It takes the location of the nastran.exe executable form the environmental variable UGII_NX_NASTRAN.
        By directly calling the nastran executable, a standalone license for the executable is required!
        Running this with a desktop license wil result in an error:
        "Could not check out license for module: Simcenter Nastran Basic"

    Parameters
    ----------
    dat_file: str
        The full path of the .dat file to be solved. 
        If no extension is provided, .dat is assumed.
        If no directory is provided, assumed same as the sim file
    """
    # get the location nastran.exe via the environmental variable
    UGII_NX_NASTRAN: str = the_session.GetEnvironmentVariableValue("UGII_NX_NASTRAN")
    the_lw.WriteFullline(UGII_NX_NASTRAN)

    # process dat file for path and execution
    full_dat_file: str = create_full_path(dat_file, ".dat")

    # change working directory to the location of the .dat file. 
    # So that this is where the solve happens.
    cwd = os.getcwd()
    os.chdir(os.path.dirname(full_dat_file))
    
    # solve the .dat file.
    result = subprocess.run([UGII_NX_NASTRAN, full_dat_file])
    print(result)
    
    # return to original cwd
    os.chdir(cwd)


def create_full_path(file_name: str, extension: str = ".unv") -> str:
    """This function takes a filename and adds the .unv extension and path of the part if not provided by the user.
    If the fileName contains an extension, this function leaves it untouched, othwerwise adds .unv as extension.
    If the fileName contains a path, this function leaves it untouched, otherwise adds the path of the BasePart as the path.
    Undefined behaviour if basePart has not yet been saved (eg FullPath not available)

    Parameters
    ----------
    file_name: str
        The filename with or without path and .unv extension.

    Returns
    -------
    str
        A string with .unv extension and path of the basePart if the fileName parameter did not include a path.
    """
    # check if an extension is included
    if os.path.splitext(file_name)[1] == "":
        file_name = file_name + extension

    # check if path is included in fileName, if not add path of the .sim file
    unv_file_path: str = os.path.dirname(file_name)
    if unv_file_path == "":
        # if the .sim file has never been saved, the next will give an error
        file_name = os.path.join(os.path.dirname(base_part.FullPath), file_name)

    return file_name


def main():
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)

    if len(sys.argv) == 1:
        # no arguments passed
        # write some sort of a help
        the_lw.WriteFullline("Need to pass the full path of the .sim file as a first argument.")
        the_lw.WriteFullline("All additional parameters should be solutions to solve.")
        the_lw.WriteFullline("If no additional parameters are passed, all solutions in the sim file are solved.")
        return

    # designed to run in batch, so need to open the file.
    # open file using the first argument
    file_name: str = sys.argv[1] # index 0 is the name of the python file itself
    the_lw.WriteFullline("Opening file " + file_name)
    try:
        base_part = the_session.Parts.OpenActiveDisplay(filename, NXOpen.DisplayPartOption.ReplaceExisting)
    except:
        the_lw.WriteFullline("The file " + file_name + " could not be opened!")
        return

    # check if running from a sim part
    if not isinstance(NXOpen.CAE.SimPart, base_part):
        the_lw.WriteFullline("SolveSolution needs to start from a .sim file")
        return

    if len(sys.argv) == 2:
        # only one argument (file to open) so solve all solutions
        solve_all_solutions()
    else:
        for i in range(2, len(sys.argv)):
            # 2 or more arguments. Solve the solution for each argument. (skip arg[1] becasue that's the sim file)
            solve_solution(sys.argv[i])


if __name__ == '__main__':
    main()
