from calculateMichiganTax import calculateTax as taxCalculation
"""Calculates the Michigan Sales tax for a car sale
"""
michiganTax = .06
carPrice = 60000.78
totalTax = taxCalculation(carPrice)
print("The tax is: ${:.2f}".format(totalTax))

