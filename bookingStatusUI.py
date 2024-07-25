# bookingStatusUI.py

import sqlite3
import pandas as pd
from tabulate import tabulate
import userDashboardUI as udui
import printTicketBackend as ptb
import admin_database_handler.passanger_table_handler as pth


# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 21)
# pd.set_option('display.width', 1000)

def askPnrNoOption():
    # Asks PNR No option and returns the same
    pnrNoOption = input('Enter Index No to choose PNR Number [Eg. 1]: ')
    return pnrNoOption


def isValidPnrNoOption(pnrNoOption, pnrNoList):
    # returns True if PNR No Option is valid else False
    # PNR No Option should be numeric and 1 - len(pnrNoList)
    # Check if numeric
    if (pnrNoOption.isnumeric()):
        # Numeric
        # Convert to int
        pnrNoOption = int(pnrNoOption)
        # Check the limit
        if (pnrNoOption > 0 and pnrNoOption <= len(pnrNoList)):
            return True
        else:
            print('Invalid Digit !')
            return False
    else:
        print('Option should be a digit !')
        return False


def bookingStatusUI(userId):
    print('\n---  Booking Status UI  ---\n')
    print('Please find the below Booking Details booked by you.\n')

    # Open connection to perform sql queries
    con = sqlite3.connect(
        'C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    # SQL query to be executed
    query = f'SELECT * FROM Passangers p JOIN Booking b ON p.passanger_id = b.book_id WHERE p.booked_by = \'{userId}\''

    # Settings for pandas to get formatted result
    pd.set_option('display.max_columns', 30)
    pd.set_option('display.max_rows', 50)
    pd.set_option('display.width', 1000)

    # Get result of the sql query in a formatted manner
    formattedOutput = pd.read_sql_query(query, con)
    # print(formattedOutput)

    # Display Booking details
    print(tabulate(formattedOutput, headers='keys', tablefmt='fancy_grid'))

    # Commit and close the database connection
    con.commit()
    con.close()

    # Ask for option and perform accordingly
    option = input('\n1. Print Ticket\n2. Exit to Dashboard\nPlease enter a number to choose option [Eg. 1]\n: ')
    if (option == '1'):
        # print ticket

        # Open connection to perform sql queries
        con = sqlite3.connect(
            'C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
        cur = con.cursor()

        # get list of PNR No for the user
        pnrNoList = pth.getAllPnrNoForUser(cur, userId)

        # Show list of PNR No for the user
        print('Available PNR Numbers for You :')
        print(f'# - PNR Number')
        i = 1
        for pnrNo in pnrNoList:
            print(f'{i} - {pnrNo}')
            i += 1

        # Choose PNR No to print ticket
        pnrNoOption = askPnrNoOption()
        while (isValidPnrNoOption(pnrNoOption, pnrNoList) == False):
            pnrNoOption = askPnrNoOption()
        # Convert to int (As already verified)
        pnrNoOption = int(pnrNoOption)

        # Selected PNR No to print ticket
        pnrNoSelected = pnrNoList[pnrNoOption - 1]
        # print(f'[ DEBUG ] PNR Number Chosen: {pnrNoSelected}')

        # Commit and close the database connection
        con.commit()
        con.close()

        # Print ticket
        print(f'Printing Ticket for PNR Number - {pnrNoSelected}...')
        ptb.printTicket(pnrNo)

    elif (option == '2'):
        # Exit
        print('Redirecting to Dashboard...')
        udui.userDashboardUI(userId)
    else:
        print('! Invalid Input')
        # Redirect to Booking Status UI again
        bookingStatusUI(userId)

# con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
# cur = con.cursor()
# query1 = '''SELECT * FROM Passangers'''
# print('\nDetails for Passangers Table :\n')
# for row in cur.execute(query1) :
#     print(row)
#
# query2 = '''SELECT * FROM Booking'''
# print('\nDetails for Booking Table :\n')
# for row in cur.execute(query2) :
#     print(row)

# Test Starter
# bookingStatusUI('soum3')

#  JOIN Payment pt ON p.booked_by=pt.user_id

