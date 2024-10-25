# Write a Python program to remove an item from a set if it is present in the set.
set1 = {1, 2, 3, 4, 5, 6}
set1.discard(5)
print(set1)

# Write a Python program to check if two given sets have no elements in common.
set1 = {1, 2, 3, 4, 5, 6}
set2 = {7, 8, 9, 10}
if set1.isdisjoint(set2):
    print("Two sets have no items in common")
else:
    print("Two sets have items in common")

# Write a Python program toGet Only unique items from two sets
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
set3 = set1.union(set2)
print(set3)

# Write a Python program to Convert Set to one String
set1 = {'apple', 'banana', 'cherry'}
string = ' , '.join(set1)
print(string)

# program to count number of vowels using sets in given string
string = "Python is a programming language"
vowels = set("aeiou")
count = 0
for i in string:
    if i in vowels:
        count += 1
print(count)