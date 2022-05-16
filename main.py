import time
import click
import validateUser as svc

from collections import defaultdict
from collections import deque


class Item:

    def __init__(self, item_name, issue, date, customer):
        self.item_name = item_name
        self.issue = issue
        self.date = date
        self.customer = customer

    def show_full_item(self):
        print(''' 
            **************************
             Repair Ticket Validation 
            **************************''')
        print("\nThe item that needs repair is: " + self.item_name)
        print("Customer reports issue with:  " + self.issue)

    @classmethod
    def get_new_repair(cls):
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
        print(''' 
            ********************
             Service Menu Item
            ********************''')
        print("\nThe new service added is: " + self.service_name)
        print("The new price for the service is:  " + self.price)

    @classmethod
    def get_new_service(cls):
        while 1:
            try:
                service_name = input("Enter new service name: ")
                price = input("Enter the new price: ")
                return cls(service_name, price)
            except:
                print("Invalid input!")
                continue


def print_backlog(self):
    print(''' 
            ***********************
             General Service Backlog
            ***********************''')
    print(list(self.keys()))


def print_service_menu(service_dict):
    print(f"""
           **************
            Service Menu
           **************""")
    for service, price in service_dict.items():
        print(service + " " + price)


def print_repair_ticket(item):
    print(f"""
           **************
           Repair Ticket for {item.item_name}!
           **************""")
    print("\nThe item that needs repair is: " + item.item_name)
    print(f"{item.customer} reports issue with: {item.issue} ")
    print(f"{item.item_name} repair is due on {item.date}")


def faqs():
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
    print("Is this information correct?\n")
    validate = input(
        "Enter 'y' to confirm and print Repair Ticket\nor 'n' to go back to main menu: "
    )
    return validate


def write_help():
    with open("helpMe.txt", "w") as f:
        f.write("help")


def get_help():

    with open("helpMe.txt") as f:
        helpful_message = f.readline()

    return helpful_message


def is_correct_service():
    print("Is this information correct?\n")
    validate = input(
        "Enter 'y' to confirm and print Service Menu\nor 'n' to go back to main menu: "
    )
    return validate


@click.command()
# @click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def greet(name):
    # for _ in range(count):
    click.echo(f"Hello {name}!")


@click.command()
@click.option('--name', prompt='Enter the new item')
# @click.argument('item')
def create(Item=None):
    click.echo(f"Creating a new repair item!")
    print
    repair_item = Item.get_new_repair()
    repair_item.show_full_item()


def repair_menu():
    print(f"""
               ****************
               REPAIR MENU
               
               1- Add a New Repair 
               
               Return to Main Menu
               ****************
               """)
    choice = input("Enter a number or type 'Main' to Return to Main Menu: ")
    return choice


def pay_menu():
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
    click.echo(f"""
               **************
               MAIN MENU
               
               1- Enter a New Repair Item 
               2- Service Menu [Admins]
               3- Pay Now 
               4- Help
               5- HelpBot
               
               Exit RepairOS
               ****************
               
               """)
    direction = input("Enter a number or type 'Exit' to exit RepairOS: ")
    return direction


def go_back_to_main():
    menu()


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
    # with open("loginUser.txt", "w") as logger:
    #     logger.write(outstring)
    #     logger.close()

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


@click.command()
# @click.option('--count', type=int, help='number of greetings')
@click.option('--name', prompt='Enter the new item')
def justatest(Item=None):
    """
    
░██████╗██╗░██████╗░  ░█████╗░██╗░░░░░██╗
██╔════╝██║██╔═══██╗  ██╔══██╗██║░░░░░██║
╚█████╗░██║██║██╗██║  ██║░░╚═╝██║░░░░░██║
░╚═══██╗██║╚██████╔╝  ██║░░██╗██║░░░░░██║
██████╔╝██║░╚═██╔═╝░  ╚█████╔╝███████╗██║
╚═════╝░╚═╝░░░╚═╝░░░  ░╚════╝░╚══════╝╚═╝
    
    
    
\nSick driver code for rippin cli
    """
    # if count is not None:
    #     run_the_counts(count, name)
    # if Item is None:
    #     greeting(Item)


def main():
    greeting()
    login()
    queue = deque(["Schwinn", "Huffy", "Colnago"])
    backlog = {"bike"}
    while 1:
        main_menu_choice = menu()
        print("\n")

        if main_menu_choice == "1":

            repair_menu_choice = repair_menu()
            if repair_menu_choice == "1":

                item = Item.get_new_repair()
                item.show_full_item()
                print("\n")
                validate = is_correct_repair()
                print("\n")
                if validate == "y":

                    queue.append(item.item_name)
                    print_repair_ticket(item)
                    #print_backlog(queue)
                    print(list(queue))
                    print(queue[0])

                    pass
                    #repair_menu_choice = repair_menu()

                if validate == "n":
                    #repair_menu_choice = repair_menu()
                    pass

            if repair_menu_choice.upper() == "MAIN":
                pass

            # else:
            #     print("invalid command, returning to main menu")
            #     main_menu_choice = menu()

        if main_menu_choice == "2":
            service_dict = {}
            svc_menu_choice = service_menu()
            if svc_menu_choice == "1":

                service = Service.get_new_service()
                service_dict[service.service_name] = service.price
                service.show_new_service()
                print("\n")
                validate = is_correct_service()
                print("\n")
                if validate == "y":
                    print_service_menu(service_dict)
                    # svc_menu_choice = service_menu()
                    pass

                if validate == "n":
                    #svc_menu_choice = menu()
                    pass

            if svc_menu_choice == "2":
                print_service_menu(service_dict)
                pass
                #svc_menu_choice = service_menu()

            if svc_menu_choice.upper() == "MAIN":
                # main_menu_choice = menu()
                pass
            # else:
            #     print("invalid command, try again")
            #     svc_menu_choice = menu()

        if main_menu_choice == "4":
            article = help()
            if article == "1":
                documentation()
                article = help()
            if article == "2":
                faqs()
                article = help()
            if article.upper() == "MAIN":
                main_menu_choice = menu()

        if main_menu_choice == "3":
            pay_now = pay_menu()
            if pay_now == "1":
                print("To Be Implemented")
                pass
            if pay_now.upper() == "MAIN":
                pass
            # else:
            #     print("invalid command, try again")
            #     main_menu_choice = menu()

        if main_menu_choice == "5":
            print("Help is on the way!\n")
            write_help()
            time.sleep(2)
            help_msg = get_help()
            time.sleep(2)
            print(help_msg)
            print("\nReturning to main menu...")

        if main_menu_choice.upper() == "EXIT":
            print("Thank you, have a great day!")
            break


if __name__ == '__main__':
    main()
