
class Pet():
    """A simple classs for representing a pet"""

    def __init__(self, name, age):
        """ Initialize name and age variable/attributes"""
        self.name = name
        self.age = age

    def clean(self):
        """The act of cleaning a pet"""
        print(self.name + "is clean!")