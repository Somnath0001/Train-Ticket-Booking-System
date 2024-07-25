# passangerDetailsBackend.py

def isValidName(name) :
    # returns True if the name is valid else False
    # Split name: fetch firstname, middlename, lastname based on delimiter white space
    nameSplitList = name.split(" ")

    # it will help to track whether each nameSplit is valid: For final return as Ture, isTrue should be True for all the splits.
    isTrueForAllNameSplit = False
    for nameSplit in nameSplitList :
        # print(f'[ DEBUG ] nameSplit: {nameSplit}')
        if (nameSplit.isalpha()) :
            # The loop will continue and for final validity, each loop should be True
            isTrueForAllNameSplit = True
        else :
            # If one loop is False then the name is not valid: so return False
            print(f'\tName {nameSplit} should consists of alphabets only!')
            return False
    return isTrueForAllNameSplit

def isValidAge(age) :
    # returns True if the age is valid else False
    if (age.isnumeric()) :
        # Age is numeric
        age = int(age)
        # Age should be between 0 to 125
        if (age > 0 and age <= 125) :
            return True
        else :
            print('\tNot a real age (age should be 1-125) !')
            return False
    else :
        print('\tAge should be a numeric value !')
        return False

def isValidGender(gender) :
    # returns True if the gender is valid else False
    validGenderList = ['M', 'F', 'O']
    if (gender in validGenderList) :
        return True
    else :
        print(f'\tGender should be in {validGenderList} !')
        return False

def isValidIdCardType(idCardType) :
    validIdCardTypeList = ['Aadhar', 'Voter']
    if (idCardType in validIdCardTypeList) :
        return True
    else :
        print(f'\tId Card Type should be in {validIdCardTypeList} !')
        return False

def isValidIdCardNo(idCardNo, idCardType) :
    # For Aadahr card
    if (idCardType == 'Aadhar') :
        # id card no should be of 12 digits and numberic
        if (idCardNo.isnumeric()) :
            # Check if 12 digits
            if (len(idCardNo) == 12) :
                return True
            else :
                print('\tAadhar card should be of 12 digits !')
                return False
        else :
            print('\tAadhar card should consist of digits only !')
            return False
    # For Voter card
    else :
        # First 3 digits should be numeric and last 5 should be alphabet
        firstThreeCharsOfIdCardNo = idCardNo[0:3]
        lastFiveCharsOfIdCardNo = idCardNo[3:7]
        print(f'First 3 : {firstThreeCharsOfIdCardNo} | Last 5 : {lastFiveCharsOfIdCardNo}')
        if (firstThreeCharsOfIdCardNo.isalpha() and lastFiveCharsOfIdCardNo.isnumeric()) :
            return True
        else :
            print('\tVoter card no. should be like \'ABC12345\' !')
            return False



