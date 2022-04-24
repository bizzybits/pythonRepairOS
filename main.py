from datetime import date
import click


class Item:

    def __init__(self, item_name, issue, date, customer):
        self.item_name = item_name
        self.issue = issue
        self.date = date
        self.customer = customer

    def show_full_item(self):
        print(''' 
            **************
             Repair Ticket
            **************''')
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


def is_correct():
    print("Is this information correct?\n")
    validate = input(
        "Enter 'y' to confirm and print Repair Ticket\nor 'n' to go back to main menu: "
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


def help():
    print(f"""
               **************
               MENU
               
               1- Documentation
               2- FAQs
               
               Return to Main Menu
               **************
               """)
    article = input("Enter a number or type 'Main' to Return to Main Menu: ")
    return article


def greeting():
    click.echo(f"""
               **************
               HELLO!
               **************
               
               Welcome to your RepairOS!
               """)


def menu():
    click.echo(f"""
               **************
               MENU
               
               1- Enter a New Repair Item
               2- Help
               
               Exit RepairOS
               **************
               
               """)
    direction = input("Enter a number or type 'Exit' to exit RepairOS: ")
    return direction


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
    while 1:
        direction = menu()
        print("\n")
        if direction == "1":

            item = Item.get_new_repair()
            item.show_full_item()
            print("\n")
            validate = is_correct()
            print("\n")
            if validate == "y":
                print_repair_ticket(item)
                direction = menu()

            if validate == "n":
                direction = menu()
            else:
                if direction.upper() == "EXIT":
                    print("Thank you, have a great day!")
                    break

        if direction == "2":
            article = help()
            if article == "1":
                documentation()
                article = help()
            if article == "2":
                faqs()
                article = help()
            if article.upper() == "MAIN":
                direction = menu()
            else:
                print("invalid command, try again")
                direction = menu()
                if direction.upper() == "EXIT":
                    print("Thank you, have a great day!")
                    break

        if direction.upper() == "EXIT":
            print("Thank you, have a great day!")
            break

        # else:
        #     print("invalid command, try again")
        #     direction = menu()


if __name__ == '__main__':
    main()
