# train_booking_UI.py

import ticketBookingBackend as tbb
import seat_availability_search as sas
import PassangerDetailsUI as pdui
import userDashboardUI as udui
import trainBookingBackend as trainbb

def askCoachType() :
    # Asks for Coach Type and returns Coach Type
    coachType = input('Enter Coach Type [a, b, c]: ')
    return coachType

def askNoOfPassangers() :
    # Asks for No. of passangers and returns the same as String
    noOfPassangers = input('Enter no. of passengers: ')
    return noOfPassangers

def askFoodOrdered() :
    # Asks whether food is needed or not and returns the same
    foodOrdered = input('Enter \'Y\' to order food else \'N\': ')
    return foodOrdered


def trainBookingUI(userId, trainNo, dateNo, journeyFrom, journeyTo, journeyFromTime, journeyToTime, amountPerPassangerList):
    print('\n---  Train Booking UI  ---\n')
    print(f"You are going to book Train No: {trainNo}")

    # keep asking coach type until user inputs a valid input
    coachType = askCoachType()
    while (trainbb.isCoachTypeValid(coachType) == False) :
        coachType = askCoachType()
    # Convert coach type to lower case (A -> a; B -> b; C -> c)
    coachType = coachType.lower()

    # Keep asking no of passengers until user inputs a valid input
    noOfPassangers = askNoOfPassangers()
    while (trainbb.isValidNoOfPassangers(noOfPassangers) == False) :
        noOfPassangers = askNoOfPassangers()
    # Convert to int (As noOfPassangers is valid)
    noOfPassangers = int(noOfPassangers)

    # Keep asking food ordered until user inputs a valid input
    foodOrdered = askFoodOrdered()
    while (trainbb.isValidFoodOrdered(foodOrdered) == False) :
        foodOrdered = askFoodOrdered()
    # Convert foodOrdered to uppercase (y -> Y; n -> N)
    foodOrdered = foodOrdered.upper()

    if (trainbb.isSeatAvailableInCoachType(trainNo, dateNo, coachType, noOfPassangers)) :
        # Calculate total amount and store it
        totalAmount = trainbb.calculateTotalFair(noOfPassangers, coachType, amountPerPassangerList)
        print(f'[ DEBUG ] Total Amount: {totalAmount}')

        # Search available seat numbers and store the list
        bookIdLists = tbb.bookAvailableSeat(trainNo, dateNo, coachType, noOfPassangers, journeyFrom, journeyTo, journeyFromTime, journeyToTime, foodOrdered)

        # Ask for user choice
        option = input('\n1. Add Passenger Details\n2. Exit to Dashboard\nPlease enter a number to choose option [Eg. 1]\n: ')
        if (option == '1') :
            pdui.passangerDetailsUI(userId, noOfPassangers, bookIdLists, totalAmount)
        elif (option == '2') :
            udui.userDashboardUI(userId)
        else :
            print('Please Enter Valid Option !')

    else :
        # if not valid coach type (empty coaches)
        print('Please find the below... ')
        # Get available seats list and store it
        availableSeatsList = sas.searchAvailableSeats(trainNo, dateNo)
        print('\n Available Seats :\n Coach A:',availableSeatsList[0],'| Coach B:',availableSeatsList[1],'| Coach C:',availableSeatsList[2],'\n')

        # Call Train Booking Ui again
        trainBookingUI(userId, trainNo, dateNo, journeyFrom, journeyTo, journeyFromTime, journeyToTime, amountPerPassangerList)

