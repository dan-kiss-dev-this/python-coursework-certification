from machines.vehicle_stuff import Vehicle, Truck, Motorcycle
from utils.utility_stuff import DictionaryShortner, ListAndCharShortner
#methods are invoked on objects
#functions are invoked stand alone
#object oriented programming is about allowing better organization
#method is a object oriented concept

car1 = Vehicle('sedan', 'tesla')
print(car1.vehicle_body)
car2 = Vehicle('suv', 'tesla')
print(car2.get_vehicle_count())

truck1 = Truck('big rig', 'dodge')
car1 = Vehicle('sedan', 'ford')
motorcycle1 = Motorcycle('rider', 'ducatti')
print(truck1.get_vehicle_count())
# remember __init__ is constructor for python
# below is example of polymorphism aka different behavior, don't get too fancy to avoid errors
# comments are key in python as it is such a flexible language
truck1.drive()
car1.drive()
motorcycle1.drive()

myshortner = ListAndCharShortner([1,2,3,4,5])
myshortner.print_shortened_items()

myshortner = DictionaryShortner({1: 'mike', 2: 'tom', 3: 'rebeca', 4: 'mike', 5: 'paul'})
myshortner.print_shortened_items()

# double under - dunder methods

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + " age is " + str(self.age)

    def __len__(self):
        return 45


tom = Employee('Tom Lanister', 47)

# as we made a __str__ method it will the the representation of the object we made instead of a memory location
print(tom)
print(len(tom))

# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.
After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.
"""

class Animal:
    def __init__(self, name, age):
        print('animal created')
        self.name = name
        self.age = age

    def eat(self):
        print('the animal is eating')

    def move(self):
        print('the animal is moving')

class Dog(Animal):
    def move(self):
        print('the dog runs')

class Fish(Animal):
    def move(self):
        print('the fish swims')

mydog = Dog('Lassie', 2)
mydog.move()
print(mydog.name)

myfish = Fish('Goopy', 1)
myfish.eat()


