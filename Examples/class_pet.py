class Pet:
  def __init__(self, species, name, age):
    self.species = species
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.species}: Name {self.name}, Age {self.age}"

p1 = Pet("Cat", "Kinu", 18)
p2 = Pet("Dog", "Abby", 5)

print(p1)
print(p2)