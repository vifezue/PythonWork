from Clothing import Clothing

class Shirt(Clothing):
    """Creates A Shirt with inheritance from the Clothing Class
    
    Arguments:
        Clothing {string, string, string, string, string} 
    """
    def __init__ (self, size, color, quantity,     shirttype, message):
        super().__init__(size, color, quantity)
        self.shirttype = shirttype
        self.message = message

    def get_Message(self):
        """Displays the message of the shirt
        """
        print("Shirt Message: " + self.message)