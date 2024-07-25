# test_seat_booked_table_handler.py

import admin_database_handler.seat_booked_table_handler as sbth
import sqlite3

# Open database connection to perform sql queries
con = sqlite3.connect('C:\\Users\\somnath.maity\\PycharmProjects\\train_ticket_booking_system\\admin_database_handler\\ticket_booking.db')
cur = con.cursor()

def fill_all_seats_of_coachNo_of_coachA(coachNo_of_coachA):
    for seat_no in range(1, 31):
        sbth.bookSeat(cur, 12345, 'd0', 'a', coachNo_of_coachA, seat_no)

def print_seats_of_coach_A():
    query = f"SELECT * FROM d0_12345_A"
    cur.execute(query)
    for row in cur.execute(query):
        print(row)

def fill_first_n_seats_of_coachNo_of_coachA(coachNo_of_coachA, n):
    for seat_no in range(1, n+1):
        sbth.bookSeat(cur, 12345, 'd0', 'a', coachNo_of_coachA, seat_no)

def fill_all_seats_of_coachNo_of_coachType(coachType, coachNo): # ('a', 1)
    for seat_no in range(1, 31):
        sbth.bookSeat(cur, 12345, 'd0', coachType, coachNo, seat_no)

def print_seats_of_coachType(coachType):
    query = f"SELECT * FROM d0_12345_{coachType}"
    cur.execute(query)
    for row in cur.execute(query):
        print(row)

def fill_first_n_seats_of_coachNo_of_coachType(coachType, coachNo, n):
    for seat_no in range(1, n+1):
        sbth.bookSeat(cur, 12345, 'd0', coachType, coachNo, seat_no)

fill_all_seats_of_coachNo_of_coachA(1)
fill_all_seats_of_coachNo_of_coachA(2)
fill_first_n_seats_of_coachNo_of_coachA(3, 29)

print_seats_of_coachType('c')
con.commit()

# print(lowestEmptySeatNo(12345, 'd0', 'A', 1))
print('Lowest Empty Coach No, lowest Seat No: ', sbth.lowestEmptyCoachNo(12345, 'd0', 'C'))

# Commit and close database connection
# con.commit()
con.close()

