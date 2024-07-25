# trainAvailability.py

import csv
import seat_availability_search as sas
import admin_database_handler.trains_table_handler as tth
import admin_database_handler.stations_table_handler as sth

# trainAvailability
# INPUT
# 1. journeyDate (Calander Date) -> conver to
# 2. srcStation (stationName) -> convert to stationNo
# 3. destStation station (stationName) -> convert to stationNo

# INPUT -> USEFUL VALUE
# 1. Create method : stationToOrderNo()

# OUTPUT
# 1. Available trains (train no.) ->
# 2. With avilable seats for each coach
# 3. fare for 3 types of coaches (consider A=3C, B=2C, C=fare/km)
# 4. total stations in between
# 5. total journey time
# 6. total distance


# [1, 2] Logic behind available trains based on INPUT :
# 1. List all the trains (trainNo) which are running on that day
# 2. Check if stationNo of both srcStation and destStation are present for those trains, make a list
# 3. Check if seats are available for those trains
#   a. CoachA seat available
#   b. CoachB seat available
#   c. CoachC seat available

# Create dictionary for handling days : Sunday = D0
daysToColNoDict = {
            "Sunday" : 2,
            "Monday" : 3,
            "Tuesday" : 4,
            "Wednesday" : 5,
            "Thursday" : 6,
            "Friday" : 7,
            "Saturday" : 8,
            }

def fairCalculation(farePerKm, coachType, distance) : # internal call, ignoring wrong input
    # fairCalculation should return the fair amount# [3] Logic behind Fair Calculation :
    # # CoachA fair = 3 * fare/km * distance
    # # CoachB fair = 2 * fare/km * distance
    # # CoachC fair = fare/km * distance
    if (coachType == 1) :
        return 3 * farePerKm * distance
    elif (coachType == 2) :
        return 2 * farePerKm * distance
    elif (coachType == 3) :
        return farePerKm * distance
    else :
        return 0

def noOfStationsBetween(srcStationNo, destStationNo) : # internal call, ignoring wrong input
    # [4] Logic behind Total Stations Calculation :
    # stationNo of destStation - stationNo of srcStation + 1

    if (srcStationNo > destStationNo) :
        return srcStationNo - destStationNo + 1
    else :
        return destStationNo - srcStationNo + 1

def calcDistance (stationNoOfSrcStation, stationNoOfDestStation) :
    print(f'Src stn no - {stationNoOfSrcStation}; Dest stn no - {stationNoOfDestStation}')
    allStationsDetails = sth.getAllStationDetails()

    # When stationNo of srcStation < stationNo of destStation
    if (stationNoOfSrcStation == -1):
        print('Invalid Source Station !')
        return -1
    elif (stationNoOfDestStation == -1) :
        print('Invalid Destination Station !')
        return -1
    elif (stationNoOfSrcStation < stationNoOfDestStation) :
        # print('[DEBUG] Calculation for forward direction')
        distance = 0
        while (stationNoOfSrcStation < stationNoOfDestStation) :
            distance += distuptoNextStation(stationNoOfSrcStation, allStationsDetails)
            stationNoOfSrcStation += 1
        return distance

    # When stationNo of srcStation > stationNo of destStation
    elif (stationNoOfSrcStation > stationNoOfDestStation) : # (6,1)
        # print('[DEBUG] Calculation for reverse direction')
        distance = 0
        while (stationNoOfDestStation < stationNoOfSrcStation):
            # print('stationNoOfSrcStation: ',stationNoOfSrcStation, '-- stationNoOfDestStation: ',stationNoOfDestStation)
            # print('distance: ', distance)
            stationNoOfSrcStation -= 1
            distance += distuptoNextStation(stationNoOfSrcStation, allStationsDetails)
            # print('distance: ', distance)
        return distance

    # When stationNoOfSrcStation = stationNoOfDestStation
    else : # (stationNoOfSrcStation == stationNoOfDestStation)
        return 0

def calcTotalTime(trainNo, srcStationNo, distStationNo) : # internal call, ignoring wrong input
    # [5] Logic behind Total Time Calculation :
    # time = distance between srcStation and destStation / speed of the train
    speed = int(trainDetails(trainNo)[11])
    # print(f'Speed for calculating Total Time : {speed}')
    totalTime = calcDistance(srcStationNo, distStationNo) / speed
    return totalTime

def calcTotalTime(trainNo, totalDistance) : # internal call, ignoring wrong input
    # [5] Logic behind Total Time Calculation :
    # time = distance between srcStation and destStation / speed of the train
    speed = trainDetails(trainNo)[11]
    # print(f'Speed for calculating Total Time : {speed}')
    totalTime = totalDistance / speed
    return totalTime

# Further implementation needed :
# map 1 month data for trains

# def convertStationNameToStationNo (stationName) : # return type : int
#     # returns station no. for the station
#     with open('../train_ticket_booking_system/stations.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader :
#             if (row[1] == stationName) :
#                 return int(row[0])
#         print('Invalid stationName !')
#         return -1

def getFairPerKm (trainNo) :
    # return fairPerKm value for the train
    return float(trainDetails(trainNo)[15])

def getSpeed (trainNo) :
    pass # return speed of the train

def distuptoNextStation(stationNo, allStationsDetails) :
    # return distUptoNextStation value of stationNo
    detailsOfStation = allStationsDetails[stationNo - 1]
    return detailsOfStation[2]

# def distuptoNextStation(stationNo) :
#     # return distUptoNextStation value of stationNo
#     detailsOfStation = stationDetails(stationNo)
#     if (detailsOfStation == -1) :
#         return -1
#     else :
#         return detailsOfStation[2] # check if typing is needed

# get trainDetails by trainNo
# takes trainNO as parameter
# returns all details of the train from trains.csv file
def trainDetails(trainNo) :
    # returns trainDetails if exists else -1
    trainDetails = tth.getTrainDetails(trainNo)
    return trainDetails

# def trainDetails(trainNo) :
#     # returns trainDetails if exists else -1
#     with open('trains.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader :
#             #print('test - ',type(int(row[0])), 'trainNo - ',type(trainNo))
#             if (int(row[0]) == trainNo) :
#                 # return entire details
#                 #print(row)
#                 return row
#         # if trainNo is not found
#         print('Invalid trainNo !')
#         return -1

def stationDetails(stationNo) :
    stationDetails = sth.getStationDetails(stationNo)
    return stationDetails

# def stationDetails(stationNo) :
#     with open('../train_ticket_booking_system/stations.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader :
#             if (int(row[0]) == stationNo) :
#                 return row
#         # if trainNo is not found
#         print('Invalid stationNo !')
#         return -1

def isForwordJourney(srcStationNo, destStationNo) :
    # checks if the journey is forward : return type : bool
    if (srcStationNo < destStationNo) :
        # print("[DEBUG] Forward Journey")
        return True
    else :
        # print("[DEBUG] Rerverse Journey")
        return False

def calculateEndTime(startTime, duration) :
    # returns end time of the train journey
    # duration : float
    # duration in Hours to Hours and minutes
    durationInMinute = duration * 60
    durationInMinute = int(round(durationInMinute, 0))
    # print('durationInMinute: ', durationInMinute, ' Mins')

    durationHour = durationInMinute // 60
    durationMinute = durationInMinute % 60
    # print('End Time: ',durationHour, ' Hrs ', durationMinute, ' Mins')

    startTimeHour = int(str(startTime)[:2])
    startTimeMinute = int(str(startTime)[2:4])
    # print('Start Time: ',startTimeHour, ' Hrs ', startTimeMinute, ' Mins')

    endTimeMinute = startTimeMinute + durationMinute
    hourCarry = endTimeMinute // 60
    endTimeMinute = endTimeMinute % 60
    endTimeHour = startTimeHour + durationHour + hourCarry
    dayCarry = endTimeHour // 24
    endTimeHour = endTimeHour % 24

    dayCarryPrefix = '+' + str(dayCarry) + ' '

    endTime = int(str(endTimeHour) + str(endTimeMinute))
    endTimeStr = dayCarryPrefix + str(endTimeHour).zfill(2) + str(endTimeMinute).zfill(2)
    return endTime, endTimeStr

# def searchAvailableTrains(journeyDate, srcStationNo, destStationNo) : # (Tuesday, Howrah, Bengalore)
#     # returns list of trains (trainNo : type- int)
#     # 1. List all the trains (trainNo) which are running on that day
#     # 2. Check if stationNo of both srcStation and destStation are present for those trains, make a list
#     trainNoList = []
#     # loop thourgh "trains.txt"
#     with open("trains.csv", "r") as file :
#         reader = csv.reader(file)
#         # loop through all the rows of the reader
#         for row in reader :
#             # check if particular DX field is True
#             # print('trainNo:', row[0], 'Runs:', type(row[daysToColNoDict[journeyDate]]))
#             if (row[daysToColNoDict[journeyDate]] == 'True') :
#                 # print('[DEBUG] Train runs on this day')
#                 # check if stationNo of srcStation is between firstStationNo and lastStationNo (inclusive)
#                 if (isForwordJourney(srcStationNo, destStationNo)):  # firstStationNo is always lesser
#                     # print("channel 1")
#                     # print(srcStationNo, row[10], row[16])
#                     if (srcStationNo >= int(row[10]) and srcStationNo <= int(row[16])):  # (srcStationNo >= firstStaionNo [10] or srcStationNo <= lastStationNo [16])
#                         # print('[DEBUG] srcStaionNo is valid')
#                         # check if stationNo of destStation is between firstStationNo and lastStationNo (inclusive)
#                         # print(destStationNo, row[10], row[16])
#                         if (destStationNo >= int(row[10]) and destStationNo <= int(row[16])):
#                             # print('[DEBUG] destStationNo is valid')
#                             # append the trainNo in trainNoList
#                             trainNoList.append(int(row[0]))
#                             # print("[DEBUG] trainNo", int(row[0]), "is appeded")
#                         else :
#                             pass
#                             #print('[DEBUG] destStationNo is not valid!')
#                     else :
#                         # print('[DEBUG] srcStaionNo is not valid!')
#                         pass
#                 else:
#                     # print("channel 2")
#                     # print(srcStationNo, row[10], row[16])
#                     if (srcStationNo >= int(row[10]) and srcStationNo <= int(row[16])):
#                         # print('[DEBUG] srcStaionNo is valid')
#                         # check if stationNo of destStation is between firstStationNo and lastStationNo (inclusive)
#                         # print(destStationNo, row[10], row[16])
#                         if (destStationNo >= int(row[10]) and destStationNo <= int(row[16])):
#                             # print('[DEBUG] destStationNo is valid')
#                             # append the trainNo in trainNoList
#                             trainNoList.append(int(row[0]))
#                             # print("[DEBUG] trainNo", int(row[0]), "is appeded")
#                         else :
#                             # print('[DEBUG] destStationNo is not valid !')
#                             pass
#                     else :
#                         # print('[DEBUG] srcStaionNo is not valid!')
#                         pass
#             else :
#                 # print('[DEBUG] Train does not run on this day')
#                 pass
#     # return trainNoList
#     return trainNoList

def searchAvailableTrains(journeyDate, srcStationNo, destStationNo) : # (Tuesday, Howrah, Bengalore)
    # returns list of trains (trainNo : type- int)
    # 1. List all the trains (trainNo) which are running on that day
    # 2. Check if stationNo of both srcStation and destStation are present for those trains, make a list

    # Initialize list of available trains
    trainNoList = []

    # Get details of all the trains
    allTrainDetails = tth.getAllTrainDetails()

    # loop through all the rows of the allTrainDetails
    for row in allTrainDetails:
        # check if particular DX field is True
        # print('trainNo:', row[0], 'Runs:', type(row[daysToColNoDict[journeyDate]]))
        if (row[daysToColNoDict[journeyDate]] == 'True') :
            # print('[DEBUG] Train runs on this day')
            # check if stationNo of srcStation is between firstStationNo and lastStationNo (inclusive)
            if (isForwordJourney(srcStationNo, destStationNo)):  # firstStationNo is always lesser
                # print("channel 1")
                # print(srcStationNo, row[10], row[16])
                if (srcStationNo >= int(row[10]) and srcStationNo <= int(row[16])):  # (srcStationNo >= firstStaionNo [10] or srcStationNo <= lastStationNo [16])
                    # print('[DEBUG] srcStaionNo is valid')
                    # check if stationNo of destStation is between firstStationNo and lastStationNo (inclusive)
                    # print(destStationNo, row[10], row[16])
                    if (destStationNo >= int(row[10]) and destStationNo <= int(row[16])):
                        # print('[DEBUG] destStationNo is valid')
                        # append the trainNo in trainNoList
                        trainNoList.append(int(row[0]))
                        # print("[DEBUG] trainNo", int(row[0]), "is appeded")
                    else :
                        pass
                        # print('[DEBUG] destStationNo is not valid!')
                else :
                    # print('[DEBUG] srcStaionNo is not valid!')
                    pass
            else:
                # print("channel 2")
                print(srcStationNo, row[10], row[16])
                if (srcStationNo >= int(row[10]) and srcStationNo <= int(row[16])):
                    # print('[DEBUG] srcStaionNo is valid')
                    # check if stationNo of destStation is between firstStationNo and lastStationNo (inclusive)
                    print(destStationNo, row[10], row[16])
                    if (destStationNo >= int(row[10]) and destStationNo <= int(row[16])):
                        # print('[DEBUG] destStationNo is valid')
                        # append the trainNo in trainNoList
                        trainNoList.append(int(row[0]))
                        # print("[DEBUG] trainNo", int(row[0]), "is appeded")
                    else :
                        # print('[DEBUG] destStationNo is not valid !')
                        pass
                else :
                    # print('[DEBUG] srcStaionNo is not valid!')
                    pass
        else :
            # print('[DEBUG] Train does not run on this day')
            pass
    # return trainNoList
    return trainNoList

def trainAvailability(journeyDate, srcStation, destStation):
    # 1. Available trains (train no.) ->
    # print('1')
    srcStationNo = sth.convertStationNameToStationNo(srcStation)
    destStationNo = sth.convertStationNameToStationNo(destStation)
    availableTrains = searchAvailableTrains(journeyDate, srcStationNo, destStationNo)
    # print('2')
    # 2. With avilable seats for each coach
    # need to create one "seats.csv"

    print("Available Trains :")
    # For all the trains need to display below informations
    dateNo = ''

    trainNoList = []
    dateNoList = []
    srcStationList = []
    destStationList = []
    startTimeList = []
    endTimeList = []
    listOfFairOfCoachesList = []

    # print('3')
    for trainNo in availableTrains :
        # 2. With avilable seats for each coach
        dateNo = 'd' + str(daysToColNoDict[journeyDate]-2)
        # print('a')
        availableSeatsList = sas.searchAvailableSeats(trainNo, dateNo)
        # print('a - ends.')
        # print(availableSeatsList)
        # 4. total stations in between
        # print('b')
        totalStations = noOfStationsBetween(srcStationNo, destStationNo)
        # print('b - ends.')
        # 5. total distance
        # print('c')
        totalDistance = calcDistance(srcStationNo, destStationNo)
        # print('c - ends.')
        # 6. total journey time
        # print('d')
        totalTime = calcTotalTime(trainNo, totalDistance)
        # print('d - ends.')
        # 3. fare for 3 types of coaches (consider A=3C, B=2C, C=fare/km)
        # print('e')
        farePerKm = getFairPerKm(trainNo)
        # print('e - ends.')
        fairOfCoachA = fairCalculation(farePerKm, 1, totalDistance)
        fairOfCoachB = fairCalculation(farePerKm, 2, totalDistance)
        fairOfCoachC = fairCalculation(farePerKm, 3, totalDistance)

        fairOfCoachesList = [fairOfCoachA, fairOfCoachB, fairOfCoachC]

        # print('f')
        trainDetail = trainDetails(trainNo)
        # print('f - ends.')
        trainName = trainDetail[1]
        startTime = trainDetail[9]

        timeTakenToReachJourneyStartStation = calcTotalTime(trainNo, calcDistance(1, srcStationNo))
        newStartTime = calculateEndTime(startTime, timeTakenToReachJourneyStartStation)[1]
        # print(f'New Start Time: {newStartTime}')

        endTime = calculateEndTime(startTime, totalTime)[1] # need correction
        # Print All Details
        print('- - - - - - - - - -- - - - - - - - - -- - - - - - - - - -- - - - - - - - -')
        print("+Train No:",trainNo,"| Train Name:",trainName,'\n','From:',srcStation,"| Start Time:",newStartTime,'\n','Dest:',destStation,"| End Time:",endTime,'\n',"Coach A Fair:",round(fairOfCoachA, 2),"| Coach B Fair:",round(fairOfCoachB, 2),"| Coach C Fair:",round(fairOfCoachC, 2),'\n',"No of Stations:",totalStations,"| Total Distance(km):",totalDistance,"| Journey Time(Hrs):",round(totalTime, 2), '\n Available Seats :\n Coach A:',availableSeatsList[0],'| Coach B:',availableSeatsList[1],'| Coach C:',availableSeatsList[2])
        print('- - - - - - - - - -- - - - - - - - - -- - - - - - - - - -- - - - - - - - -')
        trainNoList.append(trainNo)
        dateNoList.append(dateNo)
        srcStationList.append(srcStation)
        destStationList.append(destStation)
        startTimeList.append(newStartTime)
        endTimeList.append(endTime)
        listOfFairOfCoachesList.append(fairOfCoachesList)

    # print('4')
    # return list of all details of all available trains
    return (trainNoList, dateNoList, srcStationList, destStationList, startTimeList, endTimeList, listOfFairOfCoachesList)


# Test
# print(calculateEndTime(1030, 52))
# print(stationDetails(1)[2])