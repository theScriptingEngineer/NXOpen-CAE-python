# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# untested
# If you only need to READ data from Excel or WRITE data to Excel, you can use openpyxl.
# This does not require that you have Excel installed on the machine that you are running the journal on

# In case you need to calculate the formulas, but don't have excel installed you can try pycel (limited functionality!)

import sys
import math
import NXOpen
import NXOpen.CAE
from typing import List, cast, Optional, Union
import openpyxl # pip install openpyxl

theSession: NXOpen.Session = NXOpen.Session.GetSession()
basePart = theSession.Parts.BaseWork
theLW: NXOpen.ListingWindow = theSession.ListingWindow


def main():
    theLW.Open()
    theLW.WriteFullline("Starting Main() in " + theSession.ExecutingJournal)
 
    file_name = sys.argv[1] # "C:\\temp\\Sample1.xlsx"
    # opening with the data_only=True option gives the values in case the cell contains a formula.
    wb_object: openpyxl.Workbook = openpyxl.load_workbook(file_name, data_only=True)
    sheet_object = wb_object["Sheet1"]
    value_a5 = sheet_object.cell(row=5, column=1).value
    print(value_a5) # 15

if __name__ == '__main__':
    main()
