class Animal:
    def __init__(self, name):
        self.animal_name = name
    def eat(self):
        raise NotImplementedError('Child class should be implementing this')

class Monkey(Animal):
    def eat(self):
        print('monkey eating banana')

class Bird(Animal):
    def eat(self):
        print('bird eating seeds')

    def fly(self):
        print('bird soaring high ' + self.animal_name)

mymonkey = Monkey('JoeJoe')
mymonkey.eat()
mybird = Bird('tweety')
mybird.fly()
