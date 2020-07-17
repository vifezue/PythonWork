from functions.regex_functions import *
import pyperclip

date_string = str(pyperclip.paste())

my_dates = findAllDates(date_string)

print(my_dates)
