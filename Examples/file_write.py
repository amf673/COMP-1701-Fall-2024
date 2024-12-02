#
# Example of writing to a file 
# 

# We need to open the file for writing. The mode can be 
# either "w" or "a"
# 
#  - "w" open the given path for writing. If the file does not exist, create it, if it does exist
#        delete the contents and rewrite it. 
#  - "a" open an existing file and append to the end of it. If the file does not exist, it is created. 
# 
output_file = open("animals.txt", "w")

i = 0
total_animals = 0
# use a sentinal loop to enter animal species and the number seen. 

animal = input("Enter and animal and the number of sightings (e.g. deer 12) <ret> to end: ")
while animal != "":
    # parse the input 
    species = animal.split()[0]
    number = int(animal.split()[1])

    # update counters
    total_animals += number
    i = i + 1
    
    # write to the file. write() does not add a newline, so if you want that, add it. 
    output_file.write(f"{i:>3}. {number:>5} {species}\n")
    
    # update the loop control variable. 
    animal = input("Enter and animal and the number of sightings (e.g. deer 12) <ret> to end: ")

# always close your file. 
output_file.close()

print(f"{i} species and {total_animals} in total.")
