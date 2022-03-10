# Creating data
evens = []
for number in range(0,25):
    if(number % 2 == 0):
        evens.append(number)

print("evens: ",evens)

# Changing
evens[3] = "Number 6 should be here"
evens[8] = " Where's 16? "
print(evens)