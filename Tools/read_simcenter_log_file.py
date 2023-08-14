# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# NXOpen Python Reference Guide:
# https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_python_ref/index.html

# This file is used to demonstrate a working intellisense (code completion) for 
# writing NXOpen journals using Python

import sys
import math
import re
import NXOpen
import NXOpen.CAE
from typing import List, cast, Optional, Union

the_session: NXOpen.Session = NXOpen.Session.GetSession()
base_part = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow

def main():
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)

    log_file_name: str = the_session.LogFile.FileName
    with open(log_file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # define the regex pattern to look for lines starting with a whitespace followed by "License File Sold To" followed by any number of characters
            regex_pattern = r"\s*License File Sold To.*"
            # if line matches the regex pattern, print the line
            if re.match(regex_pattern, line):
                sold_to: str = line.split(":")[1].strip()
                the_lw.WriteFullline(sold_to)


if __name__ == '__main__':
    main()