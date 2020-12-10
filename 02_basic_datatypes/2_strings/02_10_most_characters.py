'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
sen_1 = input("type word: ")
sen_2 = input("type word: ")
sen_3 = input("type word: ")
len_1 = len(sen_1)
len_2 = len(sen_2)
len_3 = len(sen_3)
print(len_1,",", sen_1)
print(len_2,",", sen_2)
print(len_3,",", sen_3)



