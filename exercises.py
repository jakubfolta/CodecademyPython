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


#Lambda expressions
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = ''.join(list(filter(lambda x: x != 'X', garbled)))
print(message)


#Lesson 10: The base 2 number system
print(0b1, end=' ')    #1
print(0b10, end=' ')   #2
print(0b11, end=' ')   #3
print(0b100, end=' ')  #4
print(0b101, end=' ')  #5
print(0b110, end=' ')  #6
print(0b111, end=' ')  #7
print(0b1000, end=' ')
print(0b1001, end=' ')
print(0b1010, end=' ')
print(0b1011, end=' ')
print(0b1100, end=' ')
print(0b1101, end=' ')
print(0b1110, end=' ')
print(0b1111, end=' ')
print(0b10000, end=' ')
print(0b10001, end=' ')
print(0b10010, 0b10011, 0b10100, 0b10101, 0b10110, 0b10111)
print(0b11000, 0b11001, 0b11010, 0b11011, 0b11100, 0b11101)
print(0b1 + 0b11)
print(0b11 * 0b11)


#The bin(function)
print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))


#int()'s Second Parameter
print(int("1",2))
print(int("10",2))
print(int("111",2))
print(int("0b100",2))
print(int(bin(5),2))
print(int('11001001', 2))
