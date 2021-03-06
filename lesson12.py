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
write_file = open('text.txt','w')

read_file = open('text.txt','r')

write_file.write('Not closing files is VERY BAD.' + '\n')
write_file.close()

print(read_file.read())
read_file.close()

#The 'with' and 'as' Keywords
with open('text.txt', 'w') as textfile:
    textfile.write('Success!' + '\n')

textfile = open('text.txt', 'r')
print(textfile.read())

#Try it yourself
with open('text2.txt', 'w') as my_file:
    my_file.write('This is my text!' + '\n')

my_file = open('text2.txt', 'r')
print(my_file.read())

#Case closed?
with open('text2.txt', 'w') as my_file:
    my_file.write('This is my text!' + '\n')

my_file = open('text2.txt', 'r')
print(my_file.read())

if not my_file.closed:
    my_file.close()

print(my_file.closed)

