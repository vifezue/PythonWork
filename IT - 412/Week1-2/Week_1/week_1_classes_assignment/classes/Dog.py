from classes.Pet import Pet
class Dog(Pet):
    """Creates a Dog object 
    
    Arguments:
        Pet [object] -- Passes in Dog object
    """

    def __init__(self, name, age, breed):
        super().__init__(name,age)
        self.breed = breed

    def placeDogInCarrier(self):
        """Places Dog in Carrier
        """
        print(self.name + " is in the car carrier!")

    def takeToVet(self):
        """Takes the Dog object and sends to Vet
        """
        self.placeDogInCarrier()
        self.____visitVet()

    def __visitVet(self):
        """Represents the act of taking the dog to the vet
        """
        print(self.name + "is on thier way to the vet!")
