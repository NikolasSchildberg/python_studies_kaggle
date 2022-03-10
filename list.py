# Creating lists
my_list = [1, 2, 3]
my_mixed_list = ["That's a list with", 4,
                 "items with different types, such as", type(my_list)]

# Printing on screen
print(my_list)
for item in my_mixed_list:
    print(item, end=" ")
