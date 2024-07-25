# ticketBookingBackend.py

import sqlite3
import admin_database_handler.seat_booked_table_handler as sbth
import admin_database_handler.booking_table_handler as bth
import admin_database_handler.stations_table_handler as sth

'''
bookAvailableSeat(trainNo, dateNo coachType, noOfPassangers, journeyFrom, journeyTo, journeyFromTime, journeyToTime, foodOrdered):
    1. Choose a seat from available seat
    for "noOfPassangers" times :
        chooseAvailableSeat(trainNO, coachType):
            search coachNo ascending.
                return the first empty coachNo
            search seatNo ascending.
                return the first empty seatNo
            should return
            2. coachNo
            3. seatNo
        2. set "isBooked = True" :
            bookSeat(trainNo, dateNo, coachType, coachNo, seatNo)
            going to update in seat_booked_table for the train, date and coachtype (Eg. : d0_12345_a)
        3. need to update in "booking" table as well
'''

def chooseAvailableSeat(trainNo, dateNo, coachType):
    result = sbth.lowestEmptyCoachNo(trainNo, dateNo, coachType) #(12345, 'd0', 'C')
    emptyCoachNo = result[0]
    emptySeatNo = result[1]
    return emptyCoachNo, emptySeatNo

def bookAvailableSeat(trainNo, dateNo, coachType, noOfPassangers, journeyFrom, journeyTo, journeyFromTime, journeyToTime, foodOrdered):
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()
    journeyFrom = sth.getStationNo(cur, journeyFrom)
    journeyTo = sth.getStationNo(cur, journeyTo)

    bookIdLists = []

    # book seat for each passenger
    for i in range(noOfPassangers):
        result = chooseAvailableSeat(trainNo, dateNo, coachType)
        coachNo = result[0]
        seatNo = result[1]
        # 2. book the seat
        sbth.bookSeat(cur, trainNo, dateNo, coachType, coachNo, seatNo)

        # 3. need to update in "booking" table as well
        book_id = bth.setBookingDetails(cur, trainNo, dateNo, coachType, coachNo, seatNo, journeyFrom, journeyTo, journeyFromTime,
                          journeyToTime, foodOrdered, status='PEND')

        print(f'Ticket is booked for passenger {i+1} with book_id = {book_id}')

        bookIdLists.append(book_id)
        con.commit()

    con.close()
    return bookIdLists

# Test
# print(chooseAvailableSeat(12345, 'd0', 'C'))

