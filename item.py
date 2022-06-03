class Item:

    def __init__(self, id, item_name, issue, date, customer):
        self.repair_id = id
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
                id = input("Enter new repair_id for repair: ")
                item_name = input("Enter new item for repair: ")
                issue = input("Enter issue to be repaired: ")
                due_date = input("Enter date to be repaired: ")
                customer = input("Enter customer name: ")

                return cls(id, item_name, issue, due_date, customer)
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
