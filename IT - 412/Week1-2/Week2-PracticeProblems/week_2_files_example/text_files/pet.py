# Virtual Representation of a Pet - can be inherited by other child classes. e.g. Dog, Cat, etc.

class Pet():
    """A simple class for representing a pet"""

    def __init__(self, name, age):
        """Initialize name and age variables/attributes"""
        self.name = name
        self.age = age

    def clean(self):
        """ Reprsents the act of cleaning the pet"""
        print(self.name + " is clean!")
        
#End of class declaration