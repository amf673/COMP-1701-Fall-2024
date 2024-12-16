# 
# Ways to read a file 

# These are equivalent:

## 1. Line by line... 

inpfile = open("nums.txt", "r")
lines = []
line = inpfile.readline()
while line != "":
   lines.append(line)
   line = inpfile.readline()
inpfile.close()
print(lines)

## 2. Using a for ... 
inpfile = open("nums.txt", "r")
lines = []
for line in inpfile:
    lines.append(line)
inpfile.close()
print(lines)

## 3. Using readlines()... 
inpfile = open("nums.txt", "r")
lines = inpfile.readlines()
inpfile.close()

print(lines)

inpfile.close()
