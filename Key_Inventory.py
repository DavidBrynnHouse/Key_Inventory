from __future__ import print_function
import argparse
import subprocess

# Defines style of print
class style:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

#Prints room #, Key #, and calls for the first and last name of the Key Holders
def displaykeyinfo(userinfo):
    print("")
    print(style.BOLD + '---------------------------------')
    print('             RESULTS             ')
    print('---------------------------------' + style.END)
    print(style.BOLD + 'Room: ' + style.END + userinfo[14])
    print(style.BOLD + 'Key #: ' + style.END + userinfo[15])
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
    print(style.BOLD+"---------------------------------")
    print("             RESULTS             ")
    print("---------------------------------"+ style.END)
    print(style.BOLD + "First Name: " + style.END + userinfo[10])
    print(style.BOLD + "Last Name: " + style.END + userinfo[11])
    print(style.BOLD + "Key Holder Email: " + style.END + userinfo[12])
    print(style.BOLD + "---------------------------------")
    print("          KEYS ASSIGNED          ")
    print("---------------------------------" + style.END)
    printkeyidinfo(userinfo)
    return

#Defines key number and key id number information.
def printkeyidinfo(userinfo):
    print(style.BOLD + "Key #: " + style.END + userinfo[15] + " - " + userinfo[16])
    return

def printinventoryinfo(userinfo1):
    print(style.BOLD + "---------------------------------")
    print("    KEY INVENTORY INFORMATION    ")
    print("---------------------------------" + style.END)
    print(style.BOLD + 'Box #: ' + style.END + (userinfo1[2]))
    print(style.BOLD + 'Total Keys: ' + style.END + (userinfo1[5]), end ='')
    print(style.BOLD + 'Keys Assigned: ' + style.END, (keycount))
    print(style.BOLD + 'Keys In Stock: ' + style.END, (int(userinfo1[5])-(int(keycount))))
    print(style.BOLD + "---------------------------------" + style.END)
    return

def printboxinfo(userinfo1):
    print(style.BOLD + "---------------------------------")
    print("    BOX NUMBER INFORMATION    ")
    print("---------------------------------" + style.END)
    print(style.BOLD + 'Box #: ' + style.END + (userinfo1[2]))
    print(style.BOLD + 'Key #: ' + style.END + (userinfo1[0]))
    print(style.BOLD + 'Room #: ' + style.END + (userinfo1[1]))
    print(style.BOLD + 'Total Keys: ' + style.END + (userinfo1[5]), end = '')
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

# Defines Main Menu and Options
while keynumber != "quit":
    subprocess.call('clear')
    print(style.BOLD +"---------------------------------")
    print("         KEY SEARCH MENU         ")
    print("---------------------------------")
    print(" 1: Search by Name")
    print(" 2: Search by Room Number")
    print(" 3: Search by Key Number")
    print(" 4: Search by Box Number")
    print(" 5: Return to Main Menu")
    print(" 6: Quit")
    print("---------------------------------" + style.END)
    print("")

    menuchoice = raw_input("Enter Command: ")
    if menuchoice == "6":
        print(style.BOLD +'Goodbye.' + style.END)
        break
    elif menuchoice == "1":
        firstname = raw_input("Enter First Name: ")
        firstname = firstname.lower()

        if firstname == "5":
            continue
        else:
            lastname = raw_input("Enter Last Name: ")
            lastname = lastname.lower()

            if lastname == "5":
                continue
# Reads .csv file and searches for data associated with name searched.
        keycount = 0
        entryfound = False
        for line in rows:
            userinfo = line.split(',')
            if (userinfo[10].lower() == (firstname or firstname.lower()) and (
                userinfo[11].lower() == (lastname or lastname.lower()))):
                keycount += 1
                if (entryfound == False):
                    displayuserinfo(userinfo)
                else:
                    printkeyidinfo(userinfo)
                entryfound = True

                # Message when name is not found.
        if entryfound == False:
            print(style.BOLD +"Sorry, Name Not Found" + style.END)
        else:
            print(style.BOLD + "---------------------------------" +style.END)

    elif menuchoice == "2":
        roomnumber = raw_input("Enter Room #: ")
        roomnumber = roomnumber.lower()
        if roomnumber == "5":
            continue
        else:
# Reads .csv file and searches for data associated with room number searched.
                keycount = 0
                entryfound = False
                for line in rows:
                    userinfo = line.split(',')
                    if (userinfo[14].lower() == (roomnumber or roomnumber.lower())):
                        keycount += 1
                        if (entryfound == False):
                            displaykeyinfo(userinfo)
                        else:
                            printkeyholderinfo(userinfo)
                        entryfound = True

# Message when Room Number is not found.
                if entryfound == False:
                    print(style.BOLD + "Sorry, Room Number Not Found" + style.END)
                else:
                    for line in rows1:
                        userinfo1 = line.split(',')
                        if (userinfo1[1].lower() == (roomnumber or roomnumber.lower())):
                            printinventoryinfo(userinfo1)

    elif menuchoice == "3":
        keynumber = raw_input("Key #: ")
        keynumber = keynumber.lower()
        if keynumber == "5":
            continue
        else:

# Reads .csv file and searches for data associated with room number searched.
                keycount = 0
                entryfound = False
                for line in rows:
                    userinfo = line.split(',')
                    if (userinfo[15].lower() == (keynumber or keynumber.lower())):
                        keycount += 1
                        if (entryfound == False):
                            displaykeyinfo(userinfo)
                        else:
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
        if boxnumber == "q":
            continue
        else:

            for line in rows1:
                userinfo1 = line.split(',')
                if (userinfo1[2].lower() == (boxnumber or boxnumber.lower())):
                    printboxinfo(userinfo1)




    elif menuchoice == "5":
        print(style.BOLD + "You are already in the Main Menu" + style.END)
        raw_input("Press Enter to Continue")
        continue

    else:
        print(style.BOLD + "Invalid Command" + style.END)
        raw_input("Press Enter to Return to Main Menu")
        continue

    raw_input("Press Enter to Continue")
args.filename1.close()
args.filename2.close()