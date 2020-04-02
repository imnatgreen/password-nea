import re, random, string


def checkPass():
    passToCheck = input("Enter a password to check: ")
    try:
        if re.fullmatch(r'[A-Za-z0-9!$%^&*()\-_=+]+', passToCheck) is None:
            raise ValueError
        if len(passToCheck) < 8 or len(passToCheck) > 24:
            raise ValueError
        print("Your password is " + calcPoints(passToCheck)[1] + " (" +
              str(calcPoints(passToCheck)[0]) + " points)\n")
    except:
        print("Password was not valid, returning to menu.\n")


def calcPoints(password):
    points = 0
    row1 = "qwertyuiop"
    row2 = "asdfghjkl"
    row3 = "zxcvbnm"
    contents = {"AZ": False, "az": False, "09": False, "Sm": False}
    contents["AZ"] = True if re.search(r'[A-Z]',
                                       password) is not None else False
    contents["az"] = True if re.search(r'[a-z]',
                                       password) is not None else False
    contents["09"] = True if re.search(r'[0-9]',
                                       password) is not None else False
    contents["Sm"] = True if re.search(r'[!$%^&*()\-_=+]',
                                       password) is not None else False
    for i in contents:
        if contents[i] == True: points += 5
    if points >= 20: points += 5
    if re.fullmatch(r'[A-Za-z]+', password): points -= 5
    if re.fullmatch(r'[0-9]+', password): points -= 5
    if re.fullmatch(r'[!$%^&*()\-_=+]+', password): points -= 5

    for i in range(0, (len(password) - 3)):
        testStr = password[i:i + 3].lower()
        if re.search(rf'{re.escape(testStr)}', row1) is not None: points -= 5
        if re.search(rf'{re.escape(testStr)}', row2) is not None: points -= 5
        if re.search(rf'{re.escape(testStr)}', row3) is not None: points -= 5
    strength = "strong" if points > 20 else "weak" if points <= 0 else "medium"
    rtrn = [points, strength]
    return (rtrn)


def genPass():
    strength = "weak"
    symbols = "!$%^&*()-_=+"
    while strength != "strong":
        genPass = ''.join(
            random.choices(string.ascii_letters + string.digits + symbols,
                           k=random.randint(8, 12)))
        strength = calcPoints(genPass)[1]
    print("Your new password is: " + genPass + " (" +
          str(calcPoints(genPass)[0]) + " points)\n")


while True:
    print("Welcome, please choose an option:")
    print("[1] Check Password")
    print("[2] Generate Password")
    print("[3] Quit")
    option = 0
    while option == 0:
        optTemp = input("(1/2/3) >> ")
        try:
            if optTemp[0] == "1" or optTemp[0].lower() == "c":
                option = 1
            elif optTemp[0] == "2" or optTemp[0].lower() == "g":
                option = 2
            elif optTemp[0] == "3" or optTemp[0].lower() == "q":
                option = 3
            else:
                raise (ValueError)
        except:
            print("Invalid input, try again")
    print("\n\n\n\n\n\n\n\n\n\n")
    if option == 1:
        checkPass()
    if option == 2:
        genPass()
    if option == 3:
        print("Goodbye, exiting...")
        break