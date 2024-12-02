
#
# finding a value in a list using a loop with a 
# compound condition 
#

animals = ['bear', 'deer', 'marten', 'pika', 'chipmunk']

animal = input("Enter the animal to search for: ").strip().lower()

i = 0 
while i < len(animals) and animals[i] != animal:
    i = i + 1
if i >= len(animals): 
    print("not found")
else: 
    print(f"found {animal} at position {i}")

