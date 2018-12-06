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
print(int("1", 2))
print(int("10", 2))
print(int("111", 2))
print(int("0b100", 2))
print(int(bin(5), 2))
print(int('11001001', 2))


#Slide to the left! Slide to the right!
shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2
shift_left = shift_left << 2
print(bin(shift_right))
print(bin(shift_left))


#A BIT of This AND That
print(bin(0b1110 & 0b101))


#A BIT of This OR That
print(bin(0b1110 | 0b101))


#This XOR That
print(bin(0b1110 ^ 0b101))


#The Man Behind The Bit Mask
def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired > 0:
    return 'on'
  else:
    return 'off'

print(check_bit4(0b00101))


#Turn it on
a = 0b10111011
mask = 0b100
desired = a | mask
print(bin(desired))


#Just Flip Out
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print(bin(desired))
