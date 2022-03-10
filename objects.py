from cmath import exp
from math import pi
from os import sep

x = 3
print(x.imag)

my_comp = (12 + 3j) * exp(1j*pi/2)

print("my_comp:", my_comp)
print("my_comp.real:", my_comp.real)
print("my_comp.imag:", my_comp.imag)

###
# assessing number method
ext_bit = 0
for number in range(12341234):
    if(number.bit_length() != ext_bit):
        print(number, number.bit_length(), sep=': ')
        ext_bit = number.bit_length()
