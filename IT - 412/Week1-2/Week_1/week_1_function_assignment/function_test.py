from functions.my_functions import divideTwoNumber
from functions.my_functions import multiplyTwoNumber

division_list = [{"top_number": 1, "bottom_number": 2}, {"top_number": 5, "bottom_number": 8}]
the_result = divideTwoNumber(division_list)
print("The result of division is:" + str(the_result))
print(str(the_result))

multiply_list = [{"top_number": 1, "bottom_number": 2}, {"top_number": 5, "bottom_number": 8}]
the_result = multiplyTwoNumber(multiply_list)
print("The result of multiplication is:" + str(the_result))
print(str(the_result))

