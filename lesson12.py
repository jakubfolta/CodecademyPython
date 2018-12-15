#File Input/Output
#The open() function
my_file = open('output.txt', 'w')

#Writing
my_list = [i ** 2 for i in range(1, 11)]

my_file = open('output.txt', 'w')

for x in my_list:
    my_file.write(str(x) + '\n')

my_file.close()

#Reading
my_file = open('output.txt', 'r')

print(my_file.read())

my_file.close()

#Reading between the lines
my_file = open('text.txt', 'w')

my_file.write('This is the first line' + '\n')
my_file.write('This is the second line' + '\n')
my_file.write('This is the third line' + '\n')

my_file.close()

my_file = open('text.txt', 'r')

print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

my_file.close()

#PSA: Buffering data










