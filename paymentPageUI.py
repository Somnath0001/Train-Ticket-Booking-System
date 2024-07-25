# paymentPageUI.py

import sqlite3
import bookingStatusUI as bsui
import cardDetailsUI as cdui
import cardDetailsBackend as cdb
import admin_database_handler.payment_table_handler as payth
import admin_database_handler.booking_table_handler as bth
import admin_database_handler.passanger_table_handler as pth
import bank

def askCardSelection() :
    cardSelection = input('Choose Card [Eg. 1]: ')
    return cardSelection

def isValidCardSelection(cardSelection, cardList) :
    # returns Ture if cardSelection is valid else False
    # Card Selection should be numeric and with in 1 - len(cardList)
    if (cardSelection.isnumeric()) :
        # is numeric
        # Convert to int
        cardSelection = int(cardSelection)
        if (cardSelection > 0 and cardSelection <= len(cardList)) :
            return True
        else :
            print('Invalid Selection !')
            return False
    else :
        print('Card Selection should be a numeric value !')
        return False

def askpaymentMethodOption() :
    # Asks user option for payment method and returns the same
    paymentMethodOption = input(f'Choose Payment Method [1. Card, 2. Cash, 3. Wallet]: ')
    return paymentMethodOption

def isValidPaymentMethodOption(paymentMethodOption):
    # returns True if Payment Method Option is valid else False
    validPaymentMethodOptionList = ['1', '2', '3']
    if (paymentMethodOption in validPaymentMethodOptionList):
        return True
    else:
        print(f'Please choose valid option from {validPaymentMethodOptionList}')
        return False

def askCardOption() :
    # Asks user Card Option and returns the same
    cardOption = input(f'1. Choose CARD\n2. Add CARD\n3. Exit\nPlease enter a number to choose option [Eg. 1]\n: ')
    return cardOption

def isValidCardOption(cardOption) :
    # returns True if Card Option is valid else False
    validCardOptionList = ['1', '2', '3']
    if (cardOption in validCardOptionList) :
        return True
    else :
        print(f'Valid Options: {validCardOptionList}')
        return False

def askBookingStatusOption() :
    # Asks user options and returns the same
    option = input('1.Booking Status\n2.Retry\n3. Exit\nPlease enter a number to choose option [Eg. 1]\n: ')
    return option

def isValidBookingStatusOption(option) :
    # returns True if option is valid else False
    validBookingStatusOptionList = ['1', '2', '3']
    if (option in validBookingStatusOptionList) :
        return True
    else :
        print(f'Valid Options: {validBookingStatusOptionList}')
        return False

def askPayOption() :
    # Asks user pay option and returns the same
    payOption = input('\n1. Pay [Redirect to Bank Page]\n2. Exit\nPlease enter a number to choose option [Eg. 1]\n: ')
    return payOption

def isValidPayOption(payOption) :
    # returns True if payOption is valid else False
    validPayOptionList = ['1', '2', '3']
    if (payOption in validPayOptionList) :
        return True
    else :
        print(f'Please choose from {validPayOptionList}')
        return False

def chooseCardDetails(userId) :
    # Shows available Cards. It lets user select one Card and returns the CardNo

    print(f'Please select Card:')
    # print('print card details with index no')

    # Open connection to perform sql queries
    con = sqlite3.connect(
        'C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur = con.cursor()

    # Store list of available Cards of the user
    cardList = cdb.getCardDetails(cur, userId)
    print(cardList)

    # Commit and close the database
    con.commit()
    con.close()

    # Initialize cardSelected variable
    cardSelected = False

    # Cards are available for the user
    if (cardList) :
        # not empty
        # Display all the available cards with index no. to choose
        i = 1
        for card in cardList :
            print('\t', i, '- Card No.: ', card)
            i += 1

        # Keep asking Card Selection until user inputs a valid input
        cardSelection = askCardSelection()
        while (isValidCardSelection(cardSelection, cardList) == False) :
            cardSelection = askCardSelection()
        # Convert to int
        cardSelection = int(cardSelection)

        # print(f'[ DEBUG ] cardSelection: {cardSelection}')

        # Card Selected
        cardSelected = cardList[cardSelection-1]

    # No available Cards for the user
    else :
        # card list is empty
        # redirect to Card Details UI to add card
        print('Redirecting to Card Details UI...')
        cdui.cardDetailsUI(userId)
        # Let user choose card details
        chooseCardDetails(userId)

    return cardSelected
    # ask for index no

def paymentProcess(userId, amount, paymentMethod, cardNo, bookIdList) :
    # Open connection to perform sql queries
    con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
    cur1 = con.cursor()

    # Add/update 'Payment' status = 'PEND'
    paymentId = payth.addPayment(cur1, userId, amount, paymentMethod, cardNo)

    print(f'[ DEBUG ] View All Payments: ')
    payth.viewAllPayment(cur1)  # need to comment later

    # Keep asking user choice until user inputs a valid input and perform accordingly
    payOption = askPayOption()
    while (isValidPayOption(payOption) == False) :
        payOption = askPayOption()

    if (payOption == '1'):
        # send payment details to bank
        # payToBankAPI(paymentId, amount) : it should return True if payment confirmed else False
        pass
    elif (payOption == '2'):
        # exit
        pass
    else:
        print('Invalid Input !')

    print('Payment Processing...')

    # while loop for 30 sec
    # in every 1 sec call paymentConfirmationAPI(paymentId, amount)
    # if it returns true get out of the loop

    # Call payment to bank API for transaction
    isPaymentSuccessful = bank.paymentToBankAPI(userId, amount, paymentMethod, cardNo)

    if (isPaymentSuccessful) :
        print('\nPayment Successful :)\n')

        # update 'Payment' status = 'COMP' and add PNR No
        pnrNo = payth.updatePaymentStatusToCOMP(cur1, paymentId)

        print(f'[ DEBUG ] View All Payments: ')
        payth.viewAllPayment(cur1)  # need to comment later

        # Test
        # print('Get all Passanger Details Before Update')
        # pth.getAllPassagnerDetails(cur1)

        # add/update PNR No to 'Passangers' table for the passagner_id/ book_id
        for bookId in bookIdList:
            pth.updateStatusAndAddPnrNoByBookId(cur1, bookId, pnrNo)
            print(f'Added PNR No in Passangers Table for passanger_id = {bookId}')

        # Test
        # print('Get all Passanger Details after Update')
        # pth.getAllPassagnerDetails(cur1)

        # Test
        # print('Get All Booking Details Before Update')
        # bth.getAllBookingDetails(cur1)

        # update 'Booking' status to 'COMP' for the passagner_id/ book_id
        for bookId in bookIdList:
            bth.updateBookingStatusByBookId(cur1, bookId)
            print(f'Status updated to COMP for book_id = {bookId}')

        # Test
        # print('Get All Booking Details after Update')
        # bth.getAllBookingDetails(cur1)

        # Commit and close database connection
        con.commit()
        con.close()
    else :
        print('\nPayment Unsuccessful !\n')

        # Insert failed payment details in Failed_Transaction table (userId, amount, bookIdList)
        # We will be able to recover the details and retry payment again

    # Ask options to user to perform accordingly
    # Keep asking user for Option until user inputs a valid input
    option = askBookingStatusOption()
    while (isValidBookingStatusOption(option) == False) :
        option = askBookingStatusOption()

    if (option == '1'):
        # Redirect to booking status UI
        print('Redirecting to Booking Status UI')
        bsui.bookingStatusUI(userId)
    elif (option == '2'):
        # Retry the payment if payment is not successful : Call Payment Page UI again
        paymentPageUI(userId, amount)
    elif (option == '3'):
        # exit
        print('Exiting...')
    else :
        print('Invalid Input !')

def paymentPageUI(userId, amount, bookIdList) :
    print('\n---  Payment Page UI  ---\n')
    print(f'User Id: {userId}')
    print(f'Amount to Pay: {amount}')

    # Keep asking Payment Method Option until user inputs a valid input
    paymentMethod = askpaymentMethodOption()
    while (isValidPaymentMethodOption(paymentMethod) == False) :
        paymentMethod = askpaymentMethodOption()

    # Payment with Card
    if (paymentMethod == '1') :
        # Fetch Card Details

        # Keep asking Card Option until user inputs a valid input
        cardOption = askCardOption()
        while (isValidCardOption(cardOption) == False) :
            cardOption = askCardOption()

        if (cardOption == '1') :
            # Choose available cards
            selectedCardNo = chooseCardDetails(userId)
            print(f'Selected Card No.: {selectedCardNo}')

            # Open connection to perform sql queries
            con = sqlite3.connect(
                'C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
            cur = con.cursor()

            # Process payment
            paymentProcess(userId, amount, paymentMethod, selectedCardNo, bookIdList)

            # Commit and close database connection
            con.commit()
            con.close()

        elif (cardOption == '2') :
            # Open connection to perform sql queries
            con = sqlite3.connect('C:\\Users\\somna\\PycharmProjects\\Train_Ticket_Booking_System\\admin_database_handler\\ticket_booking.db')
            cur = con.cursor()

            # Add Card : call payment backend method
            cdb.addCard(cur, userId)

            # Choose available cards
            selectedCardNo = chooseCardDetails(userId)
            print(f'Selected Card No.: {selectedCardNo}')

            # Process payment
            paymentProcess(userId, amount, paymentMethod, selectedCardNo, bookIdList)

            # Commit and close connection
            con.commit()
            con.close()

        elif (cardOption == '3') :
            # exit
            print('Exiting...')

        else :
            print('Please Enter Valid Input !')

    # Payment with Cash
    elif (paymentMethod == '2') :
        print(f'You have selected \'Cash\' as Payment Method.')

    # Payment with Wallet
    elif (paymentMethod == '3') :
        print(f'You have selected \'Wallet\' as Payment Method')

    # Invalid input
    else :
        print('Invalid Input !')

# paymentPageUI('som1', 3000)

