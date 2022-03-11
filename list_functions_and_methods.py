# Creating data
import this


numbers = [1, 2, 3, 4, 5, 6]
cities = ["Taubaté", "Ubatuba", "São Paulo", "Ilhabela"]

# Playing around
print("len(cities):", len(cities))
print("sorted(numbers):", sorted(numbers))
print("sorted(cities):", sorted(cities, reverse=True),)
# print("sum(cities):",sum(cities))
print("sum(numbers):", sum(numbers))
print("max(numbers):", max(numbers))

cities.append("Rio de Janeiro")
print("Now:", cities)
print("Popped:", cities.pop(2), cities)


def find_city(this_city):
    if(this_city in cities):
        print(this_city, " found at cities[",
              cities.index(this_city), "]", sep="")
    else:
        print("City", this_city, "not found in cities.")


this_city = "Ilhabela"
find_city(this_city)
this_city = "São Paulo"
find_city(this_city)
