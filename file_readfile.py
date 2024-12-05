# An example of reading a text file. 
# 
# readbylines.py demonstrates how to read a file line by line. 
# In some cases (small files) there is another method that 
# can be used. 
# 
# file.readlines() 
#
# which reads the whole text file as a string and breaks 
# it up into lines and returns a list of lines.
# 


input_file = open("lyrics.txt", "r")
print("No.  Chars Words -- Text")
print("----------------------------")

lines = 0
words = 0
chars = 0
# Read all the lines
all_lines = input_file.readlines()

for line in all_lines:
    lines = lines + 1
    word_per_line = len(line.split())
    words = words + word_per_line
    chars = chars + len(line)
    print(f"{lines:>3}. {len(line):>5} {words:>3}   -- {repr(line)}")

input_file.close()

print(f"lines = {lines:>10}")
print(f"words = {words:>10}")
print(f"characters = {chars:>8}")
