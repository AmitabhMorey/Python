# Q1) Write a Python program to compute the element-wise sum of given tuples.             Original :    (1, 2, 3, 4)   (3, 5, 2, 1)   (2, 2, 3, 1)
#             Element-wise sum of the said tuples:  (6, 9, 8, 6)
tup1 = (1, 2, 3, 4)
tup2 = (3, 5, 2, 1)
tup3 = (2, 2, 3, 1)
tup4 = tuple(map(sum, zip(tup1, tup2, tup3)))
print("Element-wise sum of the said tuples:", tup4)

# Q2) Write a Python program to convert a given list of tuples to a list of lists. 
#             Original list of tuples: [(1, 2), (2, 3), (3, 4)]
list1 = [(1, 2), (2, 3), (3, 4)]
list2 = [list(elem) for elem in list1]
print("Convert the said list of tuples to a list of lists:", list2)

# Q3) Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
list1 = [(1, 2), (2, 3), (3, 4)]
list2 = [list(elem) for elem in list1]
print("Convert the said list of tuples to a list of lists:", list2)

# Q4) Write a Python program to remove an empty tuple(s) from a list of tuples.
list1 = [(1, 2), (), (3, 4), (5, 6), (), (), (7, 8)]
list2 = [elem for elem in list1 if elem]
print("After removing empty tuple(s) from the said list of tuples:", list2)

# Q5) Write a Python program to convert a given string to a tuple
str1 = "Python"
tup1 = tuple(str1)
print("Convert the said string to a tuple:", tup1)

# Q6) Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
tup1 = (1, 2, 3, 4, 5)
result = 1
for elem in tup1:
    result *= elem
print("Product of all the numbers in the given tuple:", result)