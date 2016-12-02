from entities import *
import argparse
import os.path

# CONSTANTS and GLOBALS
alarm_list = []
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


def create_alarms():
    print "Creating alarms..."

    for al in range(0,37):
        alarm_list.append(
            RCSAlarm(ident_number=al+1, name=2+al*3, desc=3+al*3, help=4+al*3)
        )

    for al in range(1,13):
        alarm_list.append(
            RCSAlarmProbe(number=al, starting_ident_number=37, name=113, desc=114, help=115)
        )

    for al in range(1,10):
        alarm_list.append(
            RCSAlarmProbe(number=al, starting_ident_number=49, name=116, desc=117, help=118)
        )

    alarm_list.append(
        RCSAlarmProbe(number=1, starting_ident_number=58, name=119, desc=120, help=121)
    )

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
