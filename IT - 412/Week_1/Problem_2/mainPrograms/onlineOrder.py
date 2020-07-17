import calculateMichiganTax
"""Calcualates the Michigan Tax for the online order
"""

onlineOrderTotal = 147.00
totalTax = calculateMichiganTax.calculateTax(onlineOrderTotal)
print("The tax is: ${:.2f}".format(totalTax))