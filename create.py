from entities import *
import argparse
import os.path

# CONSTANTS and GLOBALS
alarm_list = []
export_lang = Languages.EN

def create_ecodry():
	# TOTAL: 27 alarms
	for row in range(1, 25):
		# COMMUNICATION ALARMS
		alarm_list.append(Row3PRComAlarm(row))
		alarm_list.append(RowTB9ComAlarm(row))
		alarm_list.append(RowFanComAlarm(row))
		alarm_list.append(RowFanBreakerAlarm(row))
		# SERIAL ALARMS of fans
		for fan in range(1, 11):
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
	# SPRAY GROUP
	alarm_list.append(NonserialAlarm(ident='WNS_PBE', name=2, desc=3, help=4, group='SPRAY', reset='MANUAL', what='WARNING', page='ecodry_spray_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='WNS_PAE', name=5, desc=6, help=7, group='SPRAY', reset='MANUAL', what='WARNING', page='ecodry_spray_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='WNS_DRN', name=8, desc=9, help=10, group='SPRAY', reset='MANUAL', what='WARNING', page='ecodry_spray_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='WNS_FPD', name=11, desc=12, help=13, group='SPRAY', reset='MANUAL', what='WARNING', page='ecodry_spray_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='ALS_FPD', name=14, desc=15, help=16, group='SPRAY', reset='MANUAL', what='ALARM', page='ecodry_spray_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='WNS_ADB', name=17, desc=18, help=19, group='SPRAY', reset='PASSWORD', what='WARNING', page='_none_', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='WNS_BST', name=20, desc=21, help=22, group='SPRAY', reset='PASSWORD', what='WARNING', page='_none_', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='WNS_PSE', name=23, desc=24, help=25, group='SPRAY', reset='MANUAL', what='WARNING', page='ecodry_spray_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='ALS_PSE', name=26, desc=27, help=28, group='SPRAY', reset='MANUAL', what='ALARM', page='ecodry_spray_page.qml', cond='LOGIC'))

	# SDP PUMPS
	alarm_list.append(NonserialAlarm(ident='A05_COM', name=149, desc=150, help=151, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A05_LWL', name=152, desc=153, help=154, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A05_LWS', name=155, desc=156, help=157, group='CIRCUIT SDP', reset='PASSWORD', what='ALARM', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A05_LWR', name=158, desc=159, help=160, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='W05_REF', name=161, desc=162, help=163, group='CIRCUIT SDP', reset='PASSWORD', what='WARNING', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A05_LTE', name=164, desc=165, help=166, group='CIRCUIT SDP', reset='PASSWORD', what='ALARM', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A05_LED', name=167, desc=168, help=169, group='CIRCUIT SDP', reset='AUTO', what='ALARM', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A05_HED', name=170, desc=171, help=172, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='W05_PSR', name=173, desc=174, help=175, group='CIRCUIT SDP', reset='MANUAL', what='WARNING', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='W05_RTS', name=176, desc=177, help=178, group='CIRCUIT SDP', reset='MANUAL', what='WARNING', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='W05_TSR', name=179, desc=180, help=181, group='CIRCUIT SDP', reset='MANUAL', what='WARNING', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A05_TER', name=182, desc=183, help=184, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='PROBE'))
	alarm_list.append(NonserialAlarm(ident='A05_TSR', name=185, desc=186, help=187, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='PROBE'))
	alarm_list.append(NonserialAlarm(ident='A05_PSR', name=188, desc=189, help=190, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='PROBE'))
	alarm_list.append(NonserialAlarm(ident='A05_LTR', name=191, desc=192, help=193, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='PROBE'))
	
	# 8 POMPE SDP
	for pump in range(1,9):
		alarm_list.append(SDPumpAlarm(pump))
		
	# COMMUNICATION MODULES
	for module in range(1,4):
		alarm_list.append(PLCCMAlarm(module))
		
def export(where):
	content = ''
	for alarm in alarm_list:
		content += alarm.XML(export_lang)
	with open(where, 'w') as outfile:
		output = xml_file_template%content # FIXME replace & with UTF-8 value
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
		create_standards()
		create_ecodry()
		create_circuits()
		create_chiller()
		create_multistage()
		# TODO: setup export_lang
		print "Alarms created. Saving results"
		where = args.output if args.output is not None else get_output(args.filename)
		export(where)
