# Q1) Write a python program to remove duplicates from a list.
def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list
list = [1, 2, 2, 3, 4, 4,]
print(remove_duplicates(list))

# Q2) Write a python function that takes two lists and return True if they have at least one common member.
def common_member(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
print(common_member(list1, list2))

# Q3) Write a Python program to print the numbers of a specified list after removing even numbers from it.
def remove_even(list):
    new_list = []
    for i in list:
        if i%2 != 0:
            new_list.append(i)
    return new_list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(remove_even(list))

# Q4) Write a Python program to find the second smallest number in a list.
def second_smallest(list):
    list.sort()
    return list[1]
list = [1, 2, 3, 4, 5]
print(second_smallest(list))

# Q5) Write a Python program to split a list every Nth element.
def split_list(list, n):
    new_list = []
    for i in range(0, len(list), n):
        new_list.append(list[i:i+n])
    return new_list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
print(split_list(list, n))

# Q6) Write a Python a function to find the union and intersection of two lists.
def union_intersection(list1, list2):
    union = list1 + list2
    intersection = []
    for i in list1:
        if i in list2:
            intersection.append(i)
    return union, intersection
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
print(union_intersection(list1, list2))

# Q7) Write a Python function to check if a list is a palindrome or not. Return true otherwise false.
def palindrome(list):
    return list == list[::-1]
list = [1, 2, 3, 2, 1]
print(palindrome(list))