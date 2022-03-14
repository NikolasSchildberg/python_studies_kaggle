hello = 'hello\nworld'
trip = """hello
world"""
print(hello)
print(trip)
print(hello == trip)

# Iterating
ref_str = 'rolhonewson'
print('which are in "', ref_str, '"', sep='')
for char in hello:
    if char in ref_str:
        print(char, end='')
print('\n')

# Indexes and slicing
print(hello[8])
print(ref_str[3:7])

message = "DrOp Your pHones And gEt your books!"
print(message)
print(message.lower())
print(message.upper())
look_for = 'op'
try:
    print(message.index(look_for))
except:
    print('"', look_for, '" not in "', message, '"', sep='')

# List comprehension form string
vowels = 'aeiouyAEIOUY'
lst_cph = [
    charr + '_'
    for charr in message
    if not (charr in vowels)
]
print("List comprehension:", lst_cph)

# Splitting
message_split = message.split('e')
print("Splitting:", message_split)

# State-of-the-art
s = 'state'
o = 'of'
t = 'the'
a = 'art'
print('-'.join([s, o, t, a]))

# Format method
name = 'Nikolas'
cat = 'Miguilim'
age = 9.31
msg = 'My name is {} and my youngest cat is {}, which is {} months old.'.format(name,cat,age)
print(msg)

import math
from socket import NI_DGRAM
ndig = 3
print(
    "{} rounded to {} decimal digits is {:.3}, and the radius of any circle corresponds to {:.1%} of its diameter".format(math.pi,ndig,10*math.pi,0.50000)
)