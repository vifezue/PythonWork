import pyperclip
from functions.regex_functions import *

dataSet = str(pyperclip.paste())
amounts = findAllAmounts(dataSet)
creditCards = findAllCreditCards(dataSet)
coordinates = findAllCoordinates(dataSet)

zip(amounts, coordinates, creditCards)

output_string = ""
for (amount, location, card) in zip(amounts, coordinates, creditCards):
    output_string = output_string + location + " | " + amount + " | " + card + "\n"

pyperclip.copy(output_string)

