# Q1)
# write a python program to reverse the order of the items in the array.
def reverse_list(l):
    return l[::-1]
l = [1,2,3,4,5]
print(reverse_list(l))

# Q2)
# write a python program to get the number of occurences  of a specified element in an array.
def count_occurences(l, n):
    return l.count(n)
l = [1,2,3,4,5,1,2,3,4,5]
n = 1
print(count_occurences(l, n))

# Q3)
# write a python program to find out if any given array of integers contains any duplicate elements.
def contains_duplicates(l):
    return len(l) != len(set(l))
l = [1,2,3,4,5]
print(contains_duplicates(l))

# Q4)
# write a python program to find the missing number in a given integer array of 5 continuous number.
def find_missing(l):
    return 18 - sum(l)
l = [1,2,3,4,5]
print(find_missing(l))

# Q5)
# Replace all odd numbers in the given array with -1.
def replace_odd(l):
    return [-1 if n % 2 != 0 else n for n in l]
l = [1,2,3,4,5]
print(replace_odd(l))