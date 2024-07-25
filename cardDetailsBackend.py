# cardDetailsBackend.py

def askCardType() :
    # Asks for Card Type and returns the same
    cardType = input('Enter Card Type [DEBIT, CREDIT]: ')
    return cardType

def isValidCardType(cardType) :
    # returns True if Card Type is valid else False
    validCardTypeList = ['DEBIT', 'CREDIT']
    if (cardType in validCardTypeList) :
        return True
    else :
        print(f'Card Type should be in {validCardTypeList}')
        return False

def askCardNo() :
    # Asks for Card No and returns the same
    cardNo = input('Enter Card No.: ')
    return cardNo

def isValidCardNo(cardNo):
    # returns True if Card No is valid else False
    # Card No should be numeric and of 16 digits
    if (cardNo.isnumeric()):
        # Card No is numeric
        # Check if Card No is of 16 digits
        if (len(cardNo) == 16):
            return True
        else:
            print('Card No. should be of 16 digits !')
            return False
    else:
        print('Card No. should be numeric !')
        return False

def askValidFrom() :
    # Asks for Valid From date and returns the same
    validFrom = input('Valid From [Eg. 02/23]: ')
    return validFrom

def askValidTo() :
    # Asks for Valid To date and returns the same
    validTo = input('Valid to [Eg. 02/27]: ')
    return validTo

def isValidCardDate(validDate) :
    # returns True if validFrom is valid else False
    # Valid From [Eg. 02/23]
    validDateSplitList = validDate.split('/')
    month = validDateSplitList[0]
    year = validDateSplitList[1]

    validMonth = False
    if (month.isnumeric()) :
        # Month value is numeric
        month = int(month)
        # month should be 1 - 12
        if (month >= 0 and month <= 12) :
            # valid month
            validMonth = True
        else :
            validMonth = False
    else :
        # Month value is not numeric
        print(f'Month \'{month}\' should be numeric !')
        validMonth = False

    validYear = False
    if (year.isnumeric()):
        # Month value is numeric
        year = int(year)
        # month should be 1 - 12
        if (year >= 0 and year <= 99):
            # valid year
            validYear = True
        else:
            validYear = False
    else:
        # Month value is not numeric
        print(f'Year \'{year}\' should be numeric !')
        validYear = False

    # If both Month and Year are valid
    if (validMonth and validYear) :
        return True
    # If Any one of Month and Year is not valid
    else :
        return False

def askCvv() :
    # Asks user for CVV and returns the same
    cvv = input('Enter CVV Code [Eg. 333]: ')
    return cvv

def isValidCvv(cvv) :
    # returns True if CVV is valid else False
    # CVV should be numeric and of 3 digits
    if (cvv.isnumeric()) :
        # cvv is numeric
        # Check if CVV is of 3 digits
        if (len(cvv) == 3) :
            return True
        else :
            print('CVV should be of 3 digits !')
            return False
    else :
        print('CVV should be of numeric value !')
        return False

def addCard(cur, userId) :
    print('Please Enter Card Details :')

    # Keep asking Card Type until user inputs a valid input
    cardType = askCardType()
    while (isValidCardType(cardType) == False) :
        cardType = askCardType()

    # Keep asking Card No until user inputs a valid input
    cardNo = askCardNo()
    while (isValidCardNo(cardNo) == False) :
        cardNo = askCardNo()
    # Convert to int
    cardNo = int(cardNo)

    # Keep asking ValidFrom until user inputs a valid input
    validFrom = askValidFrom()
    while (isValidCardDate(validFrom) == False) :
        validFrom = askValidFrom()

    # Keep asking ValidTo until user inputs a valid input
    validTo = askValidTo()
    while (isValidCardDate(validTo) == False) :
        validTo = askValidTo()

    # Keep asking CVV until user inputs a valid input
    cvv = askCvv()
    while (isValidCvv(cvv) == False) :
        cvv = askCvv()
    # Convert to int (As cvv is already validated)
    cvv = int(cvv)

    # Insert Card Details into SQL table
    query = f'INSERT INTO Cards VALUES(\'{userId}\', \'{cardType}\', {cardNo}, \'{validFrom}\', \'{validTo}\', {cvv})'
    cur.execute(query)

    print('Card is added Successfully.')

def getCardDetails(cur, userId):
    # returns list of cards
    cardList = []
    query = f'SELECT * FROM Cards WHERE user_id = \'{userId}\''
    for row in cur.execute(query) :
        # print(row)
        cardList.append(row[2])
    return cardList
