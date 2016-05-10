import xlrd, xlwt, xlutils
from entities import *


# CONSTANTS and GLOBALS
open_page = None # open page from a excel workbook

alarm_list = [
#NonserialAlarm(iden, name, desc, help, group, reset, what, page, cond)
] # TODO: fill the list with instance of alarms


for row in range(1, 24):
	alarm_list.append(RowTB9ComAlarm(row))
