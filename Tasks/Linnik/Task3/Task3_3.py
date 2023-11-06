# 3. Write a program that takes a string as input
# returns a dictionary with the count of each word in the string.
string = "The time for change is now. The time for progress is now. The time for unity is now."
list_of_words = string.split()
dict_of_words = {}
for i in list_of_words:
    if i in dict_of_words:
        dict_of_words[i] += 1
    else:
        dict_of_words[i] = 1
for i in dict_of_words:
    print(i, '-', dict_of_words[i])
