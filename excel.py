import xlrd
import enum

open_page = None # declared here

def open_file_at_page(path, page):
	print "Opening file", path, "at page", page
	global open_page
	try:
		print "..."
		myfile = xlrd.open_workbook(path)
		open_page = myfile.sheet_by_index(page)
		print "Done"
	except Exception as ex:
		print "Error opening the excel file: ", ex.message
		open_page = "ERROR"

def value_at(row, col):
	return open_page.cell_value(row, col)

class Languages(enum.Enum):
	EN = 0
	IT = 4
	JA = 5
	ZH = 6
	DE = 7
	ES = 8
	PO = 9
	FR = 10
