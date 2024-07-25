# PassangerDetailsUI.py

import sqlite3
import admin_database_handler.passanger_table_handler as pth
import paymentPageUI as payui
import userDashboardUI as udui
import passangerDetailsBackend as pdb

def askName() :
    # Asks for Name and returns the same
    name = input('\tEnter Passenger Name: ')
    return name

def askAge() :
    # Asks for Age and returns the same
    age = input('\tEnter Age: ')
    return age

def askGender() :
    # Asks for Gender and returns the same
    gender = input('\tEnter Gender [M, F, O]: ')
    return gender

def askIdcardType() :
    # Asks for Id Card Type and returns the same
    idCardType = input('\tEnter Id Card Type [Aadhar, Voter]: ')
    return idCardType

def askIdCardNo() :
    # Asks for Id Card No. and returns the same
    idCardNo = input('\tEnter Id Card No.: ')
    return idCardNo

def askPassangerDetials(i, bookIdLists) :
    # Asks and returns name, age, gender, idCardType, idCardNo of Passenger

    print(f'\nFill Details of Passenger {i + 1} with Book Id - {bookIdLists[i]}')

    # Keep asking name until user inputs a valid input
    name = askName()
    while (pdb.isValidName(name) == False) :
        name = askName()

    # Keep asking age until user inputs a valid input
    age = askAge()
    while (pdb.isValidAge(age) == False) :
        age = askAge()
    # Convert to int (As the age is valid)
    age = int(age)

    # Keep asking gender until user inputs a valid input
    gender = askGender()
    while (pdb.isValidGender(gender) == False) :
        gender = askGender()

    # Keep asking id card until user inputs a valid one
    idCardType = askIdcardType()
    while (pdb.isValidIdCardType(idCardType) == False) :
        idCardType = askIdcardType()

    # Keep asking id card no until user inputs a valid one
    idCardNo = askIdCardNo()
    while (pdb.isValidIdCardNo(idCardNo, idCardType) == False) :
        idCardNo = askIdCardNo()

    return name, age, gender, idCardType, idCardNo

def passangerDetailsUI(userId, noOfPassangers, bookIdLists, totalAmount) :
    print('\n---  Passanger Details UI  ---\n')
    print(f'Please fill detials of {noOfPassangers} passengers :')

    # Ask Details for each Passengers
    for i in range(noOfPassangers) :
        # Ask details for each Passenger and store it
        passangerDetials = askPassangerDetials(i, bookIdLists)

        name = passangerDetials[0]
        age = passangerDetials[1]
        gender = passangerDetials[2]
        idCardType = passangerDetials[3]
        idCardNo = passangerDetials[4]

        # Open connection to perform sql queries
        con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
        cur = con.cursor()

        # Set PNR No as 'null' for now. PNR No will be generated once payment is successful
        pnrNo = 'null'

        # save info to Passagner Table
        # print(cur, bookIdLists[i], name, age, gender, idCardType, idCardNo, pnrNo, userId)

        # Insert Passenger Details into the Table
        pth.insertPassangerDetails(cur, bookIdLists[i], name, age, gender, idCardType, idCardNo, pnrNo, userId)

        # Test
        print('[ DEBUG ] Passenger Details: ')
        pth.getPassangerDetailsByPassangerId(cur, bookIdLists[i])

        # Commit and close connection
        con.commit()
        con.close()


    print(f'\nTotal Amount To Pay : {totalAmount}')

    # Ask option from user and perform accordingly
    option = input('\n1. Proceed to Payment\n2. Exit to Dashboard\n: ')
    if (option == '1') :
        print('Redirecting to Payment Page UI...')
        payui.paymentPageUI(userId, totalAmount, bookIdLists)
    elif (option == '2') :
        print('Redirecting to User Dashboard...')
        # udui.userDashboardUI(userId)
    else :
        print('! Invalid Input')


# Test Starter
# passangerDetailsUI('som1', 1, [37], 2000)

