#Class basics
class Car(object):
    pass

#Create an instance of a class
class Car(object):
    pass

my_car = Car()

#Class member variables
class Car(object):
    condition = 'new'

my_car = Car()

#Calling class member variables
class Car(object):
    condition = 'new'

my_car = Car()
    
print(my_car.condition)

#Initializing a class
class Car(object):
    condition = 'new'
    
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

my_car = Car('DeLorean', 'silver', 88)

print(my_car.condition)

#Reffering to member variables
class Car(object):
    condition = 'new'

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

my_car = Car('DeLorean', 'silver', 88)

print(my_car.model)
print(my_car.color)
print(my_car.mpg)

#Creating class methods
class Car(object):
    condition = 'new'

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print('This is a {} {} with {} MPG.'.format(self.color, self.model, self.mpg))

my_car = Car('DeLorean', 'silver', 88)

my_car.display_car()











