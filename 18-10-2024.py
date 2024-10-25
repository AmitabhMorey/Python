# Write a Python script to sort (ascending and descending) a dictionary by value.
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1)))
print("Dictionary in ascending order by value: ", sorted_d)

# Write a Python program to remove duplicates from the dictionary. 
def remove_duplicate(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        if value not in output_dict.values():
            output_dict[key] = value
    return output_dict
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3}
result = remove_duplicate(original_dict)
print("Dictionary after removing duplicates: ", remove_duplicate(original_dict))

# Write a Python program to combine two dictionary by adding values for common keys.
def combine_dict(dict1, dict2):
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
        else:
            result[key] = dict1[key]
    for key in dict2:
        if key not in result:
            result[key] = dict2[key]
    return result
dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}
print("Dictionary after combining: ", combine_dict(dict1, dict2))

# Write a Python program to create a dictionary from a string. ( Track the count of the letters from the string.)
def count_letters(input_string):
    result = {}
    for letter in input_string:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result
input_string = "google.com"
print("Dictionary from string: ", count_letters(input_string))

# Write a Python program to match key and values both, in two dictionaries.
def match_key_values(dict1, dict2):
    result = {}
    for key in dict1:
        if key in dict2 and dict1[key] == dict2[key]:
            result[key] = dict1[key]
    return result
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'd': 3}
print("Matching key-values: ", match_key_values(dict1, dict2))