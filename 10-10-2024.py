# Q1)
# Write a Python function to check whether a number falls within a given range
def check_range(num, lower, upper):
    return lower <= num <= upper

print(check_range(5, 1, 10))

# Q2)
#  Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list
def shortest_longest_word(words):
    shortest = min(words, key=len)
    longest = max(words, key=len)
    return (shortest, longest)
print(shortest_longest_word(["apple", "banana", "cherry", "date"]))

# Q3)
# Write a Python function that takes a list and an element as input. The function should add the element to the list only if it's not already present in the list.
def add_element_if_not_present(lst, element):
    if element not in lst:
        lst.append(element)
    return lst
print(add_element_if_not_present([1, 2, 3], 4))

# Q4)
# Write a program to implement these formulae of permutations and combinations. Number of permutations of n objects taken r at a time: p(n, r) = n! / (n-r)!.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
def permutations(n, r):
    return factorial(n) / factorial(n - r)
def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))
n = 5
r = 3
print("Permutations:", permutations(n, r))
print("Combinations:", combinations(n, r))

# Q5)
# A number is called perfect if the sum of proper divisors of that number is equal to the number. For example 28 is perfect number, since 1+2+4+7+14=28.
def sum_of_divisors(n):
    return sum([i for i in range(1, n) if n % i == 0])
def perfect_numbers_in_range(lower, upper):
    return [n for n in range(lower, upper + 1) if sum_of_divisors(n) == n]
lower = 1
upper = 1000
print(perfect_numbers_in_range(lower, upper))

# Q6)
# Write a recursive function that will return the nth term of the Fibonacci sequence.The sequence has a relationship of Fn = Fn-1 + Fn-2 with F0 = 0 and F1 = 1, where n=0,1,2,3,4,5,...
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
n = 10
print(fibonacci(n))