#Stride length
to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]

print(backwards_by_tens)


#Practice makes perfect
to_21 = range(1, 22)
odds = to_21[::2]
middle_third = to_21[7:14]


#Anonymous functions
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)


#Lambda syntax
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == 'Python' , languages)

