import sqlite3

from click import command

#define connection and cursor

connection = sqliteConnection = sqlite3.connect('repairOS.db')
cursor = sqliteConnection.cursor()

#create repair table
command1 = """CREATE TABLE IF NOT EXISTS
    repairs(repair_id INTEGER, item_name TEXT, issue TEXT, due_date TEXT, customer TEXT)"""
cursor.execute(command1)

#create service table
command2 = """CREATE TABLE IF NOT EXISTS
    services(service_name TEXT, price TEXT)"""
cursor.execute(command2)

#add to repairs

# cursor.execute(
#     "INSERT INTO repairs VALUES (1, 'Schwinn', 'front flat tire', '06/07/2022', 'Helen')"
# )
# cursor.execute(
#     "INSERT INTO repairs VALUES (2, 'Surly', 'saddle swap','07/4/2022', 'Franklin')"
# )
# cursor.execute(
#     "INSERT INTO repairs VALUES (3, 'Colnago', 'install water bottle cage', '06/09/2022', 'Petunia')"
# )

# #add to services
# cursor.execute("INSERT INTO services VALUES ('Flat Fix', '$25')")
# cursor.execute("INSERT INTO services VALUES ('Saddle Swap', '$15')")
# cursor.execute("INSERT INTO services VALUES ('Accessory Install', '$10')")

#get results

cursor.execute("SELECT * FROM services")

all_services = cursor.fetchall()

cursor.execute("SELECT * FROM repairs")
all_repairs = cursor.fetchall()
