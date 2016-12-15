from entities import *
import argparse
import os.path

# CONSTANTS and GLOBALS
alarm_list = []

# the PEMS identifier (bit position)
bit_position = 0

# the row of "name" in excel translations file
translation = 2

export_lang = Languages.EN


def export(where):
    print "Saving results"
    content = ''
    for alarm in alarm_list:
        content += alarm.XML(export_lang)
    with open(where, 'w') as outfile:
        output = xml_file_template % content
        # replace unwanted ampersands...
        output = output.replace('&', '&amp;')
        outfile.write(output.encode('utf-8'))
        outfile.close()
    print "Done! Check the file", where


def get_output(original):
    return os.path.dirname(os.path.realpath(original)) + "/alarms.xml"


def add_one_zone_alarm(type='ALARM', condition='LOGIC'):
    global  bit_position
    global translation
    alarm_list.append(RCSAlarm(bit=bit_position, name=translation, desc=translation + 1, help=translation + 2, zone_number=1, type=type, condition=condition))
    bit_position += 1
    translation += 3


def add_two_zone_alarm(type='ALARM', condition='LOGIC'):
    global  bit_position
    global translation
    alarm_list.append(RCSAlarm(bit=bit_position, name=translation, desc=translation + 1, help=translation + 2, zone_number=1, type=type, condition=condition))
    bit_position += 1
    alarm_list.append(RCSAlarm(bit=bit_position, name=translation, desc=translation + 1, help=translation + 2, zone_number=2, type=type, condition=condition))
    bit_position += 1
    translation += 3


def add_no_zone_alarm(type='ALARM', condition='LOGIC'):
    global  bit_position
    global translation
    alarm_list.append(RCSAlarm(bit=bit_position, name=translation, desc=translation + 1, help=translation + 2, type=type, condition=condition))
    bit_position += 1
    translation += 3


def add_probes_alarm():
    global  bit_position
    global translation
    for al in range(1, 13):
        alarm_list.append(
            RCSAlarmProbe(number=al, probe='T', bit=bit_position, name=translation, desc=translation + 1, help=translation + 2))
        bit_position += 1
    for al in range(1, 10):
        alarm_list.append(
            RCSAlarmProbe(number=al, probe='P', bit=bit_position, name=translation, desc=translation + 1, help=translation + 2))
        bit_position += 1
    alarm_list.append(
        RCSAlarmProbe(number=1, probe='S', bit=bit_position, name=translation, desc=translation + 1, help=translation + 2))


def create_alarms():
    print "Creating alarms..."

    # LOW WATER LEVEL ZONE {zone}
    add_two_zone_alarm()

    # PD - HIGH ZONE {zone}
    add_two_zone_alarm()

    # PS - HIGH ZONE {zone}
    add_two_zone_alarm()

    # WARNING TEMPERATURE PROCESS TS ZONE {zone}
    add_two_zone_alarm(type='WARNING')

    # CHECK POLARITY OF THREEPHASE SUPPLY
    add_no_zone_alarm()

    # PD - LOW ZONE {zone}
    add_two_zone_alarm()

    # OVERLOAD PROCESS PUMP ZONE {zone}
    add_two_zone_alarm()

    # TEMPERATURE SWITCH HEATER ZONE {zone}
    add_two_zone_alarm()

    # PC -HIGH
    add_no_zone_alarm()
    
    # PE - LOW
    add_no_zone_alarm()
    
    # TE - HIGH - HIGH TANK TEMPERATURE
    add_no_zone_alarm()
    
    # OVERLOAD COMPRESSOR
    add_no_zone_alarm()
    
    # OVERLOAD CIRCULATING PUMP
    add_no_zone_alarm()
    
    # ANTIFREEZE SAFETY
    add_no_zone_alarm()
    
    # OVERLOAD FAN
    add_no_zone_alarm()
    
    # COMPRESSOR THERMISTORS
    add_no_zone_alarm()
    
    # HIGH PRESSURE SWITCH
    add_no_zone_alarm()
    
    # FLOWMETER ZONE {zone}
    add_two_zone_alarm()
    
    # OVERLOAD SECOND COMPRESSOR ZONE 1
    add_one_zone_alarm()
    
    # SECOND COMPRESSOR THERMISTORS ZONE 1
    add_one_zone_alarm()
    
    # PROCESS WATER FLOW ZONE {zone}
    add_two_zone_alarm()
    
    # AUXILIARY ALARM ZONE {zone}
    add_two_zone_alarm()
    
    # EVAPORATOR ANTIFREEZE PROTECTION ZONE 1
    add_one_zone_alarm()
    
    # WARNING OSCILLATIONS ZONE {zone}
    add_two_zone_alarm(type='WARNING')

    # TOO MANY DRAIN PROCEDURES ZONE 1
    add_one_zone_alarm(type='WARNING')

    # CONDENSER FOULING
    add_no_zone_alarm(type='WARNING')

    # BROKEN PROBE {probe}{row}
    add_probes_alarm()

    print "Alarms created."


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
            create_alarms()
            where = args.output if args.output is not None else get_output(args.filename)
            export(where)
