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
