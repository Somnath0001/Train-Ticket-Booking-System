# seat_availability_search.py

import sqlite3

def searchAvailableSeats(trainNo, dateNo):
    noOfCoachA = 3 # in future we can fetch based on train details
    noOfCoachB = 7 # in future we can fetch based on train details
    noOfCoachC = 12 # in future we can fetch based on train details
    noOfCoachASeatAvailable = 0
    noOfCoachBSeatAvailable = 0
    noOfCoachCSeatAvailable = 0

    con = sqlite3.connect('admin_database_handler/ticket_booking.db')
    cur = con.cursor()

    for coachNo in range(1, noOfCoachA+1):
        query = f"SELECT COUNT(*) FROM {dateNo}_{trainNo}_a WHERE a{coachNo} = 0"
        for row in cur.execute(query):
            # print(row[0])
            noOfCoachASeatAvailable += row[0]
    # print(f"noOfCoachASeatAvailable: {noOfCoachASeatAvailable}")

    for coachNo in range(1, noOfCoachB+1):
        query = f"SELECT COUNT(*) FROM {dateNo}_{trainNo}_b WHERE b{coachNo} = 0"
        for row in cur.execute(query):
            # print(row[0])
            noOfCoachBSeatAvailable += row[0]
    # print(f"noOfCoachBSeatAvailable: {noOfCoachBSeatAvailable}")

    for coachNo in range(1, noOfCoachC+1):
        query = f"SELECT COUNT(*) FROM {dateNo}_{trainNo}_c WHERE c{coachNo} = 0"
        for row in cur.execute(query):
            # print(row[0])
            noOfCoachCSeatAvailable += row[0]
    # print(f"noOfCoachCSeatAvailable {noOfCoachCSeatAvailable}")
    # con.commit()
    # con.close()
    return(noOfCoachASeatAvailable, noOfCoachBSeatAvailable, noOfCoachCSeatAvailable)

# print(searchAvailableSeats(12345, 'd0'))

