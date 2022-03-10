# Creates list from range object
my_list = list(range(45))

# Manually filters odd numbers
evens = []
for number in my_list:
    if (number % 2 == 0):
        evens.append(number)
print("my_list:", my_list)
print("evens:", evens)

# Using filter method
smart_evens = list(filter(lambda p: p % 2 == 0, my_list))
print("smart_evens:", smart_evens)

# Defining function to filter out evens
def is_odd(entry):
    return entry % 2 == 1
my_odds = list(filter(is_odd, my_list))
print("my_odds:",my_odds)

# Prints the last and penultimate elements
print("Last one:",my_list[-1])
print("Penultimate one:",my_list[-2])

# Prints reverse (2 ways)
reversed = []
for item in range(len(my_list)):
    reversed.append(my_list[-item-1])
print(reversed)