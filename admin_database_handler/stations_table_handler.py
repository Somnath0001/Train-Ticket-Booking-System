# stations_table_handler.py

import sqlite3

# Open connection to perform sql queries
con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
cur = con.cursor()

# cur.execute('''DROP TABLE Stations''')

# cur.execute('''CREATE TABLE IF NOT EXISTS stations
#             (station_no INT PRIMARY KEY,
#             station_name TEXT,
#             dist_upto_next_station REAL)''')

# cur.execute('''INSERT INTO stations VALUES(1,'Howrah',100)''')
# cur.execute('''INSERT INTO stations VALUES(2,'Kharagpore',150)''')
# cur.execute('''INSERT INTO stations VALUES(3,'Vadrak',200)''')
# cur.execute('''INSERT INTO stations VALUES(4,'Bhubaneswar',200)''')
# cur.execute('''INSERT INTO stations VALUES(5,'Vishakapatnam',300)''')
# cur.execute('''INSERT INTO stations VALUES(6,'Bengalore',0)''')

def getAllStationDetails(cur) :
    for row in cur.execute('''SELECT * FROM stations;'''):
        print(row)

def getAllStationDetails():
    # returns list of details of all stations

    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    query = f'SELECT * FROM Stations'
    cur.execute(query)
    allStationsDetails = cur.fetchall()

    # Close the database connection
    con.close()

    return allStationsDetails

def getStationNo(cur, stationName):
    query = f'SELECT station_no FROM stations WHERE station_name = \'{stationName}\''
    cur.execute(query)
    station_no = cur.fetchone()[0]
    return station_no

def getStationName(cur, stationNo):
    query = f'SELECT station_name FROM stations WHERE station_no = \'{stationNo}\''
    cur.execute(query)
    station_name = cur.fetchone()[0]
    return station_name

def isValidStationName(cur, stationName) :
    # The query will return 1 if station name exists in DB else it will return 0
    query = f'SELECT EXISTS(SELECT 2 FROM Stations WHERE station_name = \'{stationName}\' LIMIT 1)'
    cur.execute(query)
    result = cur.fetchone()[0]
    # print(result)
    if (result == 1) :
        return True
    else :
        return False


def getStationDetails(stationNo):
    # returns Station Details if exists else -1

    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    # Station No exists
    if (isStationNoExists(stationNo)):
        # Prepare Query
        query = f'SELECT * FROM Stations WHERE station_no = \'{stationNo}\''
        cur.execute(query)
        stationDetails = cur.fetchone()

        # Close the database connection
        con.close()

        return stationDetails
    # Station No does not exist
    else:
        # Close the database connection
        con.close()
        print('Invalid Station Number !')
        return -1


def isStationNoExists(stationNo):
    # returns True if Station No exists else False

    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    # Prepare query to check if Train No exists
    query = f'SELECT EXISTS(SELECT 1 FROM Stations WHERE station_no = \'{stationNo}\' LIMIT 1)'
    cur.execute(query)
    isStationNoExists = cur.fetchone()[0]
    # print(isStationNoExists)

    # Close the database connection
    con.close()

    # What to return
    if (isStationNoExists == 1):
        return True
    else:
        return False

def isStationNameExists(stationName):
    # returns True if Station No exists else False

    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    # Prepare query to check if Train No exists
    query = f'SELECT EXISTS(SELECT 1 FROM Stations WHERE station_name = \'{stationName}\' LIMIT 1)'
    cur.execute(query)
    isStationNameExists = cur.fetchone()[0]
    # print(isStationNoExists)

    # Close the database connection
    con.close()

    # What to return
    if (isStationNameExists == 1):
        return True
    else:
        return False

def convertStationNameToStationNo(stationName) :
    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    # Station No exists
    if (isStationNameExists(stationName)):
        # Prepare Query
        query = f'SELECT station_no FROM Stations WHERE station_name = \'{stationName}\''
        cur.execute(query)
        stationNo = cur.fetchone()[0]

        # Close the database connection
        con.close()
        return stationNo
    # Station No does not exist
    else:
        # Close the database connection
        con.close()
        print('Invalid Station Name !')
        return -1

def askStationDetails() :
    stationNo = int(input('Enter Station No: '))
    stationName = input('Enter Station Name: ')
    distanceToNextStation = int(input('Enter Distance to next Station: '))
    return stationNo, stationName, distanceToNextStation

def insertStationDetails(cur, stationNo, stationName, distanceToNextStation) :
    query = f'INSERT INTO stations VALUES({stationNo},\'{stationName}\',{distanceToNextStation})'
    cur.execute(query)
    print('Station Details are inserted :)')

def adminUI() :
    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    endLoop = False
    while (endLoop == False) :
        choice = input('\n1. Add Station\n2. Show all Stations\n3. Exit\n: ')
        if (choice == '1') :
            stationDetails = askStationDetails()
            insertStationDetails(cur, stationDetails[0], stationDetails[1], stationDetails[2])
            # Commit changes to database
            con.commit()
        elif (choice == '2') :
            getAllStationDetails(cur)
        elif (choice == '3') :
            endLoop = True
        else :
            print('Invalid Input !')

    # Commit and close the database connection
    con.commit()
    con.close()

# print(getStationNo(cur, 'Howrah'))
# print(isValidStationName(cur, 'Howrah'))
# getAllStationDetails(cur)
# print(isStationNoExists(9))
# print(getStationDetails(9))

# adminUI()
# getAllStationDetails(cur)

# print(isValidStationName(cur, 'SMVT Bengaluru'))
# print(convertStationNameToStationNo('SMVT Bengaluru'))
# print(getAllStationDetails()[2-1])

# Commit and close the database connection
con.commit()
con.close()
