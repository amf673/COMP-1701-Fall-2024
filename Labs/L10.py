# 
# Lab 10
# 
# 

def enter_cities()->list: 
    """ Enter cities and return them as 
    a list of strings """

    cities = []
    city = input("Enter a city: ")
    while city != "":
        cities.append(city)
        city = input("Enter a city: ")
    
    return cities


def enter_population(cities:list)->list:

    populations = []
    for i in range(len(cities)):
        pop = int(input(f"Enter the population for {cities[i]}: "))
        populations.append(pop)

    return populations

def find_pop(city: str, cities:list, populations:list)->int: 
    """ return the population for city """

    pop = 0 
    if city in cities:
        ## do this the long way 
        i = 0 
        while i < len(cities) and cities[i] != city:
            i = i + 1
        pop = populations[i]

    return pop


def main():

    cities = enter_cities()
    populations = enter_population(cities)

    print(cities)
    print(populations)

    city = input("city to find population ")

    print(f"The pop of {city} is {find_pop(city, cities, populations)}")

main()