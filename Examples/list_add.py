# 
# Fun with lists 
# 
# 

a_list = ['a','b','c','d']

# Loop through the list adding to it as we go. 

for i in range(len(a_list)):
    print( i, a_list[i])
    a_list.append( a_list[i] + a_list[i])
print(a_list)

# Notice that the new elements are not printed. range() creates an iterator when it is 
# invoked and does not get updated. But if we reset and use another technique: 

a_list = ['a','b','c','d']

# Loop through the list adding to it as we go. 

i = 0
for a in a_list:
    print( i, a)
    a_list.append( a )
    i = i + 1

# We get an infinite loop. We keep adding to the loop so we never get to the end. 
