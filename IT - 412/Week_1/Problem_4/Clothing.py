class Clothing:
    def __init__ (self, size, color, quantity = 1):
        self.size = size
        self.color = color
        self.quantity = quantity

    def addQuantity(self,value):
        self.quantity = self.quantity + value

    def subtractQuantity(self,value):
        self.quantity = self.quantity - value