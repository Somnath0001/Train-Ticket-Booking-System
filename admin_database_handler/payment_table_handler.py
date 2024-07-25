# payment_table_handler.py

import sqlite3
import admin_database_handler.pnr_table_handler as pnrth

# Open database connection to perform sql queries
con = sqlite3.connect('ticket_booking.db')
cur = con.cursor()

# # cur.execute('''DROP TABLE payment''')
#
# cur.execute('''CREATE TABLE IF NOT EXISTS payment
#         (payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id TEXT,
#         pnr_no INT,
#         amount INT,
#         method TEXT,
#         card_no INT,
#         status TEXT,
#         datetime TEXT DEFAULT CURRENT_TIMESTAMP)''')


# cur.execute('''INSERT INTO payment VALUES(1, 'som1', 1234567890, 200, 'CARD', 1234123412341234, 'PEND', datetime())''')



def addPayment(cur, userId, amount, paymentMethod, cardNo, status='PEND') :
    query = f'INSERT INTO payment(user_id, amount, method, card_no, status) VALUES(\'{userId}\', {amount}, \'{paymentMethod}\', {cardNo}, \'{status}\')'
    cur.execute(query)
    selectQuery = f'SELECT MAX(payment_id) FROM Payment'
    cur.execute(selectQuery)
    newlyCreatedPaymentId = cur.fetchall()[0][0]
    return newlyCreatedPaymentId

def updatePaymentStatusToCOMP(cur, paymentId) :
    # generate PNR No.
    pnrNo = pnrth.generateNewPnrNo(cur)
    updateQuery = f'UPDATE Payment SET status = \'COMP\', pnr_no = {pnrNo} WHERE payment_id = {paymentId}'
    cur.execute(updateQuery)
    return pnrNo

def viewAllPayment(cur) :
    for row in cur.execute('''SELECT * FROM payment'''):
        print(row)

# # payment_id = addPayment(cur, 'som1', 3000, 'CARD', 1234123412341234)
# # print(payment_id)
# updatePaymentStatusToCOMP(cur, 3)
#
#
# viewAllPayment(cur)

# Commit and close the database connection
# con.commit()
con.close()