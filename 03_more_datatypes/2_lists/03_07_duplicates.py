'''

Write a script that removes all duplicates from a list.

'''

list = [1, 2, 3, 4, 3, 4, 5]
list_2 = []
for item in list:
    if item not in list_2:
        list_2.append(item)

print(list_2)
