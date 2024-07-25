# users_table_handler.py

import sqlite3

# Open connection to perform sql queries
con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
cur = con.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS users
#             (user_id TEXT PRIMARY KEY,
#             password TEXT NOT NULL,
#             f_name TEXT,
#             l_name TEXT,
#             address TEXT,
#             age INT,
#             email TEXT,
#             mobile INT)''')

# cur.execute('''INSERT INTO users VALUES('som1','som1','Som','Maity','12, Park Street',25,'som@mail.com',1112223333)''')
# cur.execute('''INSERT INTO users VALUES('lal2','lal2','Laltu','Karma','11, Avanue',24,'lal@mail.com',3334445555)''')
# cur.execute('''INSERT INTO users VALUES('soum3','soum3','Soumen','Karma','soum@mail.com',24,'soum@mail.com',2223334444)''')
# cur.execute('''INSERT INTO users VALUES('sou4','sou4','Souvick','Patra','14, Washington',26,'sou@mail.com',4445556666)''')

# View all Users' details
def getAllUsersDetails(cur) :
    for row in cur.execute('''SELECT * FROM users'''):
        print(row)

def getUserDetails(cur, userId) :
    query = f'SELECT * FROM Users WHERE user_id = \'{userId}\''
    cur.execute(query)
    userDetails = cur.fetchone()
    return userDetails

def signup(userId, password, fname, lname, address, age, email, mobile):
    # Open database connection to perform sql queries
    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    query = f'INSERT INTO Users VALUES(\'{userId}\',\'{password}\',\'{fname}\',\'{lname}\',\'{address}\',{age},\'{email}\',{mobile})'
    cur.execute(query)

    # Commit and close the database connection
    con.commit()
    con.close()

    # User confirmation
    print('Signup Successful :)\n')
    print('Hi ', fname, ', Redirecting you to login page...')

def isUserIdExists(userId) :
    # returns True if userId exists else False

    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    query = f'SELECT EXISTS(SELECT user_id FROM Users WHERE user_id=\'{userId}\' LIMIT 1)'
    cur.execute(query)
    result = cur.fetchone()[0]
    # print(result)

    # Close the database connection
    con.close()

    if (result == 1) :
        return True
    else :
        return False

def isPasswordMatching(userId, password) :
    # returns True if password is matching else False

    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    query = f'SELECT password FROM Users WHERE user_id=\'{userId}\' LIMIT 1'
    cur.execute(query)
    result = cur.fetchone()[0]
    # print(result)

    # Close the database connection
    con.close()

    if (result == password):
        return True
    else:
        return False

# signup('dhananjay11', 'dhananjay11', 'Dhananjay', 'Valeti', 'Vishakhapatnam, AP', 24, 'dhananjay@mail.com', 9988776655)
# getAllUsersDetails(cur)
# print(isUserIdExists('lal2'))
# print(isPasswordMatching('lal2', 'lal2'))
# print(getUserDetails(cur, 'som1'))

# Commit and close the database connection
con.commit()
con.close()
