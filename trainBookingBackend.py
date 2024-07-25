# trainBookingBackend.py

import seat_availability_search as sas

def isCoachTypeValid(coachType) :
    # returns True if entered coach type is valid else False
    validCoachTypeList = ['A', 'a', 'B', 'b', 'C', 'c']

    if (coachType in validCoachTypeList) :
        return True
    else :
        print('Invalid Coach Type selected !')
        return False

def isValidNoOfPassangers(noOfPassangers) :
    # returns True if no of passengers is valid else False
    if (noOfPassangers.isnumeric()) :
        if (noOfPassangers == '0') :
            print('0 Passengers can\'t be selected !')
            return False
        else :
            return True
    else :
        print('No of Passengers should be a digit !')
        return False

def isValidFoodOrdered(foodOrdered) :
    # returns True if foodOrdered is valid input else False
    validFoodOrderedList = ['Y', 'y', 'N', 'n']

    if (foodOrdered in validFoodOrderedList) :
        return True
    else :
        print('Invalid Input !')
        return False

def calculateTotalFair(noOfPassangers, coachType, amountPerPassangerList) :
    # This dictionary maps A -> 0; B -> 1; C -> 2
    coachTypeToCodeDict = {"a": 0, "b": 1, "c": 2, "A": 0, "B": 1, "C": 2}

    # Calculate total fair
    totalFair = noOfPassangers * amountPerPassangerList[coachTypeToCodeDict[coachType]]

    # round totalFair to 2 decimal places
    totalFair = round(totalFair, 2)
    return totalFair

def isSeatAvailableInCoachType(trainNo, dateNo, coachType, noOfPassangers):
    # Checks and returns boolean whether the seats are available in the coaches

    # Find list of available seats and store in availableSeatsList
    availableSeatsList = sas.searchAvailableSeats(trainNo, dateNo)

    if (coachType == 'a' or coachType == 'A') :
        if (availableSeatsList[0] >= noOfPassangers) :
            # seat available for coachType A
            return True
        else :
            # seat not available for the coachType A
            print("\n! Insufficient seats in Coach A")
            return False

    elif (coachType == 'b' or coachType == 'B') :
        if (availableSeatsList[1] >= noOfPassangers):
            # seat available for coachType B
            return True
        else:
            # seat not available for the coachType B
            print("\n! Insufficient seats in Coach B")
            return False

    elif (coachType == 'c' or coachType == 'C') :
        if (availableSeatsList[2] >= noOfPassangers):
            # seat available for coachType C
            return True
        else:
            # seat not available for the coachType C
            print("\n! Insufficient seats in Coach C")
            return False

    else :
        print("Please enter valid Coach Type !")

