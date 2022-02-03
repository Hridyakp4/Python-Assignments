from collections import Counter
string = input("Enter string: ")
dictionary = dict(Counter(string))

Keymax = max(dictionary, key= lambda x: dictionary[x])
print(Keymax)