from entities import *
import argparse
import os.path

# CONSTANTS and GLOBALS
alarm_list = []
export_lang = Languages.EN

def create_ecodry(rows = 24):
	# TOTAL: 27 alarms
	for row in range(1, rows):
		# COMMUNICATION ALARMS
		alarm_list.append(Row3PRComAlarm(row))
		alarm_list.append(RowTB9ComAlarm(row))
		alarm_list.append(RowFanComAlarm(row))
		alarm_list.append(RowFanBreakerAlarm(row))
		# SERIAL ALARMS of fans
		for fan in range(1, 10):
			alarm_list.append(RowFanErrorAlarm(row, fan))
		# PROBES
		alarm_list.append(RowHighTSEAlarm(row))
		alarm_list.append(RowTAEAlarm(row))
		alarm_list.append(RowTSEAlarm(row))
		alarm_list.append(RowTREAlarm(row))
		alarm_list.append(RowPINEAlarm(row))
		alarm_list.append(RowPOUTEAlarm(row))
		alarm_list.append(RowLTEAlarm(row))
		alarm_list.append(RowPSEAlarm(row))
		alarm_list.append(RowPBE1Alarm(row))
		alarm_list.append(RowPBE2Alarm(row))
		alarm_list.append(RowPBE3Alarm(row))
		alarm_list.append(RowPAEAlarm(row))
		alarm_list.append(RowBWRAlarm(row))
		
def create_circuits():
	pass
	
def create_chiller():
	pass
	
def create_multistage():
	pass

def create_standards():
	# TODO SPRUZZI FILA 1
	# TODO SDP POMPE
	# TODO CAZZATE ALLA FINE DELL'EXCEL
	pass
		
def export(where):
	XML = """
	<?xml version="1.0" encoding="UTF-8" ?>
	<ALARMS>
	%s
	</ALARMS>"""
	content = ''
	for alarm in alarm_list:
		content += alarm.XML(export_lang)
	with open(where, 'w') as outfile:
		output = XML%content # FIXME replace & with UTF-8 value
		outfile.write(output.encode('utf-8')) 
		outfile.close()
	print "Done! Check the file", where
	
def get_output(original):
	return os.path.dirname(original) + "/alarms.xml"

		
	
############
#   MAIN   #
############
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Create a xml alarms file using translation excel file')
	parser.add_argument('filename', type=str, help='input xlsx file')
	parser.add_argument('-page', type=int, required=True, help='index of the page containing alarms (it starts from 0)')
	parser.add_argument('-lang', type=str, required=True, help='chosen language')
	parser.add_argument('-output', type=str, required=False, help='xml target file')
	args = parser.parse_args()
	open_file_at_page(args.filename, args.page)
	from excel import open_page as sheet
	if sheet:
		print "Creating alarms..."
		create_ecodry()
		create_circuits()
		create_chiller()
		create_multistage()
		create_standards()
		# TODO: setup export_lang
		print "Alarms created. Saving results"
		where = args.output if args.output is not None else get_output(args.filename)
		export(where)
