'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
for x in list_:
   for y in list_:
        if y == x:
           list_.remove(x)
print(list_)






