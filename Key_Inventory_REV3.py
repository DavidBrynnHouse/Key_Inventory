from __future__ import print_function
import argparse
import subprocess
import collections
import csv
import os
from os import path
from urllib.request import urlopen
from boxsdk import OAuth2
import webbrowser
from boxsdk.util import json
from oauthlib.common import urlencode, Request

core_map = {'mz9000': 'pz1x',
            'mz9001': 'na',
            'mz9002': 'pz3',
            'mz9003': 'pz5',
            'mz9004': 'pz6',
            'mz9006': 'pz8',
            'mz9008': 'pz10',
            'mz9011': 'pz',
            'mz9024': 'pzf1x',
            'mz9025': 'pzf2',
            'mz9026': 'pzf3',
            'mz9027': 'pzf4',
            'mz9028': 'pzf5',
            'mz9032': 'pzf9',
            'mz9190': 'na',
            'mz9036': 'pzf13x',
            'mz9037': 'pzf14',
            'mz9038': 'pzf15',
            'mz9039': 'pzf16',
            'mz9040': 'pzf17',
            'mz9041': 'pzf21x',
            'mz9042': 'pzf22',
            'mz9043': 'pzf23',
            'mz9044': 'pzf24',
            'mz9045': 'pzf',
            'mz9046': 'pze1',
            'mz9047': 'pze2',
            'mz9048': 'pze3',
            'mz9049': 'pze4',
            'mz9050': 'pze5x',
            'mz9051': 'pze6',
            'mz9052': 'pze7',
            'mz9053': 'pze8',
            'mz9054': 'pze9',
            'mz9193': 'pze11',
            'mz9056': 'pze13x',
            'mz9057': 'pze15',
            'mz9058': 'pze16',
            'mz9059': 'pze17',
            'mz9060': 'pze17',
            'mz9061': 'pze21',
            'mz9062': 'pze25x',
            'mz9063': 'pze26',
            'mz9064': 'pze27',
            'mz9065': 'pze28',
            'mz9066': 'pze',
            'mz9067': 'pzd1',
            'mz9068': 'pzd2',
            'mz9069': 'pzd3',
            'mz9070': 'pzd4',
            'mz9071': 'pzd4',
            'mz9072': 'pzd6',
            'mz9073': 'pzd7',
            'mz9074': 'pzd8',
            'mz9075': 'pzd9',
            'mz9076': 'pzd10',
            'mz9077': 'pzd11',
            'mz9079': 'pzd13',
            'mz9080': 'pzd14',
            'mz9081': 'pzd15',
            'mz9085': 'pzd19',
            'mz9095': 'pzd29',
            'mz9096': 'na',
            'mz9097': 'pzd31',
            'mz9098': 'pzd32',
            'mz9099': 'pzd33',
            'mz9100': 'pzd34',
            'mz9101': 'pzd35',
            'mz9102': 'pzd36',
            'mz9103': 'pzd37',
            'mz9104': 'pzd38',
            'mz9105': 'pzd39',
            'mz9106': 'pzd40',
            'mz9107': 'pzd41',
            'mz9108': 'pzd42',
            'mz9110': 'pzd44',
            'mz9111': 'pzd45',
            'mz9112': 'pzd46',
            'mz9113': 'pzd47',
            'mz9114': 'pzd48',
            'mz9115': 'pzd49',
            'mz9116': 'pzd50',
            'mz9117': 'pzd51',
            'mz9118': 'pzd52',
            'mz9120': 'pzd',
            'mz9121': 'pzc1',
            'mz9122': 'pzc2',
            'mz9123': 'pzc3',
            'mz9124': 'pzc4',
            'mz9125': 'pzc5',
            'mz9126': 'pzc',
            'mz9127': 'pzb1',
            'mz9128': 'pzb2x',
            'mz9129': 'pzb3',
            'mz9130': 'pzb4',
            'mz9131': 'pzb5',
            'mz9132': 'pzb',
            'mz9133': 'pza1',
            'mz9136': 'pza4',
            'mz9137': 'pza5',
            'mz9138': 'pza6',
            'mz9139': 'pza7',
            'mz9140': 'pza8',
            'mz9141': 'pza9',
            'mz9142': 'pza10',
            'mz9143': 'pza11',
            'mz9144': 'pza12',
            'mz9145': 'pza13',
            'mz9146': 'pza14',
            'mz9147': 'pza15',
            'mz9148': 'pza',
            'mz9153': 'pze29',
            'mz9154': 'pzf62',
            'mz9157': 'pzc7',
            'mz9158': 'pzc8',
            'mz9162': 'pzc10',
            'mz9163': 'pzc11',
            'mz9164': 'pzc12',
            'mz9189': 'na',
            'mz9166': 'pzd55',
            'mz9167': 'pzf26',
            'mz9168': 'pzc14',
            'mz9169': 'pzd56',
            'mz9171': 'pzd57',
            'mz9172': 'pzd58',
            'mz9191': 'na',
            'mz9174': 'pzd59',
            'mz9175': 'pzc15',
            'mz9176': 'pzo59',
            'mz9177': 'pzc16',
            'mz9178': 'na',
            'mz9179': 'pzd61',
            'mz9180': 'pzd62',
            'mz9181': 'pzd63',
            'mz9182': 'pzd64',
            'mz9184': 'ct15',
            'mz9185': 'na',
            'mz9187': 'pz16x',
            'mz9194': 'pzd66',
            'mz9188': 'na'}


# Defines style of print
class Style:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# Prints room #, Key #, and calls for the first and last name of the Key Holders
def display_key_info(room_number, key_core_number, list_names):
    """
    :param key_core_number: The number that is associated with the displayed key
    :param room_number: The room that is associated with the displayed key
    :param list_names: boolean result which when true lists the names of individuals who have the displayed key
    """
    print("")
    print(Style.BOLD + '---------------------------------')
    print('             RESULTS             ')
    print('---------------------------------' + Style.END)
    print(Style.BOLD + 'Room: ' + Style.END + room_number)
    print(Style.BOLD + 'Key #: ' + Style.END + key_core_number)
    if list_names:
        print(Style.BOLD + '---------------------------------')
        print("           KEY HOLDERS           ")
        print("---------------------------------" + Style.END)


# Defines First and Last Name of Key Holder
def print_key_holder_info(ticket_info):
    """
    :param ticket_info: array of data associated with a single ticket
    """
    first_name = ticket_info[10]
    last_name = ticket_info[11]
    print(Style.BOLD + "Key Holder: " + Style.END + first_name + " " + last_name)


# Prints Name, email, key number, and key id number.
def display_user_info(ticket_info):
    first_name = ticket_info[10]
    last_name = ticket_info[11]
    email = ticket_info[12]
    print("")
    print(Style.BOLD + "---------------------------------")
    print("             RESULTS             ")
    print("---------------------------------" + Style.END)
    print(Style.BOLD + "First Name: " + Style.END + first_name)
    print(Style.BOLD + "Last Name: " + Style.END + last_name)
    print(Style.BOLD + "Key Holder Email: " + Style.END + email)
    print(Style.BOLD + "---------------------------------")
    print("          KEYS ASSIGNED          ")
    print("     Key #  : Key ID : Room #")
    print("---------------------------------" + Style.END)


# Defines key number and key id number information.
def print_key_id_info(user_info):
    print(Style.BOLD + "Key: " + Style.END + user_info[15] + " : " + user_info[16] + " : " + user_info[14])
    return


# Prints Key Inventory Information
def print_inventory_info(key_details):
    print(Style.BOLD + "---------------------------------")
    print("    KEY INVENTORY INFORMATION    ")
    print("---------------------------------" + Style.END)
    print(Style.BOLD + 'Box #: ' + Style.END + (key_details[3]))
    print(Style.BOLD + 'Core #: ' + Style.END + (key_details[1]))
    print(Style.BOLD + 'Total Keys: ' + Style.END + (key_details[6]), end='')
    print(Style.BOLD + 'Keys Assigned: ' + Style.END, key_details[5])
    print(Style.BOLD + 'Keys In Stock: ' + Style.END, key_details[4])
    print(Style.BOLD + "---------------------------------" + Style.END)
    return


# Prints information regarding number and location of keys
def print_box_info(user_info, key_count):
    print(Style.BOLD + "---------------------------------")
    print("    BOX NUMBER INFORMATION    ")
    print("---------------------------------" + Style.END)
    print(Style.BOLD + 'Box #: ' + Style.END + (user_info[3]))
    print(Style.BOLD + 'Key #: ' + Style.END + (user_info[0]))
    print(Style.BOLD + 'Core #: ' + Style.END + (user_info[1]))
    print(Style.BOLD + 'Room #: ' + Style.END + (user_info[2]))
    print(Style.BOLD + 'Total Keys: ' + Style.END + (user_info[6]), end='')
    print(Style.BOLD + 'Keys Assigned: ' + Style.END, key_count)
    print(Style.BOLD + 'Keys In Stock: ' + Style.END, (int(user_info[6]) - (int(key_count))))
    print(Style.BOLD + "---------------------------------" + Style.END)
    return


# Prints the menu for a user to choose from
def print_search_menu():
    print(Style.BOLD + "---------------------------------")
    print("         KEY SEARCH MENU         ")
    print("---------------------------------")
    print(" 1: Search by Name")
    print(" 2: Search by Room Number")
    print(" 3: Search by Key Number")
    print(" 4: Search by Box Number")
    print(" 5: Quit")
    print(" 6: Audit")
    print(" 7: Open Inventory")
    print("---------------------------------" + Style.END)
    print("")


# Code that is run when a user chooses to search by name
def search_by_name():
    first_name = input("Enter First Name: ")
    first_name = first_name.lower()
    last_name = input("Enter Last Name: ")
    last_name = last_name.lower()
    no_value = False
    run = False
    if (first_name == '') and (last_name == ''):
        no_value = True

    # Reads .csv file and searches for data associated with name searched.
    entry_not_found = True
    for name in key_master:
        name = name.split(",")

        if (first_name == name[10].lower() or (first_name == '')) \
                and ((last_name == name[11].lower()) or (last_name == '')):
            entry_not_found = False

            if not run:
                display_user_info(name)

            run = True
            print_key_id_info(name)

    # Message when name is not found.
    if entry_not_found or no_value:
        print(Style.BOLD + "Sorry, Name Not Found" + Style.END)

    else:
        print(Style.BOLD + "---------------------------------" + Style.END)


# Code that is run when a user chooses to  search by room number
def search_by_room_number():
    room_number = input("Enter Room #: ")
    room_number = room_number.lower()
    entry_found = False

    # Reads .csv file and searches for data associated with room number searched.
    list_names = True if input("List Key Holder Information? (Y/[N]): ").lower() == 'y' else False
    key_count = 0

    for row in key_master:
        row = row.split(",")

        if row[14].lower() == (room_number or room_number.lower()):
            entry_found = True

            if key_count is 0:
                display_key_info(row[14], row[15], list_names)

            if list_names:
                print_key_holder_info(row)

            key_count += 1

    for line in key_inventory:
        line = line.split(',')

        if line[2].lower() == (room_number or room_number.lower()):
            print_inventory_info(line)

    if not entry_found:
        print(Style.BOLD + "Sorry, Room Number Not Found" + Style.END)


# Code that is run when a user chooses to search by key number
def search_by_key_number():
    key_core_number = input("Key #: ").lower()
    if key_core_number in core_map.keys():
        core_map[key_core_number]
        core_number = core_map[key_core_number].lower()

    # Reads .csv file and searches for data associated with room number searched.
    list_names = input("List Key Holder Information? (Y/[N]): ")
    list_names = list_names.lower()
    key_count = 0
    entry_found = False
    for row in key_master:
        row = row.split(",")
        if row[15].lower() == ((key_core_number or key_core_number.lower()) or core_number):
            key_count += 1
            if not entry_found:
                display_key_info(row[14], row[15], list_names)
            else:
                if list_names == 'y':
                    print_key_holder_info(row)
            entry_found = True

    # Message when Room Key is not found.
    if not entry_found:
        print(Style.BOLD + "Sorry, Room Key Not Found" + Style.END)
    else:
        for line in key_inventory:
            line = line.split(',')
            if line[0].lower() == (key_core_number or key_core_number.lower()):
                print_inventory_info(line)


# Code that is run when a user chooses to search by box number
def search_by_box_number():
    box_number = input("Enter Box #: ")
    box_number = box_number.lower()
    for line in key_inventory:
        line = line.split(',')
        if line[3].lower() == (box_number or box_number.lower()):
            key_count = 0
            for user_info in key_master:
                if user_info[15].lower() == line[0].lower():
                    key_count += 1
            print_box_info(line, key_count)


# Audits the current number of active keys
def audit_keys():
    run = False
    update_stock = True if input("Do you want to take stock? [y/N] ").lower() == 'y' else False
    with open('Key_Inventory.csv', 'w') as csv_file:
        with open('Low_Keys.csv', 'w') as csv_file_low:
            low_key_file_writer = csv.writer(csv_file_low, delimiter=',')
            file_writer = csv.writer(csv_file, delimiter=',')
            file_writer.writerow(['Key #', 'Core #', 'Room #', 'Box #', '# In Stock', '# Assigned', 'Total'])
            low_key_file_writer.writerow(['Key #', '# Left'])
            for inventory_row in key_inventory:
                inventory_row = inventory_row.split(",")
                key_count = 0
                if run and inventory_row[0] != "end":
                    updated_key = inventory_row[0]
                    for master_row in key_master:
                        master_row = master_row.split(",")
                        if updated_key == master_row[15]:
                            key_count += 1
                    if int(inventory_row[4]) < 2 and 37 < int(inventory_row[3]) < 186:
                        low_key_file_writer.writerow([inventory_row[0], inventory_row[4]])
                    if update_stock and 37 < int(inventory_row[3]) < 186:
                        inventory_row[4] = input("How many keys are left in box " + str(inventory_row[3]) + "? : ")
                    inventory_row[5] = str(key_count)
                    inventory_row[4] = int(inventory_row[6]) - int(inventory_row[5])
                    file_writer.writerow(inventory_row)
                run = True


def open_key_inventory():
    os.system("libreoffice --calc " + path.join(path.dirname(__file__), 'Key_Inventory.csv'))


# Defines argparse for filename 1 and 2 ( REX .CSV File and Key_Inventory_Total_Master.CSV file)
parser = argparse.ArgumentParser(description='Import File.')

parser.add_argument('filename1', metavar='filename1', type=open, help='Use exported .csv file from REX')
parser.add_argument('filename2', metavar='filename2', type=open, help='Use Key_Inventory_Total.xls')
args = parser.parse_args()
key_master = args.filename1.readlines()
key_inventory = args.filename2.readlines()

# rows = map((lambda line: line.split(',')), rows)
key_dict = collections.defaultdict(list)
for key in key_master:
    key_dict[(key[10].lower(), key[11].lower())].append(key)

# Main logic of code
while True:
    # mac
    subprocess.call('clear')

    # windows
    # os.system('cls')

    print_search_menu()

    menu_choice = input("Enter Command: ")

    if menu_choice == "1":
        search_by_name()

    elif menu_choice == "2":
        search_by_room_number()

    elif menu_choice == "3":
        search_by_key_number()

    elif menu_choice == "4":
        search_by_box_number()

    elif menu_choice == "5":
        print(Style.BOLD + 'Goodbye.' + Style.END)
        break

    elif menu_choice == "6":
        audit_keys()

    elif menu_choice == "7":
        open_key_inventory()

    else:
        print(Style.BOLD + "Invalid Command" + Style.END)
        input("Press Enter to Return to Main Menu")
        continue

    input("Press Enter to Continue")

args.filename1.close()
args.filename2.close()
