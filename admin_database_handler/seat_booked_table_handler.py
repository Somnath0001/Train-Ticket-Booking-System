# seat_booked_table_handler.py

import sqlite3

# Open database connection to perform sql queries
con = sqlite3.connect('ticket_booking.db')
cur = con.cursor()

trainNO = 12345
dateNo = 0
# print('d'+str(dateNo))

def generateCreateQuery():
    for trainNo in range(12345, 12446):
        for dateNo in range(0, 7):
            tableName = 'd' + str(dateNo) + '_' + str(trainNo)
            # print(tableName)

            queryColumns = '('
            # code for coachA
            coachType = 'a'
            for coachNo in range(1, 4):
                columnName = coachType + str(coachNo)
                # print(columnName)
                queryColumns += columnName + ' INT,'

            # code for coachB
            coachType = 'b'
            for coachNo in range(1, 8):
                columnName = coachType + str(coachNo)
                # print(columnName)
                queryColumns += columnName + ' INT,'

            # code for coachC
            coachType = 'c'
            for coachNo in range(1, 13):
                columnName = coachType + str(coachNo)
                # print(columnName)
                queryColumns += columnName + ' INT,'

            queryColumns = queryColumns.rstrip(queryColumns[-1]) + ')'
            # print(queryColumns)
            createQuery = f"CREATE TABLE IF NOT EXISTS {tableName}{queryColumns}"
            insertQuery = f"INSERT INTO {tableName} VALUES(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)"
            selectQuery = f"SELECT * FROM {tableName}"
            # print(createQuery)
            cur.execute(createQuery)
            cur.execute(insertQuery)
            for row in cur.execute(selectQuery):
                print(row)


# generateCreateQuery()

# cur.execute('''INSERT INTO d0_12345 VALUES(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)''')
#
# for row in cur.execute('''SELECT * FROM d0_12345'''):
#     print(row)

# dateNo = d0, trainNO = 12345, coachType = A, coachNo = 1
def getTotalCount(trainNo, dateNo, coachType, coachNo):
    tableName = dateNo + '_' + str(trainNo)
    columnName = coachType + str(coachNo)
    print(f"Table Name: {tableName}")
    print(f"Column Nmae: {columnName}")
    selectQuery = f"SELECT {columnName} FROM {tableName}"
    for row in cur.execute(selectQuery):
        return row[0]

# dateNo = d0, trainNO = 12345, coachType = A, coachNo = 1, value = 5
def setTotalCount(trainNo, dateNo, coachType, coachNo, value):
    tableName = dateNo + '_' + str(trainNo)
    columnName = coachType + str(coachNo)
    print(f"Table Name: {tableName}")
    print(f"Column Nmae: {columnName}")
    updateQuery = f"UPDATE {tableName} SET {columnName} = {value}"
    cur.execute(updateQuery)

# print(getTotalCount(12345, 'd0', 'A', 1))
# setTotalCount(12345, 'd0', 'A', 1, 5)
# print(getTotalCount(12345, 'd0', 'A', 1))

# Version 2

def generateCreateQueryV2():
    for trainNo in range(12345, 12446):
        for dateNo in range(0, 7):
            tableName1 = 'd' + str(dateNo) + '_' + str(trainNo)

            # code for coachA
            coachType = 'a'
            tableName = tableName1 + '_' + coachType
            print(tableName)
            # First execute create query
            columnNames = '(seat_no,'
            zeroValues = ''
            for coachNo in range(1, 4):
                columnNames += coachType + str(coachNo) + ' INT,'
                zeroValues += ',0'
            columnNames = columnNames.rstrip(columnNames[-1]) + ')'
            createQuery = f"CREATE TABLE IF NOT EXISTS {tableName}{columnNames}"
            print(createQuery)

            # Execute INSERT query
            for seatNo in range(1, 31):
                insertQuery = f"INSERT INTO {tableName} VALUES({seatNo}{zeroValues})"
                print(insertQuery)

            # code for coachB
            coachType = 'b'
            tableName = tableName1 + '_' + coachType
            print(tableName)
            columnNames = '(seat_no,'
            zeroValues = ''
            for coachNo in range(1, 8):
                columnNames += coachType + str(coachNo) + ' INT,'
                zeroValues += ',0'
            columnNames = columnNames.rstrip(columnNames[-1]) + ')'
            createQuery = f"CREATE TABLE IF NOT EXISTS {tableName}{columnNames}"
            print(createQuery)

            # Execute INSERT query
            for seatNo in range(1, 46):
                insertQuery = f"INSERT INTO {tableName} VALUES({seatNo}{zeroValues})"
                print(insertQuery)

            # code for coachC
            coachType = 'c'
            tableName = tableName1 + '_' + coachType
            print(tableName)
            columnNames = '(seat_no,'
            zeroValues = ''
            for coachNo in range(1, 13):
                columnNames += coachType + str(coachNo) + ' INT,'
                zeroValues += ',0'
            columnNames = columnNames.rstrip(columnNames[-1]) + ')'
            createQuery = f"CREATE TABLE IF NOT EXISTS {tableName}{columnNames}"
            print(createQuery)

            # Execute INSERT query
            for seatNo in range(1, 71):
                insertQuery = f"INSERT INTO {tableName} VALUES({seatNo}{zeroValues})"
                print(insertQuery)


# generateCreateQueryV2()


# Version 3

def generateCreateQueryV3(trainNoStart, totalTrain, days, noOfCoachA, noOfSeatsInCoachA, noOfCoachB, noOfSeatsInCoachB, noOfCoachC, noOfSeatsInCoachC):
    trainNoEnd = trainNoStart + totalTrain
    for trainNo in range(trainNoStart, trainNoEnd+1):
        for dateNo in range(0, days):
            tableName1 = 'd' + str(dateNo) + '_' + str(trainNo)

            # code for coachA
            coachType = 'a'
            tableName = tableName1 + '_' + coachType
            print(tableName)
            # First execute create query
            columnNames = '(seat_no,'
            zeroValues = ''
            for coachNo in range(1, noOfCoachA+1):
                columnNames += coachType + str(coachNo) + ' INT,'
                zeroValues += ',0'
            columnNames = columnNames.rstrip(columnNames[-1]) + ')'
            createQuery = f"CREATE TABLE IF NOT EXISTS {tableName}{columnNames}"
            print(createQuery)
            cur.execute(createQuery)

            # Execute INSERT query
            for seatNo in range(1, noOfSeatsInCoachA+1):
                insertQuery = f"INSERT INTO {tableName} VALUES({seatNo}{zeroValues})"
                print(insertQuery)
                cur.execute(insertQuery)

            # code for coachB
            coachType = 'b'
            tableName = tableName1 + '_' + coachType
            print(tableName)
            columnNames = '(seat_no,'
            zeroValues = ''
            for coachNo in range(1, noOfCoachB+1):
                columnNames += coachType + str(coachNo) + ' INT,'
                zeroValues += ',0'
            columnNames = columnNames.rstrip(columnNames[-1]) + ')'
            createQuery = f"CREATE TABLE IF NOT EXISTS {tableName}{columnNames}"
            print(createQuery)
            cur.execute(createQuery)

            # Execute INSERT query
            for seatNo in range(1, noOfSeatsInCoachB+1):
                insertQuery = f"INSERT INTO {tableName} VALUES({seatNo}{zeroValues})"
                print(insertQuery)
                cur.execute(insertQuery)

            # code for coachC
            coachType = 'c'
            tableName = tableName1 + '_' + coachType
            print(tableName)
            columnNames = '(seat_no,'
            zeroValues = ''
            for coachNo in range(1, noOfCoachC+1):
                columnNames += coachType + str(coachNo) + ' INT,'
                zeroValues += ',0'
            columnNames = columnNames.rstrip(columnNames[-1]) + ')'
            createQuery = f"CREATE TABLE IF NOT EXISTS {tableName}{columnNames}"
            print(createQuery)
            cur.execute(createQuery)

            # Execute INSERT query
            for seatNo in range(1, noOfSeatsInCoachC+1):
                insertQuery = f"INSERT INTO {tableName} VALUES({seatNo}{zeroValues})"
                print(insertQuery)
                cur.execute(insertQuery)


# generateCreateQueryV3(12345, 100, 30, 3, 30, 7, 45, 12, 70)

# dateNo = d0, trainNO = 12345, coachType = A, coachNo = 1
def isBooked(trainNo, dateNo, coachType, coachNo, seatNo):
    tableName = dateNo + '_' + str(trainNo) + '_' + coachType
    columnName = coachType + str(coachNo)
    # print(f"Table Name: {tableName}")
    # print(f"Column Nmae: {columnName}")
    selectQuery = f"SELECT {columnName} FROM {tableName} WHERE seat_no = {seatNo}"
    for row in cur.execute(selectQuery):
        return row[0]

# dateNo = d0, trainNO = 12345, coachType = A, coachNo = 1, value = 5
# value = 0 = notBooked; value = 1 = booked; value = other = define
def bookSeat(cur, trainNo, dateNo, coachType, coachNo, seatNo, value=1):
    tableName = dateNo + '_' + str(trainNo) + '_' + coachType
    columnName = coachType + str(coachNo)
    # print(f"Table Name: {tableName}")
    # print(f"Column Nmae: {columnName}")
    updateQuery = f"UPDATE {tableName} SET {columnName} = {value} WHERE seat_no = {seatNo}"
    cur.execute(updateQuery)

def unBookSeat(cur, trainNo, dateNo, coachType, coachNo, seatNo, value=0):
    tableName = dateNo + '_' + str(trainNo) + '_' + coachType
    columnName = coachType + str(coachNo)
    # print(f"Table Name: {tableName}")
    # print(f"Column Nmae: {columnName}")
    updateQuery = f"UPDATE {tableName} SET {columnName} = {value} WHERE seat_no = {seatNo}"
    cur.execute(updateQuery)

def lowestEmptySeatNo(trainNo, dateNo, coachType, coachNo):
    lowestEmptySeatNo = 0
    tableName = dateNo + '_' + str(trainNo) + '_' + coachType
    columnName = coachType + str(coachNo)
    # print('tableName: ', tableName)
    # print('columnName: ', columnName)
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()
    query = f"SELECT min(seat_no) FROM {tableName} WHERE {columnName} = 0"
    try :
        cur.execute(query)
        result = cur.fetchone()[0]
        # print('result: ', result)
        if result is None :
            # there is no row/record available in DB
            lowestEmptySeatNo = -1
        else :
            # row/record is available in DB
            lowestEmptySeatNo = result
    except Exception as e :
        print('Returned Type Error : None')
        print(e)
    return lowestEmptySeatNo

    # con.commit()
    con.close()

def lowestEmptyCoachNo(trainNo, dateNo, coachType):
    global lowestEmptySeatNo
    tableName = dateNo + '_' + str(trainNo) + '_' + coachType
    # con = sqlite3.connect('admin_database_handler/ticket_booking.db')
    # cur = con.cursor()

    # iterate through each coachNo
    if (coachType == 'a' or coachType == 'A'):
        # iterate 3 times
        for coachNo in range(1, 4):
            # print('coachNo: ', coachNo)
            # check if there is any empty seat
            resultOfLowestEmptySeatNo = lowestEmptySeatNo(trainNo, dateNo, coachType, coachNo)
            # print(f"lowestEmptySeatNo: {resultOfLowestEmptySeatNo}")
            # if not -1, that means seat available then return the current coachNo
            if (resultOfLowestEmptySeatNo != -1 ):
                return coachNo, resultOfLowestEmptySeatNo
            # else continue
        # didn't get empty seat in all coaches
        return coachNo, resultOfLowestEmptySeatNo

    elif (coachType == 'b' or coachType == 'B'):
        # iterate 7 times
        for coachNo in range(1, 8):
            # print('coachNo: ', coachNo)
            # check if there is any empty seat
            resultOfLowestEmptySeatNo = lowestEmptySeatNo(trainNo, dateNo, coachType, coachNo)
            # print(f"lowestEmptySeatNo: {resultOfLowestEmptySeatNo}")
            # if not -1, that means seat available then return the current coachNo
            if (resultOfLowestEmptySeatNo != -1):
                return coachNo, resultOfLowestEmptySeatNo
            # else continue
        # didn't get empty seat in all coaches
        return coachNo, resultOfLowestEmptySeatNo

    elif (coachType == 'c' or coachType == 'C'):
        # iterate 12 times
        for coachNo in range(1, 13):
            # print('coachNo: ', coachNo)
            # check if there is any empty seat
            resultOfLowestEmptySeatNo = lowestEmptySeatNo(trainNo, dateNo, coachType, coachNo)
            # print(f"lowestEmptySeatNo: {resultOfLowestEmptySeatNo}")
            # if not -1, that means seat available then return the current coachNo
            if (resultOfLowestEmptySeatNo != -1):
                return coachNo, resultOfLowestEmptySeatNo
            # else continue
        # didn't get empty seat in all coaches
        return coachNo, resultOfLowestEmptySeatNo

    # con.commit()
    # con.close()

# print(isBooked(12345, 'd0', 'a', 1, 3))
# bookSeat(12345, 'd0', 'a', 1, 3) # 5th one is optional parameter: development use
# print(isBooked(12345, 'd0', 'a', 1, 3))
# unBookSeat(12345, 'd0', 'a', 1, 3)
# print(isBooked(12345, 'd0', 'a', 1, 3))


# bookSeat(12345, 'd0', 'a', 1, 1)
# bookSeat(12345, 'd0', 'a', 1, 2)
# bookSeat(12345, 'd0', 'a', 1, 3)
# bookSeat(12345, 'd0', 'a', 1, 4)
# bookSeat(12345, 'd0', 'b', 1, 1)
# bookSeat(12345, 'd0', 'b', 1, 2)
# bookSeat(12345, 'd0', 'c', 1, 1)

# Commit and close the database connection
con.commit()
con.close()
