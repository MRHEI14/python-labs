'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
n_1 = int(input("1st number: "))
n_2 = int(input("2nd number: "))
n_3 = int(input("3rd number: "))
n_4 = int(input("4th number: "))
n_5 = int(input("5th number: "))
n_6 = int(input("6th number: "))
n_7 = int(input("7th number: "))
n_8 = int(input("8th number: "))
n_9 = int(input("9th number: "))
n_10 = int(input("10th number: "))

list = [n_1, n_2, n_3, n_4, n_5, n_6, n_7, n_8, n_9, n_10]

biggest = 0
for num in list:
    if biggest < num:
        biggest = num
print("Highest number: ", biggest)


product = 1
for x in list:
    product *= x
print("Product of all numbers: ", product)



