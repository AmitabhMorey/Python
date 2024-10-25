# Q1)
# Multiplication Table
num = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# Q2)
# Count total number of digits in a number
num = int(input("Enter the number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print(f"Total number of digits: {count}")

# Q3)   
# Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)-1, -1, -1):
    print(list1[i])

# Q4)
# Print all prime numbers with a range
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
for i in range(start, end+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")

# Q5)
# Fibonacci Series up to 10 Terms
n = 10
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a+b
    count += 1
print()

# Q6)
# Reverse a integer number
num = int(input("Enter the number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10
print(f"Reverse number: {rev}")

# Q7)
# Initialize sums for evens and odds
n = 100
sum_even = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"Sum of even numbers: {sum_even}")

# Q8)
# program that accepts a string and calculates the number of digits and letters.
string = input("Enter the string: ")
digits = 0
letters = 0
for i in string:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1
print(f"Number of digits: {digits}")
print(f"Number of letters: {letters}")

# Q9)
#Write a Python program to print the pattern using a loop.
# (a)
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# (b)
# print star pattern
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()