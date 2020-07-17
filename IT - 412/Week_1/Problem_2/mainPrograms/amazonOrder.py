from calculateMichiganTax import *
"""Calculates Tax for the Amazon Order
"""

onlineOrderTotal = 13.00
totalTax = calculateTax(onlineOrderTotal)
print("The tax is: ${:.2f}".format(totalTax))