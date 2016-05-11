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
		alarm_list.append(RowSerialComAlarm(row))
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
	for circuit in ['A','B','C','D']:
		# 20 alarms + 6 vfd + 6/8 onoff: 32/34 alarms
		alarm_list.append(Circuit3PRComAlarm(circuit))
		alarm_list.append(CircuitTB9ComAlarm(circuit))
		alarm_list.append(CircuitSerialComAlarm(circuit))
		alarm_list.append(WaterOnAlarm(circuit))
		alarm_list.append(WaterOffAlarm(circuit))
		alarm_list.append(WaterResetAlarm(circuit))
		alarm_list.append(CircuitRefillAlarm(circuit))
		alarm_list.append(CircuitHTSAAlarm(circuit))
		alarm_list.append(CircuitPumpsDeltaPWAlarm(circuit))
		alarm_list.append(CircuitPumpsDeltaPAlarm(circuit))
		alarm_list.append(CircuitPumpsHPSAlarm(circuit))
		alarm_list.append(CircuitFilterDropWAlarm(circuit))
		alarm_list.append(CircuitFilterDropAlarm(circuit))
		alarm_list.append(CircuitPumpServAlarm(circuit))
		alarm_list.append(CircuitTSAlarm(circuit))
		alarm_list.append(CircuitTRAlarm(circuit))
		alarm_list.append(CircuitPSAlarm(circuit))
		alarm_list.append(CircuitLTAlarm(circuit))
		alarm_list.append(CircuitFINAlarm(circuit))
		alarm_list.append(CircuitFOUTAlarm(circuit))
		if circuit == 'A' or circuit == 'B':
			onoff = 8
		else:
			onoff = 6
		vfd = 6
		for pump in range(1, onoff+1):
			alarm_list.append(CircuitONOFFAlarm(circuit, pump))
		for pump in range(1, vfd+1):
			alarm_list.append(CircuitVFDAlarm(circuit, pump))
	
def create_chiller():
	alarm_list.append(NonserialAlarm(ident='A07_COM', name=196, desc=197, help=198, group='CENTRAL CHILLER', reset='AUTO', what='ALARM', page='_none_', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='W07_COM', name=199, desc=200, help=201, group='CENTRAL CHILLER', reset='AUTO', what='WARNING', page='chiller_pid.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='E07_COM', name=202, desc=203, help=204, group='CENTRAL CHILLER', reset='AUTO', what='WARNING', page='_none_', cond='LOGIC', regtype='HOLDING_REGISTER'))
	
	alarm_list.append(NonserialAlarm(ident='W07_TSH', name=205, desc=206, help=207, group='CENTRAL CHILLER', reset='AUTO', what='WARNING', page='chiller_pid.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A07_TSH', name=208, desc=209, help=210, group='CENTRAL CHILLER', reset='MANUAL', what='ALARM', page='chiller_pid.qml', cond='PROBE'))
	alarm_list.append(NonserialAlarm(ident='A07_TRH', name=211, desc=212, help=213, group='CENTRAL CHILLER', reset='MANUAL', what='ALARM', page='chiller_pid.qml', cond='PROBE'))
	alarm_list.append(NonserialAlarm(ident='A07_TAH', name=214, desc=215, help=216, group='CENTRAL CHILLER', reset='MANUAL', what='ALARM', page='chiller_pid.qml', cond='PROBE'))
	
	for chiller in range(1, 7):
		for alarm in range(1, 7):
			alarm_list.append(ChillerAlarm(chiller, alarm))
	
def create_multistage():
	# TODO
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
	alarm_list.append(NonserialAlarm(ident='A05_COM', name=148, desc=149, help=150, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A05_LWL', name=151, desc=152, help=153, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A05_LWS', name=154, desc=155, help=156, group='CIRCUIT SDP', reset='PASSWORD', what='ALARM', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A05_LWR', name=157, desc=158, help=159, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='W05_REF', name=160, desc=161, help=162, group='CIRCUIT SDP', reset='PASSWORD', what='WARNING', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A05_LTE', name=163, desc=164, help=165, group='CIRCUIT SDP', reset='PASSWORD', what='ALARM', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A05_LED', name=166, desc=167, help=168, group='CIRCUIT SDP', reset='AUTO', what='ALARM', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A05_HED', name=169, desc=170, help=171, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='W05_PSR', name=172, desc=173, help=174, group='CIRCUIT SDP', reset='MANUAL', what='WARNING', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='W05_RTS', name=175, desc=176, help=177, group='CIRCUIT SDP', reset='MANUAL', what='WARNING', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='W05_TSR', name=178, desc=179, help=180, group='CIRCUIT SDP', reset='MANUAL', what='WARNING', page='ecodry_selfdrain_page.qml', cond='LOGIC'))
	alarm_list.append(NonserialAlarm(ident='A05_TER', name=181, desc=182, help=183, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='PROBE'))
	alarm_list.append(NonserialAlarm(ident='A05_TSR', name=184, desc=185, help=186, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='PROBE'))
	alarm_list.append(NonserialAlarm(ident='A05_PSR', name=187, desc=188, help=189, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='PROBE'))
	alarm_list.append(NonserialAlarm(ident='A05_LTR', name=190, desc=191, help=192, group='CIRCUIT SDP', reset='MANUAL', what='ALARM', page='ecodry_selfdrain_page.qml', cond='PROBE'))
	
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
		output = xml_file_template%content
		# replace unwanted ampersands...
		output = output.replace('&', '&amp;')
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
	parser.add_argument('filename', type=str, help='translations input xlsx file')
	parser.add_argument('-page', type=str, required=True, help='title of the page containing the translations')
	parser.add_argument('-lang', type=str, required=True, help='chosen language')
	parser.add_argument('-output', type=str, required=False, help='xml target file')
	args = parser.parse_args()
	export_lang = string_to_lang(args.lang)
	if export_lang is not None:
		open_file_at_page(args.filename, args.page)
		from excel import open_page as sheet
		if sheet:
			print "Creating alarms..."
			create_standards()
			create_ecodry()
			create_circuits()
			create_chiller()
			create_multistage()
			print "Alarms created. Saving results"
			where = args.output if args.output is not None else get_output(args.filename)
			export(where)
