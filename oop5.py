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

print("hey \'ann\'s house\' ",2 ** 3 ** 2 ** 1)

print(type(len("Python")))

z, y, x = 2, 1, 0

# put line here
print(x, y, z)

print(0 ** 0)

for i in range(1, 4, 2):
    print("*")

# for i in range(1, 4, 2):
#     print("*1", end=".")

for i in range(1, 4, 2):
    print("*", end="**")
print("***")

x = "20"
y = "30"
print(x > y)

s = "Hello, Python!"
print(s[-14:15])

lst = ["A", "B", "C", 2, 4]
del lst[0:-2]
print(lst)

dict={'a':1,'b':2, 'c':3}
for item in dict:
    print(item)

s = 'python'
for i in range(len(s)):
    i = s[i].upper()
print(s, end="")

lst = [[c for c in range(r)] for r in range(3)]
for x in lst:
    for y in x:
        if y < 2:
            print('*')

lst = [2 ** x for x in range(0, 11)]
print(lst[-1])

print(2**3)

def list1():
    val = []
    for x in range(0,11):
        val.append(2**x)
    return val



lst1 = "12,34"
lst2 = lst1.split(',')
print(152,len(lst1) < len(lst2))

def fun(a, b=0, c=5, d=1):
    return a ** b ** c
print(fun(b=2, a=4, c=3))

x=5
f = lambda x: 1 + 2
print(f(x))

from math import pi as xyz    # line 01
print(xyz)

x=1
def a(x):
    return 2 * x
x = 2 + a(x)
print(a(x))
#line1 #line2 #line3 #line4 #line5

a = 'hello'
def x(a,b='a'):
    z = a[0]
    return z
print(x(a))
#line1 #line2 #line3 #line4 #line5

s = 'SPAM'
def f(x):
    return s + 'MAPS'
print(f(s))

lst = range(5)
print(len(lst))

def gen():
    lst = range(5)
    for i in lst:
        yield i*i
for i in gen():
    print(i, end="")

class A:
    def a(self):
        print("A", end='')
class B(A):
    def a(self):
        print("B", end='')
class C(B):
    def b(self):
        print("B", end='')
a = A()
b = B()
c = C()
a.a()
b.a()
c.b()
print('\nhi')

try:
    print("Hello")
    raise Exception
    print(1/0)
except Exception as e:
    print(e)

Val = 1
Val2 = 0
Val = Val ^ Val2
print(Val)
Val2 = Val ^ Val2
print(Val2)
Val = Val ^ Val2
print(Val)
print(1^1)

dict={'a':1,'b':2, 'c':3}
for item in dict:
    print(item)

lst = [[c for c in range(r)] for r in range(3)]
for x in lst:
    for y in x:
        if y < 2:
            print('*', end='')
print(lst)

from random import randint
for i in range(10):
    # print(random(1, 5))
    pass

print(randint(0,1))
