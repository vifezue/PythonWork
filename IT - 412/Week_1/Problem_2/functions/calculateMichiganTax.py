def calculateTax(priceAmount):
    """This method calculates the Michigan sales Tax
    
    Arguments:
        priceAmount {float} -- Passes in the amount for the item
    
    Returns:
        float -- The price of the tax
    """
    michiganTax = .06
    cost = float(priceAmount)
    totalTax = cost * michiganTax
    return totalTax

    
    
    