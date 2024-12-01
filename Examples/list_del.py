# 
# Fun with lists 
# 
# Deleting 

a_list = ['a','b','c','d']

# You can delete an element from a list with del 

print(a_list)
del a_list[2]
print(a_list)

# Remember though, that now the list is shorter. This illustrates that nicely: 

a_list = [1, 2, 4, 8]
for index in range ( len ( a_list )):
    del a_list [ index ]
    print (index, len( a_list ))

# This results in an error!
