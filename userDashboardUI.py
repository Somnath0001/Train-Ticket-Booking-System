# userDashboardUI.py

import trainSearchUI as tsui
import login as l
import cardDetailsUI as cdui
import bookingStatusUI as bsui

def askOption(userId) :
    option = input('\n1. Search Trains\n2. Card Details UI\n3. Booking Status\n5. Logout\nPlease enter a number to choose option [Eg. 1]\n: ')

    if (option == '1'):
        print('Redirecting to Train Search Ui...')
        tsui.trainSearchUI(userId)
        askOption(userId)

    elif (option == '2'):
        print('Redirecting to Card Details Ui...')
        cdui.cardDetailsUI(userId)
        askOption(userId)

    elif (option == '3'):
        print('Redirecting to Booking Status Ui...')
        bsui.bookingStatusUI(userId)
        askOption(userId)

    elif (option == '5'):
        print('Redirecting to Login UI...')
        l.login()

    else:
        print('Invalid Input !')
        # Ask to choose option again
        askOption(userId)


def userDashboardUI(userId) :
    print('\n---  User Dashboard UI  ---\n')
    print(f'Welcome {userId} !')

    askOption(userId)
    # Activites to be performed
    # Check My Details
    # Setting
    # Exit
    # Search For Trains
    # My Booked Trains
    # Passenger Details
    # Card Details
    # Booking Status

