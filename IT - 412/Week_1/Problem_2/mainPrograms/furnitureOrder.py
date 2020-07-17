import calculateMichiganTax as taxCalculation
"""This method calculates the sales tax by importing the calculateTax method
"""

michiganTax = .06
chairPrice = 1500
totalTax = taxCalculation.calculateTax(chairPrice)
print("The tax is: ${:.2f}".format(totalTax))