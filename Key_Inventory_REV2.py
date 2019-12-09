from __future__ import print_function
import argparse
import subprocess
import os
import collections

#Core Number Mapping
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
            'mz9188':'na'}



# Defines style of print
class style:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

#Prints room #, Key #, and calls for the first and last name of the Key Holders
def displaykeyinfo(userinfo, listnames):
    print("")
    print(style.BOLD + '---------------------------------')
    print('             RESULTS             ')
    print('---------------------------------' + style.END)
    print(style.BOLD + 'Room: ' + style.END + userinfo[14])
    print(style.BOLD + 'Key #: ' + style.END + userinfo[15])
    if listnames == 'y':
        print(style.BOLD+'---------------------------------')
        print("           KEY HOLDERS           ")
        print("---------------------------------"+style.END)
        printkeyholderinfo(userinfo)
    return

#Defines First and Last Name of Key Holder
def printkeyholderinfo(userinfo):
    print(style.BOLD+ "Key Holder: " + style.END + userinfo[10] + " " + userinfo[11])
    return

# Prints Name, email, key number, and key id number.
def displayuserinfo(userinfo):
    print("")
    #print(style.BOLD+"---------------------------------")
    #print("             RESULTS             ")
    print("---------------------------------"+ style.END)
    print(style.BOLD + "First Name: " + style.END + userinfo[10])
    print(style.BOLD + "Last Name: " + style.END + userinfo[11])
    print(style.BOLD + "Key Holder Email: " + style.END + userinfo[12])
    print(style.BOLD + "---------------------------------")
    print("          KEYS ASSIGNED          ")
    print("     Key #  : Key ID : Room #" )
    print("---------------------------------" + style.END)
    return

#Defines key number and key id number information.
def printkeyidinfo(userinfo):
    print(style.BOLD + "Key: " + style.END + userinfo[15] + " : " + userinfo[16] + " : " + userinfo[14])
    return

def printinventoryinfo(userinfo1):
    print(style.BOLD + "---------------------------------")
    print("    KEY INVENTORY INFORMATION    ")
    print("---------------------------------" + style.END)
    print(style.BOLD + 'Box #: ' + style.END + (userinfo1[3]))
    print(style.BOLD + 'Core #: ' + style.END + (userinfo1[1]))
    print(style.BOLD + 'Total Keys: ' + style.END + (userinfo1[6]), end='')
    print(style.BOLD + 'Keys Assigned: ' + style.END, (keycount))
    print(style.BOLD + 'Keys In Stock: ' + style.END, (int(userinfo1[6])-(int(keycount))))
    print(style.BOLD + "---------------------------------" + style.END)
    return

def printboxinfo(userinfo1):
    print(style.BOLD + "---------------------------------")
    print("    BOX NUMBER INFORMATION    ")
    print("---------------------------------" + style.END)
    print(style.BOLD + 'Box #: ' + style.END + (userinfo1[3]))
    print(style.BOLD + 'Key #: ' + style.END + (userinfo1[0]))
    print(style.BOLD + 'Core #: ' + style.END + (userinfo1[1]))
    print(style.BOLD + 'Room #: ' + style.END + (userinfo1[2]))
    print(style.BOLD + 'Total Keys: ' + style.END + (userinfo1[6]), end='')
    print(style.BOLD + 'Keys Assigned: ' + style.END, (keycount))
    print(style.BOLD + 'Keys In Stock: ' + style.END, (int(userinfo1[6]) - (int(keycount))))
    print(style.BOLD + "---------------------------------" + style.END)
    return


# Defines argparse for filename 1 and 2 ( REX .CSV File and Key_Inventory_Total_Master.CSV file)
parser = argparse.ArgumentParser(description='Import File.')
parser.add_argument('filename1', metavar='filename1', type=file, help='Use exported .csv file from REX')
parser.add_argument('filename2', metavar='filename2', type=file, help='Use Key_Inventory_Total.xls')
args = parser.parse_args()
rows = args.filename1.readlines()
rows1 = args.filename2.readlines()
keynumber = ""

rows = map((lambda line:line.split(',')), rows)
key_dict = collections.defaultdict(list)
for key in rows:
    key_dict[(key[10].lower(),key[11].lower())].append(key)


# Defines Main Menu and Options
while keynumber != "quit":
    #mac
    subprocess.call('clear')

    #windows
    #os.system('cls')

    print(style.BOLD +"---------------------------------")
    print("         KEY SEARCH MENU         ")
    print("---------------------------------")
    print(" 1: Search by Name")
    print(" 2: Search by Room Number")
    print(" 3: Search by Key Number")
    print(" 4: Search by Box Number")
    print(" 5: Quit")
    print("---------------------------------" + style.END)
    print("")

    menuchoice = raw_input("Enter Command: ")
    if menuchoice == "5":
        print(style.BOLD +'Goodbye.' + style.END)
        break
    elif menuchoice == "1":
        firstname = raw_input("Enter First Name: ")
        firstname = firstname.lower()
        lastname = raw_input("Enter Last Name: ")
        lastname = lastname.lower()
        if (firstname == '') and (lastname == ''):
            continue

# Reads .csv file and searches for data associated with name searched.
        keycount = 0
        entryfound = False
        for name in key_dict:
            if(firstname == name[0] or (firstname == '')) and ((lastname == name[1]) or (lastname == '')):
                entryfound = True
                displayuserinfo(key_dict[name][0])
                for key in key_dict[name]:
                    printkeyidinfo(key)

# Message when name is not found.
        if entryfound == False:
            print(style.BOLD +"Sorry, Name Not Found" + style.END)
        else:
            print(style.BOLD + "---------------------------------" +style.END)

    elif menuchoice == "2":
        roomnumber = raw_input("Enter Room #: ")
        roomnumber = roomnumber.lower()

# Reads .csv file and searches for data associated with room number searched.
        listnames = raw_input("List Key Holder Information? (Y/[N]): ")
        listnames = listnames.lower()
        keycount = 0
        entryfound = False
        for userinfo in rows:
            if (userinfo[14].lower() == (roomnumber or roomnumber.lower())):
                keycount += 1
                if (entryfound == False):
                    displaykeyinfo(userinfo, listnames)
                else:
                    if listnames == "y":
                        printkeyholderinfo(userinfo)
                entryfound = True

# Message when Room Number is not found.
        if entryfound == False:
            print(style.BOLD + "Sorry, Room Number Not Found" + style.END)
        else:
            for line in rows1:
                userinfo1 = line.split(',')
                if (userinfo1[2].lower() == (roomnumber or roomnumber.lower())):
                    printinventoryinfo(userinfo1)

    elif menuchoice == "3":
        keynumber = raw_input("Key #: ")
        keynumber = keynumber.lower()
        if keynumber in core_map.keys():
            core_map[keynumber]
            corenumber = core_map[keynumber].lower()

# Reads .csv file and searches for data associated with room number searched.
        listnames = raw_input("List Key Holder Information? (Y/[N]): ")
        listnames = listnames.lower()
        keycount = 0
        entryfound = False
        for userinfo in rows:
            if (userinfo[15].lower() == ((keynumber or keynumber.lower()) or (corenumber))):
                keycount += 1
                if (entryfound == False):
                    displaykeyinfo(userinfo, listnames)
                else:
                    if listnames == "y":
                        printkeyholderinfo(userinfo)
                entryfound = True

# Message when Room Number is not found.
        if entryfound == False:
            print(style.BOLD + "Sorry, Room Number Not Found" + style.END)
        else:
            for line in rows1:
                userinfo1 = line.split(',')
                if (userinfo1[0].lower() == (keynumber or keynumber.lower())):
                    printinventoryinfo(userinfo1)
    elif menuchoice == "4":
        boxnumber = raw_input("Enter Box #: ")
        boxnumber = boxnumber.lower()
        for line in rows1:
            userinfo1 = line.split(',')
            if (userinfo1[3].lower() == (boxnumber or boxnumber.lower())):
                keycount = 0
                for userinfo in rows:
                    if (userinfo[15].lower() == userinfo1[0].lower()):
                        keycount += 1
                printboxinfo(userinfo1)

    else:
        print(style.BOLD + "Invalid Command" + style.END)
        raw_input("Press Enter to Return to Main Menu")
        continue

    raw_input("Press Enter to Continue")

args.filename1.close()
args.filename2.close()
