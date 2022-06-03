import click


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