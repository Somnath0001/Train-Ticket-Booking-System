# signupBackend.py

import csv

def askAge() :
    # Asks for Age and returns the same
    age = input('Enter Age: ')
    return age

def isValidAge(age) :
    # returns True if the age is valid else False
    if (age.isnumeric()) :
        # Age is numeric
        age = int(age)
        # Age should be between 0 to 125
        if (age > 0 and age <= 125) :
            return True
        else :
            print('Not a real age (age should be 1-125) !')
            return False
    else :
        print('Age should be a numeric value !')
        return False

def askMobileNo() :
    # Asks Mobile No. and returns the same
    mobileNo = input('Enter Mobile No.: ')
    return mobileNo

def isValidMobileNo(mobileNo) :
    # returns True if the mobile no. is valid else False
    if (mobileNo.isnumeric()) :
        # Mobile No. is numeric
        # Mobile No. should be of 10 digits
        if (len(mobileNo) == 10) :
            return True
        else :
            print('Mobile No. should be of 10 digits !')
            return False
    else :
        print('Mobile No. should be a numeric value !')
        return False

def askEmail() :
    # Asks Email Address and returns the same
    email = input('Enter Email: ')
    return email

def isValidEmail(email) :
    # returns True if Email Address is valid else False
    # Check if '@' is there in email address
    if ('@' in email) :
        username = email.split('@')[0]
        # Check if '.' is there in email address
        if ('.' in email.split('@')[1]) :
            domain = email.split('@')[1].split('.')[0]
            domainType = email.split('@')[1].split('.')[1]
            # print(f'[ DEBUG ] Username: {username} | Domain: {domain} | Domain Type: {domainType}')
            # Any of the parts of the mail should not be null
            if (username != '' and domain != '' and domainType != '') :
                # Valid email address
                return True
            # Any of hte email part is null
            else :
                print(f'Characters are missing !')
                return False
        # '.' is not there in email address
        else :
            print(f'Invalid Email: \'.\' is missing !')
            return False
    # '@' is not there in email address
    else :
        print(f'Invalid Email: \'@\' is missing !')
        return False

def signup(userId, password, fname, lname, address, age, email, mobile):
    # store all details in .csv format
    with open('users.csv','a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([userId, password, fname, lname, address, age, email, mobile])
    print('Signup Successful :)\n')
    print('Hi ',fname,', Redirecting you to login page...')

def askSignupInput() :
    userId = input('Enter User Id: ')
    password = input('Enter Password: ')
    fname = input('Enter First Name: ')
    lname = input('Enter Last Name: ')
    address = input('Enter Address: ')

    # Keep asking age until user inputs a valid input
    age = askAge()
    while (isValidAge(age) == False):
        age = askAge()
    # Convert to int (As the age is valid)
    age = int(age)

    # Keep asking email until user inputs a valid input
    email = askEmail()
    while (isValidEmail(email) == False) :
        email = askEmail()

    # Keep asking mobile no. until user inputs a valid input
    mobile = askMobileNo()
    while (isValidMobileNo(mobile) == False) :
        mobile = askMobileNo()
    # convert to int (As already verified)
    mobile = int(mobile)

    signupDetailsList = [userId, password, fname, lname, address, age, email, mobile]

    return signupDetailsList

# Test
# print(isValidEmail('somnath@mail.com'))