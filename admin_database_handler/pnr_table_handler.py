# pnr_table_handler.py

import sqlite3

# Open database connection to perform sql queries
con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
cur = con.cursor()

def initializePnrNo() :
    con = sqlite3.connect(
        'C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    cur.execute('''DROP TABLE IF EXISTS pnr''')
    createQuery = '''CREATE TABLE IF NOT EXISTS pnr(
            max_pnr_no INT
            )'''
    cur.execute(createQuery)

    inserQuery = '''INSERT INTO pnr VALUES(1000000000)'''
    cur.execute(inserQuery)
    con.commit()
    con.close()

def getMaxPnrNo(cur) :
    query = '''SELECT * FROM pnr'''
    cur.execute(query)
    maxPnrNo = cur.fetchall()[0][0]

    return maxPnrNo

def generateNewPnrNo(cur) :
    currentPnrNo = getMaxPnrNo(cur)
    newPnrNo = currentPnrNo + 1
    # increment pnr no by 1
    updateQuery = f'UPDATE pnr SET max_pnr_no = {newPnrNo} WHERE max_pnr_no = {currentPnrNo}'
    cur.execute(updateQuery)

    return newPnrNo

# Test
# initializePnrNo()
# print(getMaxPnrNo(cur))

# Commit and close the database connection
# con.commit()
con.close()