# cardDetailsUI.py

import sqlite3
import userDashboardUI as udui
import cardDetailsBackend as cdb


def askCardDetailsOption() :
    # Asks user for option and returns the same
    option = input('1. Show Card Details\n2. Add Card\n3. Delete Card\n4. Exit to Dashboard\n5. Exit\n : ')
    return option

def isValidCardDetailsOption(option) :
    # returns True if option is valid else False
    validCardDetailsOptionList = ['1', '2', '3', '4', '5']
    if (option in validCardDetailsOptionList) :
        return True
    else :
        return False

def cardDetailsUI(userId) :
    print('\n---  Card Details UI  ---\n')

    # Keep asking user for Card Details Option until user inputs a valid input
    option = askCardDetailsOption()
    while (isValidCardDetailsOption(option) == False) :
        option = askCardDetailsOption()

    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    if (option == '1') :
        # Open connection to perform sql queries
        con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
        cur = con.cursor()

        cardList = cdb.getCardDetails(cur, userId)
        print(cardList)
        cardDetailsUI(userId)

        # Commit and close database connection
        con.commit()
        con.close()

    elif (option == '2') :
        # Open connection to perform sql queries
        con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
        cur = con.cursor()

        cdb.addCard(cur, userId)

        # Commit and close database connection
        con.commit()
        con.close()

        cardDetailsUI(userId)

    elif (option == '3') :
        print('Need to implement Delete Card')
        cardDetailsUI(userId)

    elif (option == '4') :
        print('Redirecting to User Dashboard...')
        udui.userDashboardUI(userId)

    elif (option == '5') :
        print('Exiting from Card Details UI...')

    else :
        print('Invalid Input !')

    # Commit and close database connection
    con.commit()
    # con.close()