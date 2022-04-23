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


def is_correct():
    print("Is this information correct?\n")
    validate = input("Enter 'y' to confirm or 'n' to go back to main menu: ")
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


# def run_the_counts(count, name):
#     for _ in range(count):
#         click.echo(f"Hello {name}")


def help():
    print(f"""
               **************
               MENU
               
               1- Documentation
               2- FAQs
               
               Exit
               **************
               """)
    article = input("Enter a number or type 'Exit' to exit: ")
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
               
               Exit
               **************
               
               """)
    direction = input("Enter a number or type 'Exit' to exit: ")
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
    direction = menu()
    print("\n")
    while direction == "1":

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

    if direction == "2":
        article = help()
        if article == "1":
            print("Documentation")
            direction = menu()
        if article == "2":
            print("FAQs")
            direction = menu()

    if direction == "Exit" or "exit":
        print("Thank you, have a great day!")
    else:
        print("invalid command, try again")
        direction = menu()


if __name__ == '__main__':
    main()
