class InventoryItem():
    
    def __init__(self,productID,productName,currentQuantity):
        """Constructor for the Inventory Item"""
        self.productID = productID
        self.productName = productName
        self.currentQuantity = currentQuantity
        
    def buyItem(self, quantity = 1):
        """removes the inventory item by number"""
        val = self.currentQuantity - quantity
        self.currentQuantity = val

