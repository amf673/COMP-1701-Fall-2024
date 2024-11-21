# 
# Coordinated Lists 
# 
# 

def main()-> None:
    """ coordinated lists with animals and the number 
    of sightings. """
    # intialize two empty lists. 
    animals = []
    sightings = []
    animal = input("Enter the animal sighted (END to finish): ")
    while animal != "END": 
        number = int(input(f"Enter the number of {animal} seen: "))
        animals.append(animal)
        sightings.append(number)
        animal = input("Enter the animal sighted (END to finish): ")

    print(f"{'Animal':^20}{'Sightings':^20}")
    print(f"{'-'*40}")
    for i in range(0, len(animals)):
        print(f"{i+1:4}. {animals[i]:<16}{sightings[i]:>15}")
    print()

main()
