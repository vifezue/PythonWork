from calculateMichiganTax import calculateTax
"""This method calls calculates the Michigan sales tax for a grocery order
"""

michiganTax = .06
groceryOrderTotal = 247.00
totalTax = calculateTax(groceryOrderTotal)
print("The tax is: ${:.2f}".format(totalTax))
