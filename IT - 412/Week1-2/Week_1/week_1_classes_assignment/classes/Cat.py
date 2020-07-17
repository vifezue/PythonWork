from classes.Pet import Pet
class Cat(Pet):
    """Cat Object with inhertance from Pet
    
    Arguments:
        Pet [object] -- Passes in the Pet object and attributes to create Cat
    """
    def __init__(self, name, age):

        super().__init__(name,age)
