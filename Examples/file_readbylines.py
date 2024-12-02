# An example of reading a text file. 
# 
# This one displays line numbers, the number of characters and the 
# number of words for the file. Note the use of repr(). With a string 
# repr() will show the newlines, tabs, etc. using escape characters. 

input_file = open("lyrics.txt", "r")
print("No.  Chars Words -- Text")
print("----------------------------")

lines = 0
words = 0
chars = 0
line = input_file.readline()    # reads the next line of the file. Reading is one way. No going back. 
while line != "":               # readline() returns an empty string when we are at the end of the file. 

    lines = lines + 1
    word_per_line = len(line.split())
    words = words + word_per_line
    chars = chars + len(line)
    print(f"{lines:>3}. {len(line):>5} {words:>3}   -- {repr(line)}")

    line = input_file.readline()
input_file.close()

print(f"lines = {lines:>10}")
print(f"words = {words:>10}")
print(f"characters = {chars:>8}")
