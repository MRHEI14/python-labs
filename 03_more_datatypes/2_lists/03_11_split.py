'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

string = str(input("Write sentence: "))

word_list = string.split()

#from collections import Counter
#words_to_count = (word for word in word_list)
#c = Counter(words_to_count)
#print (c.most_common(1))

print(word_list)

num = 0
for elem in word_list:
    if word_list.count(elem) > num:
        elem += num
print(elem)




