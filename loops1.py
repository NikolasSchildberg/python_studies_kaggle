# Iterating through cats' list to print all of them
cats = ["Tim", "Christie", "Madalena", "Miguilim"]
print("Cats:")
for cat in cats:
    print(cat, end=' ')

# Iterating through multiplicands' tuple to find product
print("\n\nProduct:")
multiplicands = (2, 2, 3, 5, 5, 7)
product = 1
for number in (multiplicands):
    product *= number
    if(multiplicands.index(number) != len(multiplicands)-1):
        print(number, end=" x ")
    else:
        print(number, "=", product)

# Iterating through string:
print("\nMessage:")
message = "For this reason, Other RAdio companies BOard outside of danger ZOne"
for letter in message:
    separatorr = ' '
    if letter == " ":
        print(separatorr, end='')
    else:
        print(letter, end='')

# Steganography, only upper case
print('\n\nHidden Message:')
for char in message:
    if char.isupper():
        print(char, end='')

# While Loop. Printing interating variable until reaching 15
print("\n\nWhile Loop. Printing interating variable until reaching 15")
my_var = 3
while (my_var < 15):
    print(my_var, end=',')
    my_var += 1

# List comprehensions
print("\n\nList comprehensions:")
my_numbers = [numb**2 for numb in range(10)]
print("Squares of naturals less than 10:", my_numbers)
my_evens = [num**2 for num in range(10) if (num % 2 == 0)]
print("Squares of even naturals less than 10:", my_evens)

# More of it
loud_8_letter_cats = [
    cat.upper() + '!'
    for cat in cats
    if len(cat) == 8
]
print("\nLoud 8 letter cats:", loud_8_letter_cats)


# Console formatting
print()
