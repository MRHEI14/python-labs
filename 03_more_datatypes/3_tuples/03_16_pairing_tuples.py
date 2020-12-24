'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

string = input("Input Numbers: ")

list_1 = string.split()
for i in range(0, len(list_1)):
    list_1[i] = int(list_1[i])

list_1.sort()
list_2 = ()

for i, tup2 in list_1:
    for tup1 in i:
        list_2 = (tup1, tup2)


print("list_2 =", list_2)

