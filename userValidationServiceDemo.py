import time
import validateUser as service

##################################################
# in same folder contain:
# Your code as shown with this demo python script
# and the validateUser.py script
# structure similar to this demo for
##################################################
if __name__ == "__main__":

    service.launchService()

    userId = input("Enter a User ID: ")

    passWrd = input("Enter a password: ")

    ######################################################
    # Check to see if Micro Service is ready("waiting...")
    ######################################################
    with open("loginUser.txt", "r") as userLoggingIn:
        user = userLoggingIn.read().split(" ")

        # print(f"in Read....   {user}")
        while user[0] != "waiting...":
            time.sleep(1)
            user = userLoggingIn.read().split()
            # print(user)

    userLoggingIn.close()

    ##################################################
    # Build string of UserID and passWord to write to the login file
    ##################################################
    outstring = userId + " " + passWrd

    ######################################################
    # write UserID and UserPW into the login file to launch the MicroService Action
    ######################################################
    with open("loginUser.txt", "w") as logger:
        logger.write(outstring)
        logger.close()

    ######################################################
    # read the MicroService Communication file to see results of Login Attempt
    ######################################################
    time.sleep(1)
    with open("validUserResponse.txt", "r") as errorCheck:
        errorMsg = errorCheck.read().split(" ")
        if errorMsg[0] == userId:
            # verifyAge(userId)# Other Microservice call
            print(f"Welcome {userId}, you are now logged in!")
            pwInvalid = False
        elif errorMsg[0] == "Invalid":
            print(f"Sorry that Password is invalid, Please try again.")
        else:
            # verifyAge(userId)# Other Microservice call
            print(f" ...Welcome New User: {userId}")
            pwInvalid = False
        errorCheck.close()
