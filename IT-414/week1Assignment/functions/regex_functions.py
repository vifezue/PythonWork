import re


def findAllAmounts(passed_string):
    """Finds all valid amounts

    Arguments:
        passed_string {string} -- [passed in credit card strings]

    Returns:
        [list] -- [list of passed in credit card values found]
    """
    amountRegex = re.compile(r'\$\s?\d,\d{3}')
    amountList = amountRegex.findall(passed_string)
    return amountList


def isValidAmount(passed_amount):
    """Validates Amount

    Arguments:
        passed_amount {string} -- passed in amount string

    Returns:
        [boolean] -- [true or false based on the input]
    """
    amountRegex = re.compile(r'\$\s?\d,\d{3}')
    amountTest = amountRegex.search(passed_amount)
    if amountTest is None:
        print("You did not enter a proper amount")
        return False
    else:
        if passed_amount == amountTest.group():
            print("You did enter a proper amount")
            return True
        else:
            print("You did not enter a proper amount")
            return False


def findAllCoordinates(passed_coordinates):
    coordinatesRegex = re.compile(r'\-?\d?\d?\.?\d+?,\s?\-?\d+\.?\d{4}\d?')
    coordinatesList = coordinatesRegex.findall(passed_coordinates)
    return coordinatesList


def isValidCoordinates(passed_coordinates):
    """Validates the coordinates

    Arguments:
        passed_coordinates {string} -- passed in coordinates string

    Returns:
        [boolean] -- [true or false based on the input]
    """
    coordinatesRegex = re.compile(r'\-?\d?\d?\.?\d+?,\s?\-?\d+\.?\d{4}\d?')
    coordinatesTest = coordinatesRegex.search(passed_coordinates)
    if coordinatesTest is None:
        print("You did not enter a proper amount")
        return False
    else:
        if passed_coordinates == coordinatesTest.group():
            print("You did enter a proper coordinates")
            return True
        else:
            print("You did not enter a proper coordinates")
            return False


def findAllCreditCards(passed_cards):
    """Finds all credit cards and puts them into the list

    Arguments:
        passed_cards {string} -- string of passed in cards

    Returns:
        [list] -- [list of passed in cards]
    """
    creditCardsRegex = re.compile(
        r'4\d?\d?\s?\d\s?\d\s?\d\s?\d\s?\d\s?\d\s?\d\s?\d\s?\d\s?\d\s?\s?\d\d\d?')
    creditCardsList = creditCardsRegex.findall(passed_cards)
    return creditCardsList


def isValidCreditCard(passed_cards):
    """Validates the creditcard

    Arguments:
        passed_cards {string} -- passed in credit card string

    Returns:
        [boolean] -- [true or false based on the input]
    """
    creditCardsRegex = re.compile(
        r'4\d?\d?\s?\d\s?\d\s?\d\s?\d\s?\d\s?\d\s?\d\s?\d\s?\d\s?\d\s?\s?\d\d\d?$')
    creditCardTest = creditCardsRegex.search(passed_cards)
    if creditCardTest is None:
        print("You did not enter a proper amount")
        return False
    else:
        if passed_cards == creditCardTest.group():
            print("You did enter a proper coordinates")
            return True
        else:
            print("You did not enter a proper coordinates")
            return False
