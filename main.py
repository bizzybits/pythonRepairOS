import time
import click
import andreasMicroService as svc  #for launch, service runs in own process
from models import cursor, connection, all_repairs, all_services
from menus import repair_menu, pay_menu, service_menu, help, greeting, menu
from helpCenter import faqs, documentation
from item import Item, print_repair_ticket
from service import Service


def print_backlog():
    """Prints mechanic service backlog."""
    print(''' 
            ***********************
             General Service Backlog
            ***********************''')
    print(all_repairs)


def print_service_menu():
    """Prints service menu."""
    print(f"""
           **************
            Service Menu
           **************""")
    print(all_services)


def print_repair_ticket(item):
    """Prints repair ticket with item information."""
    print(f"""
           **************
           Repair Ticket for {item.item_name}!
           **************""")
    print("\nThe item that needs repair is: " + item.item_name)
    print(f"{item.customer} reports issue with: {item.issue} ")
    print(f"{item.item_name} repair is due on {item.date}")


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


def add_service_to_menu(service):
    """Adds service to menu and prints updated backlog for user."""
    with connection:
        cursor.execute("INSERT INTO services VALUES (?, ?)",
                       [service.service_name, service.price])
        connection.commit()


def add_item_to_backlog(item):
    """Adds item to backlog and prints updated backlog for user."""
    insert_repair(item)
    print(all_repairs)


def insert_repair(item):
    with connection:
        cursor.execute("INSERT INTO repairs VALUES (?, ?, ?, ?, ?)", [
            item.repair_id, item.item_name, item.issue, item.date,
            item.customer
        ])
        connection.commit()


def remove_item_from_backlog():
    """Prompts user to enter item for removal, then removes item"""
    """from backlog and prints error or updated backlog."""
    item_to_remove = input("Enter the repair id to remove from backlog: ")
    delete_repair(item_to_remove)


def delete_repair(item_to_remove):
    item_to_remove = int(item_to_remove)
    with connection:
        cursor.execute("DELETE from repairs WHERE repair_id = :item_to_remove",
                       {'item_to_remove': item_to_remove})
        connection.commit()


@click.command()
@click.option('--name', prompt='Enter the new item')
def create(Item=None):
    click.echo(f"Creating a new repair item!")
    print
    repair_item = Item.get_new_repair()
    repair_item.show_full_item()


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


def new_repair():

    item = Item.get_new_repair()
    item.show_full_item()
    print("\n")
    validate = is_correct_repair()
    print("\n")
    if validate == "y":

        add_item_to_backlog(item)
        print_repair_ticket(item)

    if validate == "n":
        pass

    return item


def repair_menu_options(repair_menu_choice):

    if repair_menu_choice == "1":
        new_repair()

    if repair_menu_choice == "2":
        print("Backlog of Repairs: ")
        print_backlog()

    if repair_menu_choice == "3":
        remove_item_from_backlog()

    if repair_menu_choice.upper() == "MAIN":
        pass


def service_menu_options(svc_menu_choice):
    if svc_menu_choice == "1":

        service = Service.get_new_service()
        service.show_new_service()
        print("\n")
        validate = is_correct_service()
        print("\n")
        if validate == "y":
            print_service_menu()
            add_service_to_menu(service)
            pass

        if validate == "n":
            pass

    if svc_menu_choice == "2":
        print_service_menu()
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
            repair_menu_options(repair_menu_choice)

        if main_menu_choice == "2":
            svc_menu_choice = service_menu()
            service_menu_options(svc_menu_choice)

        if main_menu_choice == "4":
            article = help()
            help_menu_options(article)

        if main_menu_choice == "3":
            pay_now = pay_menu()
            pay_menu_options(pay_now)

        if main_menu_choice == "5":
            helpBot()

        if main_menu_choice.upper() == "EXIT":
            connection.close()
            print("Thank you, have a great day!")
            break


if __name__ == '__main__':
    main()
