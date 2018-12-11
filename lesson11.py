#Class syntax
class Animal():
    pass

#Classier Classes
class Animal():
    def __init__(self):
        pass

#Let's not get too selfish
class Animal():
    def __init__(self, name):
        self.name = name

#Instantiating Your First Object
class Animal():
    def __init__(self, name):
        self.name = name

zebra = Animal('Jeffrey')
print(zebra.name)

#More on __init__() and self
class Animal(object):
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry
        
zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print(zebra.name, zebra.age, zebra.is_hungry)
print(giraffe.name, giraffe.age, giraffe.is_hungry)
print(panda.name, panda.age, panda.is_hungry)

#Class Scope
class Animal(object):
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal('Jeffrey', 2)
giraffe = Animal('Bruce', 1)
panda = Animal('Po', 7 )

print(zebra.name, zebra.age, zebra.is_alive)
print(giraffe.name, giraffe.age, giraffe.is_alive)
print(panda.name, panda.age, panda.is_alive)

#A methodical approach
class Animal(object):
    is_alive= True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print(self.name)
        print(self.age)

hippo = Animal('Max', 3)

hippo.description()

#They're multiplying
class Animal(object):
    is_alive = True
    health = 'good'
    def __init__(self, name, age):
        self.name = name
        self.age =age
    def description(self):
        print(self.name)
        print(self.age)

hippo = Animal('Max', 5)
sloth = Animal('John', 6)
ocelot = Animal('Ray', 5)

hippo.description()
print(hippo.health)
print(sloth.health)
print(ocelot.health)

#It's not all animals and fruits
class ShoppingCart(object):
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items_in_cart = {}

    def add_items(self, product, price):
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + ' added')
        else:
            print(product + 'is already in the cart')

    def remove_items(self, product):
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + ' removed.')
        else:
            print(product + 'is not in the cart.')

my_cart = ShoppingCart('Qba')
my_cart.add_items('Book', 7)

#Warning: Here be dragons
class  Customer(object):
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print('I\'m a string that stands in for the contents of your shopping cart.')

class ReturningCustomer(Customer):
    def display_order_history(self):
        print('I\'m a string thatstands in for your order history.')

monthy_python = ReturningCustomer('ID: 12345')
monthy_python.display_cart()
monthy_python.display_order_history()

#Inheritance syntax
class Shape(object):
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_siides

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

#Override!
class Employee(object):
    def __init__(self, employee_name):
        self.employee_name = employee_name
        
    def greet(self, other):
        print('Hello %s, welcome!' % other.employee_name)

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

lothar = PartTimeEmployee('Lothar')
print(lothar.calculate_wage(130))
lothar.greet(lothar)

#This looks like a job for...
class Employee(object):
    def __init__(self, employee_name):
        self.employee_name = employee_name
        
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours) 
        

milton = PartTimeEmployee('John')
print(milton.full_time_wage(10))

#Class basics




















        





























            
    
