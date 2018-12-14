#File Input/Output
#The open() function
my_file = open('output.txt', 'w')

#Writing
my_list = [i ** 2 for i in range(1, 11)]

my_file = open('output.txt', 'w')

for x in my_list:
    my_file.write(str(x) + '\n')

my_file.close()
