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

#Modifying member variables
class Car(object):
    condition = 'new'

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print('This is a {} {} with {} MPG.'.format(self.color, self.model, self.mpg))

    def drive_car(self):
        self.condition = 'used'
        
    
my_car = Car('DeLorean', 'silver', 88)

print(my_car.condition)

my_car.drive_car()

print(my_car.condition)

#Inheritance
class Car(object):
    condition = 'new'

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print('This is a {} {} with {} MPG.'.format(self.color, self.model, self.mpg))

    def drive_car(self):
        self.condition = 'used'
        
    
my_car = Car('DeLorean', 'silver', 88)

print(my_car.condition)

my_car.drive_car()

print(my_car.condition)

class ElectricCar(Car):
    
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type

my_car = ElectricCar('Ford', 'black', 100, 'molten salt')

my_car.display_car()

#Overriding methods
class Car(object):
    condition = 'new'

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print('This is a {} {} with {} MPG.'.format(self.color, self.model, self.mpg))

    def drive_car(self):
        self.condition = 'used'
        
    
my_car = Car('DeLorean', 'silver', 88)

print(my_car.condition)

my_car.drive_car()

print(my_car.condition)

class ElectricCar(Car):
    
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = 'like new'

my_car = ElectricCar('Ford', 'black', 100, 'molten salt')

my_car.display_car()

print(my_car.condition)
my_car.drive_car()
print(my_car.condition)

#Building useful classes
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)

print(my_point)


