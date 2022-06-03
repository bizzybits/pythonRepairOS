import time
import click
import andreasMicroService as svc  #for launch, service runs in own process

from collections import deque


class Item:

    def __init__(self, item_name, issue, date, customer):
        self.item_name = item_name
        self.issue = issue
        self.date = date
        self.customer = customer

    def show_full_item(self):
        """Prints item information."""
        print(''' 
            **************************
             Repair Ticket Validation 
            **************************''')
        print("\nThe item that needs repair is: " + self.item_name)
        print("Customer reports issue with:  " + self.issue)

    @classmethod
    def get_new_repair(cls):
        """Gets information from user and returns the item"""
        while 1:
            try:
                item_name = input("Enter new item for repair: ")
                issue = input("Enter issue to be repaired: ")
                due_date = input("Enter date to be repaired: ")
                customer = input("Enter customer name: ")
                return cls(item_name, issue, due_date, customer)
            except:
                print("Invalid input!")
                continue


def print_repair_ticket(item):
    """Prints repair ticket."""
    print(f"""
           *******************************
           Repair Ticket for {item.item_name}!
           *******************************""")
    print("\nThe item that needs repair is: " + item.item_name)
    print(f"{item.customer} reports issue with: {item.issue} ")
    print(f"{item.item_name} repair is due on {item.date}")


class Service:

    def __init__(self, service_name, price):
        self.service_name = service_name
        self.price = price

    def show_new_service(self):
        """Prints new service menu item information."""
        print(''' 
            ********************
             Service Menu Item
            ********************''')
        print("\nThe new service added is: " + self.service_name)
        print("The new price for the service is:  " + self.price)

    @classmethod
    def get_new_service(cls):
        """Gets new service menu item information from admin."""
        while 1:
            try:
                service_name = input("Enter new service name: ")
                price = input("Enter the new price: ")
                return cls(service_name, price)
            except:
                print("Invalid input!")
                continue


def print_backlog(backlog):
    """Prints mechanic service backlog."""
    print(''' 
            ***********************
             General Service Backlog
            ***********************''')
    print(backlog)


def print_service_menu(service_dict):
    """Prints service menu."""
    print(f"""
           **************
            Service Menu
           **************""")
    for service, price in service_dict.items():
        print(service + " " + price)


def print_repair_ticket(item):
    """Prints repair ticket with item information."""
    print(f"""
           **************
           Repair Ticket for {item.item_name}!
           **************""")
    print("\nThe item that needs repair is: " + item.item_name)
    print(f"{item.customer} reports issue with: {item.issue} ")
    print(f"{item.item_name} repair is due on {item.date}")


def faqs():
    """Prints FAQs."""
    print('''
                            ** Frequently Asked Questions **
                            
                What kind of items can I enter?
                    
                    Any! You decide, the program is designed to be flexible
                    for your needs.
                
                What kind of payments does the software accept?
                    
                    This is up to you -- the payments processing module
                    will be updated to function in an upcoming software
                    update release.
                    
                What if everything freezes?
                
                    Turn it off then turn it off again.
                    
                More questions will be added as features roll out.
                    
          ''')


def documentation():
    """Prints general documentation."""
    print('''
                            ** General Documentation **
                RepairOS is a helpful software program that allows you to 
                manage your repair shop's intake and payment processes.
                
                When you select 1 at the main menu, you will be prompted
                through a series of entries to input information about the
                item to repair.
                
                Each step of the way you will receive instructions on next 
                steps.
                
                Finally you will be asked if the information entered is 
                correct -- if not you will return to the main menu to restart.
          ''')


def is_correct_repair():
    """Returns the response from the user to confirm repair information."""
    print("Is this information correct?\n")
    validate = input(
        "Enter 'y' to confirm and print Repair Ticket\nor 'n' to go back to main menu: "
    )
    return validate


def write_help():
    """Prints "help" to the communication file."""
    with open("helpMe.txt", "w") as f:
        f.write("help")


def get_help():
    """Reads help message from communication file and returns message to user."""
    with open("helpMe.txt") as f:
        helpful_message = f.readline()

    return helpful_message


def is_correct_service():
    """Returns user answer for is this information correct."""
    print("Is this information correct?\n")
    validate = input(
        "Enter 'y' to confirm and print Service Menu\nor 'n' to go back to main menu: "
    )
    return validate


def add_item_to_backlog(backlog, item):
    """Adds item to backlog and prints updated backlog for user."""
    backlog.append(item.item_name)
    print(backlog)


def remove_item_from_backlog(backlog):
    """Prompts user to enter item for removal, then removes item"""
    """from backlog and prints error or updated backlog."""
    item_to_remove = input("Enter the item to remove from backlog: ")
    if item_to_remove in backlog:
        backlog.remove(item_to_remove)
        print(backlog)
    else:
        print("Item is not in the backlog.")
        print("Current Backlog: ", backlog)


@click.command()
@click.option('--name', prompt='Enter the new item')
def create(Item=None):
    click.echo(f"Creating a new repair item!")
    print
    repair_item = Item.get_new_repair()
    repair_item.show_full_item()


def repair_menu():
    """Returns choice from Repair Menu options."""
    print(f"""
               ****************
               REPAIR MENU
               
               1- Add a New Repair to Backlog
               2- Print Backlog
               3- Delete Repair from Backlog
               
               Return to Main Menu
               ****************
               """)
    choice = input("Enter a number or type 'Main' to Return to Main Menu: ")
    return choice


def pay_menu():
    """Returns choice from Payments Menu options."""
    print(f"""
               ****************
               PAYMENTS MENU
               
               1- Pay Now
               
               Return to Main Menu
               ****************
               """)
    choice = input("Enter a number or type 'Main' to Return to Main Menu: ")
    return choice


def service_menu():
    """Returns choice from Service Menu options."""
    print(f"""
               ****************
               SERVICE MENU
               
               1- Add a New Service to Menu
               2- Print Service Menu
               
               Return to Main Menu
               ****************
               """)
    choice = input("Enter a number or type 'Main' to Return to Main Menu: ")
    return choice


def help():
    """Returns choice from Help Center Menu options."""
    print(f"""
               *****************
                HELP CENTER MENU
               
               1- Documentation
               2- FAQs
               
               Return to Main Menu
               *****************
               """)
    article = input("Enter a number or type 'Main' to Return to Main Menu: ")
    return article


def greeting():
    """Prints welcome message."""
    click.echo(f"""
               **************
               HELLO!
               **************
               
               Welcome to your RepairOS!
               Software that gives you only the features that 
               provide impact to your shop and none of the 
               extras. 
               
               We shave the grams off your bulky systems!
               
               
               """)


def menu():
    """Returns choice from Main Menu options."""
    click.echo(f"""
               **************
               MAIN MENU
               
               1- Repair Menu
               2- Service Menu [Admins]
               3- Pay Now 
               4- Help
               5- HelpBot
               
               Exit RepairOS
               ****************
               
               """)
    direction = input("Enter a number or type 'Exit' to exit RepairOS: ")
    return direction


# This is Andrea's service launch call
def login():
    svc.launchService()
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

    # ######################################################
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
    return outstring, pwInvalid


def new_repair(backlog):

    item = Item.get_new_repair()
    item.show_full_item()
    print("\n")
    validate = is_correct_repair()
    print("\n")
    if validate == "y":

        add_item_to_backlog(backlog, item)
        print_repair_ticket(item)
    if validate == "n":
        pass


def repair_menu_options(repair_menu_choice, backlog):

    if repair_menu_choice == "1":
        new_repair(backlog)

    if repair_menu_choice == "2":
        print("Backlog of Repairs: ")
        print_backlog(backlog)

    if repair_menu_choice == "3":
        remove_item_from_backlog(backlog)

    if repair_menu_choice.upper() == "MAIN":
        pass


def service_menu_options(svc_menu_choice, service_dict):
    if svc_menu_choice == "1":

        service = Service.get_new_service()
        service_dict[service.service_name] = service.price
        service.show_new_service()
        print("\n")
        validate = is_correct_service()
        print("\n")
        if validate == "y":
            print_service_menu(service_dict)
            pass

        if validate == "n":
            pass

    if svc_menu_choice == "2":
        print_service_menu(service_dict)
        pass

    if svc_menu_choice.upper() == "MAIN":
        pass


def help_menu_options(article):

    if article == "1":
        documentation()
        article = help()
    if article == "2":
        faqs()
        article = help()
    if article.upper() == "MAIN":
        pass


def pay_menu_options(pay_now):
    if pay_now == "1":
        print("To Be Implemented")
        pass
    if pay_now.upper() == "MAIN":
        pass


def helpBot():
    print("Help is on the way!\n")
    write_help()
    time.sleep(2)
    help_msg = get_help()
    time.sleep(2)
    print(help_msg)
    print("\nReturning to main menu...")


def main():

    greeting()
    login()
    backlog = []
    service_dict = {}
    while 1:
        main_menu_choice = menu()
        print("\n")

        if main_menu_choice == "1":
            repair_menu_choice = repair_menu()
            repair_menu_options(repair_menu_choice, backlog)

        if main_menu_choice == "2":
            svc_menu_choice = service_menu()
            service_menu_options(svc_menu_choice, service_dict)

        if main_menu_choice == "4":
            article = help()
            help_menu_options(article)

        if main_menu_choice == "3":
            pay_now = pay_menu()
            pay_menu_options(pay_now)

        if main_menu_choice == "5":
            helpBot()

        if main_menu_choice.upper() == "EXIT":
            print("Thank you, have a great day!")
            break


if __name__ == '__main__':
    main()
