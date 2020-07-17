from classes.Pet import Pet
from classes.Cat import Cat
from classes.Dog import Dog

my_cat = Cat("Fluffy", 3)      
print("My dog's name is: "+my_cat.name)

my_dog = Dog("Scout",3,"German Shepard")
print("My dog's name is: "+my_dog.name)
my_dog.clean() 
print("My Dog's breed is: "+ my_dog.breed)