# trains_table_handler.py

import sqlite3

# Open database connection to perform sql queries
# con = sqlite3.connect('ticket_booking.db')
# cur = con.cursor()

# cur.execute('''DROP TABLE Trains''')

# cur.execute('''CREATE TABLE IF NOT EXISTS trains
#             (train_no INT PRIMARY KEY,
#             train_name TEXT,
#             d0 TEXT,
#             d1 TEXT,
#             d2 TEXT,
#             d3 TEXT,
#             d4 TEXT,
#             d5 TEXT,
#             d6 TEXT,
#             start_time TEXT,
#             first_stn_no INT,
#             speed INT,
#             no_of_coach_a INT,
#             no_of_coach_b INT,
#             no_of_coach_c INT,
#             fair_per_km REAL,
#             last_station_no INT)''')

# cur.execute('''INSERT INTO trains VALUES(12345,'Duronto Express','True','False','True','False','True','False','True',1030,1,120,20,40,100,2,33)''')
# cur.execute('''INSERT INTO trains VALUES(12346,'SMVT Express','False','False','True','True','False','False','True',1650,1,100,30,50,120,1,33)''')
# cur.execute('''INSERT INTO trains VALUES(12347,'Shatabdi Express','True','True','False','False','True','True','False',2300,1,110,20,50,80,1.2,33)''')

# for row in cur.execute('''SELECT * FROM trains;'''):
#     print(row)

def getTrainDetails(trainNo) :
    # returns train Details if exists else -1

    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    # Train No exists
    if (isTrainNoExists(trainNo)) :
        # Prepare Query
        query = f'SELECT * FROM Trains WHERE train_no = \'{trainNo}\''
        cur.execute(query)
        trainDetails = cur.fetchone()
        return trainDetails
    # Train No does not exist
    else :
        return -1

    # Close the database connection
    con.close()

def isTrainNoExists(trainNo) :
    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    # Prepare query to check if Train No exists
    query = f'SELECT EXISTS(SELECT 1 FROM Trains WHERE train_no = \'{trainNo}\' LIMIT 1)'
    cur.execute(query)
    isTrainNoExists = cur.fetchone()[0]
    # print(isTrainNoExists)

    # Close the database connection
    con.close()

    # What to return
    if (isTrainNoExists == 1) :
        return True
    else :
        return False

def getAllTrainDetails() :
    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    query = f'SELECT * FROM Trains'
    cur.execute(query)
    allTrainDetails = cur.fetchall()

    # Close the database connection
    con.close()

    return allTrainDetails


# print(getTrainDetails(12345))
# print(getAllTrainDetails())

# allTrainDetails = getAllTrainDetails()
# for row in allTrainDetails :
#     print(row)

def askTrainDetails() :
    # returns Train details

    trainNo = int(input('Enter Train Number [Eg. 12345]: '))
    trainName = input('Enter Train Name [Eg. Duronto Express]: ')
    d0 = input('Runs on Sunday [Eg. True/False: ')
    d1 = input('Runs on Monday [Eg. True/False: ')
    d2 = input('Runs on Tuesday [Eg. True/False: ')
    d3 = input('Runs on Wednesday [Eg. True/False: ')
    d4 = input('Runs on Thursday [Eg. True/False: ')
    d5 = input('Runs on Friday [Eg. True/False: ')
    d6 = input('Runs on Saturday [Eg. True/False: ')
    startTime = int(input('Train start time [Eg. 1030 if 10:30]: '))
    firstStationNo = int(input('Enter First Station No [Eg. 1]: '))
    speed = int(input('Enter Speed [Eg. 120]: '))
    noOfCoachA = int(input('Enter No of Coach A [Eg. 20]: '))
    noOfCoachB = int(input('Enter No of Coach B [Eg. 40]: '))
    noOfCoachC = int(input('Enter No of Coach C [Eg. 100]: '))
    fairPerKm = int(input('Enter Fair per Km [Eg. 1]: '))
    lastStationNo = int(input('Enter Last Station No. [Eg. 33]: '))

    return trainNo,trainName,d0,d1,d2,d3,d4,d5,d6,startTime,firstStationNo,speed,noOfCoachA,noOfCoachB,noOfCoachC,fairPerKm,lastStationNo

def insertTrainDetails(trainNo,trainName,d0,d1,d2,d3,d4,d5,d6,startTime,firstStationNo,speed,noOfCoachA,noOfCoachB,noOfCoachC,fairPerKm,lastStationNo) :
    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    query = f'INSERT INTO trains VALUES({trainNo},\'{trainName}\',\'{d0}\',\'{d1}\',\'{d2}\',\'{d3}\',\'{d4}\',\'{d5}\',\'{d6}\',{startTime},{firstStationNo},{speed},{noOfCoachA},{noOfCoachB},{noOfCoachC},{fairPerKm},{lastStationNo})'
    cur.execute(query)

    # Commit and close the database connection
    con.commit()
    con.close()

    print('Train added successfully :)')

def adminUI() :
    print('---  Admin UI  ---')

    endLoop = False

    while (endLoop == False) :
        choice = input('\n1. Add Train\n2. Show all Trains\n3. Exit\n: ')

        if (choice == '1') :
            trainDetails = askTrainDetails()
            insertTrainDetails(*trainDetails)

        elif (choice == '2') :
            for row in getAllTrainDetails() :
                print(row)

        elif (choice == '3') :
            endLoop = True

        else :
            print('Invalid Input !')

# adminUI()

# Commit and close the database connection
# con.commit()
# con.close()