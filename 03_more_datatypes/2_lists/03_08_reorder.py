'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

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

print(list[1], list[3], list[5], list[7], list[9], list[8], list[6], list[4], list[2], list[0])
