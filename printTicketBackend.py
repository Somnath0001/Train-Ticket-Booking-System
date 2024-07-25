# printTicketBackend.py

import sqlite3
import os
import admin_database_handler.stations_table_handler as sth
import trainAvailability as ta

def prepareTicketBody(pnrNo) :
    # returns ticket body of the PNR Number

    # Open database connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    # Test
    # cur.execute('''SELECT * FROM Passangers''')
    # print('Passangers :')
    # print(cur.fetchall())
    #
    # cur.execute('''SELECT * FROM Booking''')
    # print('Booking :')
    # print(cur.fetchall())
    #
    # cur.execute('''SELECT * FROM Payment''')
    # print('Payment :')
    # print(cur.fetchall())
    #
    # cur.execute('''SELECT * FROM Trains''')
    # print('Trains :')
    # print(cur.fetchall())
    #
    # cur.execute('''SELECT * FROM Cards''')
    # print('Cards :')
    # print(cur.fetchall())

    # print('Join Query :')
    # query = f'SELECT b.status,b.journey_from,b.journey_to,b.journey_from_time,b.journey_to_time,pt.pnr_no,b.train_no,t.train_name,b.coach_type,b.booking_date,p.name,p.age,p.gender,b.food_ordered,pt.payment_id,pt.amount FROM Passangers p JOIN Booking b ON p.passanger_id=b.book_id JOIN Payment pt ON p.pnr_no=pt.pnr_no JOIN Trains t ON b.train_no=t.train_no WHERE pt.user_id=\'{userId}\' AND pt.status = \'COMP\''
    # # print('Join Query :')
    # data1 = cur.execute(query)
    # for row in data1:
    #     print(row)
    #     data = row

    # print('Query Other Than Passengers :')

    # Query Other Than Passengers
    queryOtherThanPassangers = f'SELECT b.status,b.journey_from,b.journey_to,b.journey_from_time,b.journey_to_time,pt.pnr_no,b.train_no,t.train_name,b.coach_type,b.booking_date,pt.payment_id,pt.amount FROM Passangers p JOIN Booking b ON p.passanger_id=b.book_id JOIN Payment pt ON p.pnr_no=pt.pnr_no JOIN Trains t ON b.train_no=t.train_no WHERE p.pnr_no=\'{pnrNo}\' AND pt.status = \'COMP\' LIMIT 1'

    for row in cur.execute(queryOtherThanPassangers):
        # print(row)
        dataOtherThanPassengers = row

    # Prepare data for info other than passengers
    status = dataOtherThanPassengers[0]
    journeyFrom = sth.getStationName(cur, dataOtherThanPassengers[1])
    journeyTo = sth.getStationName(cur, dataOtherThanPassengers[2])
    startTimestamp = dataOtherThanPassengers[3]
    endTimestamp = dataOtherThanPassengers[4]
    pnrNo = dataOtherThanPassengers[5]
    trainNo = dataOtherThanPassengers[6]
    trainName = dataOtherThanPassengers[7]
    coachType = dataOtherThanPassengers[8].upper()
    # print(f'Journey from - {journeyFrom}; Journey to - {journeyTo}')
    # distance = ta.calcDistance(journeyFrom, journeyTo)
    distance = ta.calcDistance(dataOtherThanPassengers[1], dataOtherThanPassengers[2])
    bookingDateTimestamp = dataOtherThanPassengers[9]
    paymentId = dataOtherThanPassengers[10]
    totalAmount = dataOtherThanPassengers[11]
    convenienceFee = 0
    grandTotal = totalAmount + convenienceFee

    # print('Query For Passagners :')
    queryForPassangers = f'SELECT p.name,p.age,p.gender,b.food_ordered, b.status, b.status FROM Passangers p JOIN Booking b ON p.passanger_id=b.book_id JOIN Payment pt ON p.pnr_no=pt.pnr_no JOIN Trains t ON b.train_no=t.train_no WHERE p.pnr_no=\'{pnrNo}\' AND pt.status = \'COMP\''
    dataOfPassengersList = []
    for row in cur.execute(queryForPassangers):
        # print(row)
        dataOfPassengersList.append(row)

    # Prepare html body for the ticket
    ticketBody1 = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Train Ticket</title>
    </head>
    <style>
        .ticket-container {
            display: grid;
            width: 800px;
            grid-template-columns: auto;
            background-color: #b3cee5;
            padding: 5px;
            border: 1px solid rgba(0, 0, 0, 0.8)
        }
        .header {
            display: grid;
            grid-template-columns: auto auto auto;
            padding: 10px;
            border: 1px solid rgba(0, 0, 0, 0.8);
            text-align: center;
        }
        .header-ers {
            font-size: large;
        }
        .header-status {
            font-size: smaller;
        }
        .journey-details {
            display: grid;
            grid-template-columns: auto auto;
            padding: 10px;
            border: 1px solid rgba(0, 0, 0, 0.8);
            row-gap: 3px;
        }
        .journey-details-right {
            text-align: right;
        }
        .booking-details {
            display: grid;
            grid-template-columns: auto auto auto;
            padding: 10px;
            border: 1px solid rgba(0, 0, 0, 0.8);
            text-align: center;
            row-gap: 5px;
        }
        .booking-details-color {
            color: green;
            font-weight: bold;
            font-size: large;
        }
        .passenger-details {
            display: grid;
            grid-template-columns: auto;
            padding: 10px;
            border: 1px solid rgba(0, 0, 0, 0.8);
        }
        .passanger-details-inside {
            display: grid;
            grid-template-columns: auto auto auto auto auto auto auto;
            text-align: center;
            padding: 5px;
        }
        .passanger-details-inside-data {
            font-size: small;
        }
        .payment-details {
            display: grid;
            grid-template-columns: auto auto;
            padding: 10px;
            border: 1px solid rgba(0, 0, 0, 0.8);
        }
        .help {
            display: grid;
            grid-template-columns: auto auto;
            padding: 10px;
            border: 1px solid rgba(0, 0, 0, 0.8);
            text-align: center;
        }
    </style>
    '''

    ticketBody2 = """\
    <body>
        <div class="ticket-container">
            <div class="header">
                <div class="header-status">{0}</div>
                <div class="header-ers"><b>Electronic Reservation Slip (ERS)</b></div>
                <div class="header-status">{0}</div>
            </div>
            <div class="journey-details">
                <div><b>Booked From</b></div>
                <div class="journey-details-right"><b>To</b></div>
                <div>{1}</div>
                <div class="journey-details-right">{2}</div>
                <div>Start Date : {3} HRS</div>
                <div class="journey-details-right">End Date : {4} HRS</div>
            </div>
            <div class="booking-details">
                <div><b>PNR</b></div>
                <div><b>Train No. / Name</b></div>
                <div><b>Class</b></div>
                <div class="booking-details-color">{5}</div>
                <div class="booking-details-color">{6} / {7}</div>
                <div class="booking-details-color">{8}</div>
                <div><b>Quota</b></div>
                <div><b>Distance</b></div>
                <div><b>Booking Date</b></div>
                <div>General</div>
                <div>{9} KM</div>
                <div>{10} HRS</div>
            </div>
            <div class="passenger-details">
                <div><b>Passanger Detials :</b></div>
                <div class="passanger-details-inside">
                    <div><b>#</b></div>
                    <div><b>Name</b></div>
                    <div><b>Age</b></div>
                    <div><b>Gender</b></div>
                    <div><b>Food Choice</b></div>
                    <div><b>Booking Status</b></div>
                    <div><b>Current Status</b></div>
                    """.format(status, journeyFrom, journeyTo, startTimestamp, endTimestamp, pnrNo, trainNo, trainName,
                               coachType, distance, bookingDateTimestamp)

    # Create html code for multiple passengers
    i = 1
    ticketBodyPassangerDetailsConsolidated = ''

    for dataOfPassengers in dataOfPassengersList:
        name = dataOfPassengers[0]
        age = dataOfPassengers[1]
        gender = dataOfPassengers[2]
        foodOrdered = dataOfPassengers[3]
        bookingStatus = dataOfPassengers[4]
        currentStatus = dataOfPassengers[5]
        # print('data of passengers : ', i, name, age, gender, foodOrdered, bookingStatus, currentStatus)
        ticketBodyPassangerDetails = """
                <div class="passanger-details-inside-data">{0}</div>
                <div class="passanger-details-inside-data">{1}</div>
                <div class="passanger-details-inside-data">{2}</div>
                <div class="passanger-details-inside-data">{3}</div>
                <div class="passanger-details-inside-data">{4}</div>
                <div class="passanger-details-inside-data">{5}</div>
                <div class="passanger-details-inside-data">{6}</div>
                """.format(i, name, age, gender, foodOrdered, bookingStatus, currentStatus)
        i += 1
        ticketBodyPassangerDetailsConsolidated += ticketBodyPassangerDetails

    ticketBody3 = """
                </div>
            </div>
            <div class="payment-details">
                <div>Transaction Id :</div>
                <div>{0}</div>
                <div><b>Payment Details :</b></div>
                <div></div>
                <div>Ticket Fare :</div>
                <div><span>&#8377;</span> {1}</div>
                <div>Convenience Fee :</div>
                <div><span>&#8377;</span> {2}</div>
                <div>Total Fare :</div>
                <div><span>&#8377;</span> {3}</div>
            </div>    
            <div class="help">
                <div>Help Line No. - 139</div>
                <div>SMS 'RAIL' to 139</div>
            </div>
        </div>
    </body>
    </html>
    """.format(paymentId, totalAmount, convenienceFee, grandTotal)

    # Combine all the pieces to create the whole html
    ticketBody = ticketBody1 + ticketBody2 + ticketBodyPassangerDetailsConsolidated + ticketBody3

    # Close database connection
    con.close()

    return ticketBody

def saveTicket(ticketBody) :
    # save the ticket body in a file and return filename
    # save in a file / create ticket.html

    # check whether filename exists : if yes add number at the end eg. ticket5.html
    counter = 0
    directory = "C:\\Users\\somna\\PycharmProjects\\train_ticket_booking_system\\generated_tickets\\"
    filename = "{}ticket{}.html"
    while os.path.isfile(filename.format(directory, counter)):
        counter += 1
    filename = filename.format(directory, counter)

    # Save the file now
    # filename = 'C:\\Users\\somnath.maity\\PycharmProjects\\train_ticket_booking_system\\generated_tickets\\ticket.html'
    with open(filename, 'w') as f:
        f.write(ticketBody)

    return filename

def printTicket(userId) :
    print('\n---  Print Ticket Backend  ---\n')

    # Prepare Ticket Body
    ticketBody = prepareTicketBody(userId)

    # Save the ticket-body
    filename = saveTicket(ticketBody)

    # Print Filename
    print(f'Ticket is downloaded successfully :)\nTicket: {filename}')

# Test
# printTicket('lal2')
