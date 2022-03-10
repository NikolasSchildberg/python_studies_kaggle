# Creating data
evens = []
for number in range(0,25):
    if(number % 2 == 0):
        evens.append(number)

print("evens: ",evens)

# Slicing
print("10 to 12:",evens[5:7])
print("4 to 18:",evens[2:10])