import xlrd
import enum

# Functions to extract strings from the 3PR Translations.xlsx file

open_page = None # declared here
error_string = "__ERROR__"

# page = string, title of the page
def open_file_at_page(path, page):
	print "Opening file", path, "at page", page
	global open_page
	try:
		print "..."
		myfile = xlrd.open_workbook(path)
		open_page = myfile.sheet_by_name(page)
		print "Done"
	except Exception as ex:
		print "Error opening the excel file: ", ex.message

# return the direct cell's value (str, int, float...)
def value_at(row, col):
	if row < 2 or row > open_page.nrows:
		return error_string
	elif col < 0 or col > open_page.ncols:
		return error_string
	else:
		return open_page.cell_value(row-1, col)

class Languages(enum.Enum):
	EN = 0
	IT = 4
	JA = 5
	ZH = 6
	DE = 7
	ES = 8
	PO = 9
	FR = 10
	
def string_to_lang(langstr):
	l = langstr.lower()
	if l == 'en':
		return Languages.EN
	elif l == 'it':
		return Languages.IT
	elif l == 'ja':
		return Languages.JA
	elif l == 'zh':
		return Languages.ZH
	elif l == 'de':
		return Languages.DE
	elif l == 'es':
		return Languages.ES
	elif l == 'po':
		return Languages.PO
	elif l == 'fr':
		return Languages.FR
	else:
		print "Language '%s' unknown. Aborting"%l
		return None
