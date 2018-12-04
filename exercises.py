#Stride length
to_one_hundred = list(range(101))
backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens)


#Practice makes perfect
to_21 = range(1, 22)
odds = to_21[::2]
middle_third = to_21[7:14]


#Anonymous functions
my_list = range(16)
print(list(filter(lambda x: x % 3 == 0, my_list)))


#Lambda syntax
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(list(filter(lambda x: x == 'Python' , languages)))


#Try it!
squares = [x ** 2 for x in range(1, 11)]
print(list(filter(lambda x: 29 < x < 71 , squares)))


#Comprehending comprehensions
threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
print(threes_and_fives)


#List Slicing
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
garbledReverse = garbled[::-1]
message = garbledReverse[::2]
print(message)
