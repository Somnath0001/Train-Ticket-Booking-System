# database_handler.py

import sqlite3

# Open database connection to perform sql queries
con = sqlite3.connect('ticket_booking.db')
cur = con.cursor()

# cur.execute('''create table if not exists users
#                (userid text primary key, password text, fname text, lname text, address text, age int, email text, mobile int)''')

# cur.execute('''insert into users values
#             ('soum3','soum3','Soumen','Karma','13, Washington',24,'soum@mail.com',2223334444)''')

# for row in cur.execute('''select * from users''') :
#     print(row)

# for row in cur.execute('''select * from passagners;'''):
#     print(row)

cur.execute('''create table d0_12345
            (coachA1 int,
            coachB1 int,
            coachC1 int)''')

cur.execute('''insert into d0_12345 values(12, 23,34)''')
for row in cur.execute('''select * from d0_12345'''):
    print(row)

# Commit and close the database connection
# con.commit()
con.close()