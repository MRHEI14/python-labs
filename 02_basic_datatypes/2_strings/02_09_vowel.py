'''
    Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
sentence = input("Type sentence: ")
vowel_counts = {}
for vowel in "aeiou":
    s_count = sentence.count(vowel)
    vowel_counts[vowel] = s_count
print(vowel_counts)

s_counts = vowel_counts.values()
total_vowels = sum(s_counts)
print(total_vowels)

