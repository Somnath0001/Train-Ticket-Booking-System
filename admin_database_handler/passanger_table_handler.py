# passanger_table_handler.py

import sqlite3

# Open database connection to perform sql queries
con = sqlite3.connect('ticket_booking.db')
cur = con.cursor()

# cur.execute('''DROP TABLE passangers''')

# cur.execute('''CREATE TABLE IF NOT EXISTS passangers
#             (passanger_id INT PRIMARY KEY,
#             name TEXT,
#             age INT,
#             gender TEXT,
#             id_card_type TEXT,
#             id_card_no TEXT,
#             pnr_no INT,
#             booked_by TEXT)''')
#
# cur.execute('''INSERT INTO passangers VALUES(1, 'Som', 25, 'M', 'VOTER CARD', 'ASD12345', 1234567890, 'som1')''')

def getAllPassagnerDetails(cur) :
    for row in cur.execute('''SELECT * FROM passangers'''):
        print(row)

def getPassangerDetailsByPassangerId(cur, passangerId) :
    query = f'SELECT * FROM Passangers WHERE passanger_id = \'{passangerId}\''
    for row in cur.execute(query) :
        print(row)

def getPassangerDetailsByUserId(cur, userId) :
    query = f'SELECT * FROM Passangers WHERE booked_by = \'{userId}\''
    for row in cur.execute(query) :
        print(row)

def insertPassangerDetails(cur, bookId, name, age, gender, idCardType, idCardNo, pnrNo, userId) :
    query = f'INSERT INTO Passangers VALUES({bookId}, \'{name}\', {age}, \'{gender}\', \'{idCardType}\', \'{idCardNo}\', {pnrNo}, \'{userId}\')'
    cur.execute(query)

def updateStatusAndAddPnrNoByBookId(cur, bookId, pnrNo) :
    query = f'UPDATE Passangers SET pnr_no = {pnrNo} WHERE passanger_id = {bookId}'
    cur.execute(query)

def getAllPnrNoForUser(cur, userId) :
    # returns list of PNR No for the user where PNR No is not null
    pnrNoList = []
    query = f'SELECT pnr_no FROM Passangers WHERE booked_by = \'{userId}\' AND pnr_no is NOT NULL'
    for row in cur.execute(query) :
        pnrNoList.append(row[0])

    return pnrNoList

# insertPassangerDetails(cur, 2, 'Som', 25, 'M', 'VOTER CARD', 'ASD12345', 1234567890, 'som1')

# getAllPassagnerDetails()

# getPassangerDetailsByPassangerId(32)

# getPassangerDetailsByUserId('som1')
# getAllPassagnerDetails()
#
# updateStatusAndAddPnrNoByBookId(cur, 86, 1000000005)
# updateStatusAndAddPnrNoByBookId(cur, 87, 1000000005)
#
# getAllPassagnerDetails()

# print(getAllPnrNoForUser(cur, 'lal2'))

# Commit and close the database connection
con.commit()
con.close()