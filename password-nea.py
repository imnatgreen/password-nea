import re


def menu():
    print("Welcome, please choose an option:")
    print("[1] Check Password")
    print("[2] Generate Password")
    print("[3] Quit")
    option = 0
    while option == 0:
        optTemp = input("(1/2/3) >> ")
        try:
            if optTemp[0] == "1" or optTemp[0].lower() == "a":
                option = 1
            elif optTemp[0] == "2" or optTemp[0].lower() == "b":
                option = 2
            elif optTemp[0] == "3" or optTemp[0].lower() == "c":
                option = 3
            else:
                raise (ValueError)
        except:
            print("Invalid input, try again")
    if option == 1:
        checkPass()
    #if option == 2:
    #    genPass()


def checkPass():
    passToCheck = input("Enter a password to check: ")
    try:
        if re.fullmatch(r'[A-Za-z0-9!$%^&*()\-_=+]+', passToCheck) is None:
            raise ValueError
        if len(passToCheck) < 8 or len(passToCheck) > 24:
            raise ValueError
    except:
        print("Password was not valid, returning to menu.\n")
        menu()


menu()