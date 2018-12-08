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

print(my_cart('Qba'))















            
    
