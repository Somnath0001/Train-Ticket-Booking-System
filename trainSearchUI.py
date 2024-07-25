# trainSearchUI.py

import sqlite3
import trainAvailability as ta
import train_booking_UI as tbui
import userDashboardUI as udui
import admin_database_handler.stations_table_handler as sth

def askOption(userId) :
    # Asks for user input and performs accordingly
    choice = input('1. Search Trains\n2. Exit\nPlease enter a number to choose option [Eg. 1]\n: ')
    if (choice == '1'):
        search(userId)
    elif (choice == '2'):
        print('Redirecting to User Dashboard UI...')
        # udui.userDashboardUI(userId)
    else:
        print('Invalid Input !\n')
        askOption(userId)

def isValidJourneyDate(journeyDate) :
    # returns True if Journey date is valid else False
    journeyDateList = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if (journeyDate in journeyDateList) :
        return True
    else :
        return False

def askJourneyDate() :
    # Asks for journey date and returns journey date
    journeyDate = input("Enter Journey Date (Eg.- Sunday) : ")
    return journeyDate

def askSourceStation() :
    # Asks for source station and returns source station
    sourceStation = input("Enter Source Station (Eg. - Howrah) : ")
    return sourceStation

def askDestinationStation() :
    # Asks for destination station and returns destination station
    destinationStation = input("Enter Destination Station (Eg. - SMVT Bengaluru) : ")
    return destinationStation

def askTrainNo() :
    # Asks for trainNo and returns selected Train No
    selectedTrainNo = input("\nEnter train number to book ticket (Press 0 to Exit): ")
    return selectedTrainNo

def isValidTrainNo(trainNo, validTrainNoList) :
    # Train No should be of 5 digits,
    # so check if is numeric
    if (trainNo.isnumeric()) :
        # Check if the numberic value is of 5 digits
        if (len(trainNo) == 5) :
            # Convert to int
            trainNo = int(trainNo)
            # Check whether the trainNo exists in validTrainNoList
            if (trainNo in validTrainNoList):
                return True
            else:
                print('Please choose from Available Train List.')
                return False
        else :
            print('Train No should be of 5 digits.')
            return False
    else :
        print('Train No should be numeric')
        return False


def isTrainNoZero(trainNo) :
    if (trainNo == '0') :
        return True
    else :
        return False

def search(userId) :
    # It will ask user to search and select train for seat booking

    print("\nSearch Trains :")

    # Open Connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    # Keep asking for Journey Date until user inputs a valid input
    journeyDate = askJourneyDate()
    while (isValidJourneyDate(journeyDate) == False) :
        print('Invalid Journey Date !\n')
        journeyDate = askJourneyDate()

    # Keep asking for Source Station until user inputs a valid input
    srcStation = askSourceStation()
    while (sth.isValidStationName(cur, srcStation) == False) :
        print('Invalid Source Station !\n')
        srcStation = askSourceStation()

    # Keep asking for Destination Station until user inputs a valid input
    destStation = askDestinationStation()
    while (sth.isValidStationName(cur, destStation) == False):
        print('Invalid Destination Station !\n')
        destStation = askDestinationStation()

    print()

    # Commit and close connection of database
    con.commit()
    con.close()

    print(f'[ DEBUG ] JourneyDate: {journeyDate} | srcStation: {srcStation} | destStation: {destStation}')

    # Create empty list of available trains
    availableTrainNoList = []

    # Call Train Availability method to get available trains based on date, src, dest
    trainAvailabilityDetails = ta.trainAvailability(journeyDate, srcStation, destStation)
    print(f"[ DEBUG ] trainAvailability returns: {trainAvailabilityDetails}")

    # Store all the available trainNo in the list
    availableTrainNoList = trainAvailabilityDetails[0]

    # Ask user to choose/select the trainNo which he/she wants to book
    selectedTrainNo = askTrainNo()
    # print(f'[ DEBUG ] Selected Train No: {selectedTrainNo}| Available Train No List: {availableTrainNoList}')
    # print(f'[ DEBUG ] isValidTrainNo(selectedTrainNo, availableTrainNoList): {isValidTrainNo(selectedTrainNo, availableTrainNoList)}')
    # print(f'[ DEBUG ] isTrainNoZero : {isTrainNoZero(selectedTrainNo)}')

    # Keep user asking until user inputs either a valid trainNo or 0 to exit
    while (isValidTrainNo(selectedTrainNo, availableTrainNoList) == False and isTrainNoZero(selectedTrainNo) == False) :
        # print(f'[ DEBUG ] Selected Train No: {selectedTrainNo}| Available Train No List: {availableTrainNoList}')
        # print(
        #     f'[ DEBUG ] isValidTrainNo(selectedTrainNo, availableTrainNoList): {isValidTrainNo(selectedTrainNo, availableTrainNoList)}')
        # print(f'[ DEBUG ] isTrainNoZero : {isTrainNoZero(selectedTrainNo)}')
        print('Incorrect Train No !')
        selectedTrainNo = askTrainNo()

    # Convert to int (as it is a valid train no) and store in selectedTrainNo
    selectedTrainNo = int(selectedTrainNo)

    if (selectedTrainNo == 0) :
        # Exit to Train Search UI
        trainSearchUI(userId)
    else :
        print(f'Selected Train No: {selectedTrainNo}')

        # Prepare details of selected Trains
        indexOfSelectedTrainNo = trainAvailabilityDetails[0].index(selectedTrainNo)

        dateNo = trainAvailabilityDetails[1][indexOfSelectedTrainNo]
        journeyFrom = trainAvailabilityDetails[2][indexOfSelectedTrainNo]
        journeyTo = trainAvailabilityDetails[3][indexOfSelectedTrainNo]
        journeyFromTime = trainAvailabilityDetails[4][indexOfSelectedTrainNo]
        journeyToTime = trainAvailabilityDetails[5][indexOfSelectedTrainNo]
        fairOfCoachesList = trainAvailabilityDetails[6][indexOfSelectedTrainNo]

        print(f'[ DEBUG ] Details for Train No {selectedTrainNo} : {userId, selectedTrainNo, dateNo, journeyFrom, journeyTo, journeyFromTime, journeyToTime, fairOfCoachesList}')

        # Call Train Booking UI to book the seat
        tbui.trainBookingUI(userId, selectedTrainNo, dateNo, journeyFrom, journeyTo, journeyFromTime, journeyToTime, fairOfCoachesList)

def trainSearchUI(userId) :
    print('\n---  Train Search UI  ---\n')
    askOption(userId)