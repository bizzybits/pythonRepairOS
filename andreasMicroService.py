import time
import os


###########################################################
# function to create 3 key files
#           "loginUser.txt"
#           "validUserResponse.txt"
#           "validUsers.txt"
# and to
#           preload contents for MicroService Start
###########################################################
def launchService():
    create1 = "loginUser.txt"
    with open(create1, "w") as startUp:
        startUp.write("waiting...")
        path = os.getcwd() + "/" + create1
        print(f"Creating: {path}")
    startUp.close()
    create2 = "validUserResponse.txt"
    with open(create2, "w") as communic:
        communic.write("ready...")
        path = os.getcwd() + "/" + create2
        print(f"Creating: {path}")
    communic.close()
    create3 = "validUsers.txt"
    with open(create3, "w") as repo:
        path = os.getcwd() + "/" + create3
        print(f"Creating: {path}")
    repo.close()
    return


###########################################################
# This function generates the key in a cyclic manner until
# it's length isn't equal to the length of original text
##########################################################
def generateKey(size, keyIn):
    key = list(keyIn)
    if size == len(key):
        return key
    else:
        for i in range(size - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


###########################################################
# encrypted text generated with the help of the key
###########################################################
def cipherText(string1, string2, key):
    cipher_text = []
    cipher_text2 = []
    for i in range(len(string1)):
        rawX = (ord(string1[i]) + ord(key[i])) % 26
        x = rawX + ord('A')
        cipher_text.append(chr(x))

    for i in range(len(string2)):
        rawX2 = (ord(string2[i]) + ord(key[i])) % 26
        x2 = rawX2 + ord('A')
        cipher_text2.append(chr(x2))

    return "".join(cipher_text), "".join(cipher_text2)


###########################################################
# 2 show functions to read and print file contents
###########################################################
def showUsers():
    print("# Displayed for testing purposes # \nEncypted Users...")
    with open("validUsers.txt", "r") as pwFileRead:
        print(pwFileRead.read())


def showLogin():
    print("# Displayed for testing purposes # \nUser Logging in...")
    with open("loginUser.txt", "r") as loginFile:
        data = loginFile.read().split(" ")
        print(data[0])


###########################################################
# function to add user to valid user list in an Encrypted form
###########################################################
def addUser(userid, pw, key):
    with open("validUsers.txt", "a") as pwFile:
        print("Adding User to system ...")
        userC, passwordC = cipherText(userid, pw, key)
        pwFile.write(f"{userC:<12} {passwordC:<12}  => {userid:<12}\n")
    pwFile.close()

    showUsers()


###########################################################
# main validate user function All in an Encrypted state
###########################################################
def validateUser(userId, password):
    #####################################################
    # Build System Encryption Key to become a microService
    keyword = "scuba"
    sysKey = generateKey(max(len(userId), len(password)), keyword)
    #####################################################
    # Encrypt UserID and Password for processing
    #####################################################
    creds1, creds2 = cipherText(userId, password, sysKey)
    #####################################################
    response = ""
    with open("validUsers.txt", "r") as valids:
        data = valids.read().split("\n")
        currentUsers = {}
        for each in data:
            userID = each[0:13].strip(" ")
            userPW = each[12:25].strip(" ")
            currentUsers[userID] = userPW
        if creds1 in currentUsers.keys():
            if creds2 == currentUsers[creds1]:
                response = f"{userId} has been Validated... Welcome."
                print(f"{userId} has been Validated... Welcome.")
            else:
                response = f"Invalid Password, {userId}, Please try again."
                print("Wrong PW")
        else:
            response = "it looks like you are a new user!\n Adding your credentials to our system."
            addUser(userId, password, sysKey)
            print("New User")
        valids.close()
        return response


if __name__ == "__main__":
    thisguy = ""
    print(os.getcwd())
    launchService()
    while True:
        time.sleep(1)
        print(os.curdir)
        ###############################################
        # Check for userID and Password to be validated
        ############################################### # replace with local file path
        with open("loginUser.txt", "r") as checkUser:
            user = checkUser.read().split(" ")
            print("Login File: Status: ", user[0])
            if user[0] != "waiting...":
                showLogin()
                thisguy = validateUser(user[0], user[1])
                print("In Main Microservice: ", thisguy)
        checkUser.close()
        ####################################################
        # Send Result of validation back via file handshake.
        ####################################################
        if len(thisguy) > 0:  # replace with local file path
            with open("validUserResponse.txt", "w") as userResponse:
                userResponse.write(thisguy)
                userResponse.close()
        ##############################################
        # Reset loginUser.txt file by.... writing out "waiting...")
        ############################################## #replace with local file path
        with open("loginUser.txt", "w") as checkUser:
            checkUser.write("waiting...")
        checkUser.close()