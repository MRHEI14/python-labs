'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
list_2 = []
for x in list:
    if x not in list_2:
           list_2.append(x)
print(list_2)






