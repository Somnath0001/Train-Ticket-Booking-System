# booking_table_handler.py

import sqlite3

# Open database connection to perform sql queries
con = sqlite3.connect('ticket_booking.db')
cur = con.cursor()

# cur.execute('''DROP TABLE Booking''')

# cur.execute('''CREATE TABLE IF NOT EXISTS Booking(
#             book_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             train_no int not null,
#             date_no text not null,
#             coach_type text not null,
#             coach_no int not null,
#             seat_no int not null,
#             booking_date text DEFAULT CURRENT_TIMESTAMP,
#             journey_from int,
#             journey_to int,
#             journey_from_time text,
#             journey_to_time text,
#             food_ordered text,
#             status text)''')

# for row in cur.execute('''SELECT sql FROM sqlite_schema WHERE name = 'booking';'''):
#     print(row)

# cur.execute('''SELECT * FROM booking''')
# cur.fetchall()

# Filling sample data into booking table
# cur.execute('''INSERT INTO booking VALUES(0001, 12346, 'd0', 'A', 2, 13, '2023-07-19', 1, 6, '2023-07-25 10:50:00', '2023-07-25 14:50:00', 'N', 'PEND')''')
# cur.execute('''INSERT INTO booking(train_no, date_no, coach_type, coach_no, seat_no, journey_from, journey_to, journey_from_time, journey_to_time, food_ordered, status) VALUES(12346, 'd0', 'A', 2, 13, 1, 6, '2023-07-25 10:50:00', '2023-07-25 14:50:00', 'N', 'PEND')''')


# for row in cur.execute('''SELECT * FROM booking;'''):
#     print(row)

def generateBookId():
    # It will return unique bookId
    pass

def getMaxBookId(cur):
    query = f'SELECT MAX(book_id) FROM Booking'
    cur.execute(query)
    book_id = cur.fetchone()[0]
    # print(book_id)
    return book_id

def setBookingDetails(cur, trainNo, dateNo, coachType, coachNo,seatNo, journeyFrom, journeyTo, journeyFromTime, journeyToTime, foodOrdered, status):
    # print(cur, trainNo, dateNo, coachType, coachNo,seatNo, journeyFrom, journeyTo, journeyFromTime, journeyToTime, foodOrdered, status)
    query = f'INSERT INTO booking(train_no, date_no, coach_type, coach_no, seat_no, journey_from, journey_to, journey_from_time, journey_to_time, food_ordered, status) VALUES({trainNo}, \'{dateNo}\', \'{coachType}\', {coachNo}, {seatNo}, {journeyFrom}, {journeyTo}, \'{journeyFromTime}\', \'{journeyToTime}\', \'{foodOrdered}\', \'{status}\')'
    # print(query)
    cur.execute(query)
    book_id = getMaxBookId(cur)
    return book_id


def getAllBookingDetails(cur):
    for row in cur.execute('''SELECT * FROM booking;'''):
        print(row)

def getBookingDetails(cur, book_id):
    cur.execute(f'SELECT * FROM booking WHERE book_id = {book_id};')
    print(cur.fetchone())

def updateBookingStatusByBookId(cur, bookId) :
    query = f'UPDATE Booking SET status = \'COMP\' WHERE book_id = \'{bookId}\''
    cur.execute(query)



# Test
# getAllBookingDetails()
# getBookingDetails(1)

# setBookingDetails(cur, 12346, 'd0', 'A', 2, 13, 1, 6, '2023-07-25 10:50:00', '2023-07-25 14:50:00', 'N', 'PEND')

# updateBookingStatusByBookId(cur, 86)
# updateBookingStatusByBookId(cur, 87)
# getAllBookingDetails()

# commit : post everything is sorted, we can commit
# Commit and close the database connection
con.commit()
con.close()



