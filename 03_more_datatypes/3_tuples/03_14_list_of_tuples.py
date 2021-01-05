'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

string = str(input("Write string: "))

list_1 = string.split()
list_2 = []
for x in list_1:
    list_2.append(tuple(x))








print(list_2)




