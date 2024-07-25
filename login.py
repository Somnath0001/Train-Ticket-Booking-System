# login.py

import loginBackend as lb
import signupBackend as sb
import userDashboardUI as udui
import admin_database_handler.users_table_handler as uth

# user will come and sign up

# Login page
# give user 2 choisces (login / signup)

def askLoginDetails() :
    userId = input('Enter User Id: ')
    password = input('Enter Password: ')
    loginDetails = [userId, password]
    return loginDetails

def login():
    print('\n---  Login UI  ---\n')
    loginPageInput = input('1. Login \n2. Signup\n3. Exit\nPlease enter a number to choose option [Eg. 1]\n: ')
    # print('loginPageInput = ', loginPageInput)

    if (loginPageInput == '1'):
        # Login
        # print('call login method')
        # log in should ask for 2 inputs, verifies and lets user log in

        # Ask login details
        loginDetails = askLoginDetails()

        userId = loginDetails[0]
        password = loginDetails[1]

        # Verify Credentials
        userLoginStatus = lb.verifyCredential(userId, password)
        # print('isVerified: ', type(isVerified))

        if (userLoginStatus == 'verifiedUser') :
            print('Login Successful :)\n')
            # Login Successful so goto Train Search Ui
            udui.userDashboardUI(userId)

        elif (userLoginStatus == 'incorrectPassword') :
            print('Incorrect Password !\nLogin Failed !\n')
            # Redirect to login
            login()

        elif (userLoginStatus == 'invalidUser') :
            print('Invalid User Id !\nLogin Failed !\n')
            # Redirect to login
            login()

        else :
            print('Condition not handled. Debug it.')

    elif (loginPageInput == '2'):
        # Sign Up
        # verifyUserid method should be there

        # ask for all details
        signupDetailsList = sb.askSignupInput()

        # Prepare details of users to sign up
        # userId = signupDetailsList[0]
        # password = signupDetailsList[1]
        # fname = signupDetailsList[2]
        # lname = signupDetailsList[3]
        # address = signupDetailsList[4]
        # age = signupDetailsList[5]
        # email = signupDetailsList[6]
        # mobile = signupDetailsList[7]

        # call signup method get details save or get user signed up
        # sb.signup(userId, password, fname, lname, address, age, email, mobile)
        uth.signup(*signupDetailsList)

        # Goto Login Page
        login()

    elif(loginPageInput == '3'):
        print('You have successfully exited from the application.')

    else:
        print('Invalid Input !')
        login()
