# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# untested
# If you need your Excel file to recalculate during your journal (eg. you are changing values and want to formulas to update)
# Then yo can use xlwings.
# This requires you to have Excel installed on the machine that you are running the journal on.

# Note that xlwings will needs Excel running with the file and thus will start Excel and open that file.

import sys
import math
import NXOpen
import NXOpen.CAE
from typing import List, cast, Optional, Union
import xlwings as xw # pip install xlwings

the_session: NXOpen.Session = NXOpen.Session.GetSession()
base_part = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow


def main():
    the_lw.Open()
    the_lw.WriteFullline("Starting Main() in " + the_session.ExecutingJournal)
 
    file_name = sys.argv[1] # "C:\\temp\\Sample1.xlsx"
    with xw.Book(file_name) as wb:
        sheet = wb.sheets['Sheet1']
        print(sheet['A5'].value) # 15
        sheet['B18'].value = '=sum(B1:B17)'
        print(sheet['A18'].value) # 493

if __name__ == '__main__':
    main()
