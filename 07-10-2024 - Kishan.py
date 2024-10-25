# Q1)
# Check wheather the string is symmetrical or palindrome
string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is symmetrical")
else:
    print("The string is palindrome")

half = len(string) // 2
if string[:half] == string[-half:][::-1]:
    print("The string is symmetrical")
else:
    print("The string is palindrome")

# Q2)
# Find length of string without using len() function
string = input("Enter a string: ")
count = 0
for i in string:
    count += 1
print("Length of string is", count)

# Q3)
# Remove duplicates from string
string = input("Enter a string: ")
new_string = ""
for i in string:
    if i not in new_string:
        new_string += i
print("String after removing duplicates:", new_string)

# Q4)
# Maximum occuring character in string
string = input("Enter a string: ")
max_char = ""
max_count = 0
for i in string:
    if string.count(i) > max_count:
        max_count = string.count(i)
        max_char = i
print("Maximum occuring character is", max_char)

# Q5)
# Count number of characters in string
string = input("Enter a string: ")
char_count = len(string)
for i in string:
    print(i, end=" ")

# Q6)
# Count all letters, digits, spaces and special characters from string
string = input("Enter a string: ")
letter_count = 0
digit_count = 0
space_count = 0
special_count = 0
for i in string:
    if i.isalpha():
        letter_count += 1
    elif i.isdigit():
        digit_count += 1
    elif i.isspace():
        space_count += 1
    else:
        special_count += 1
print("Letters:", letter_count)
print("Digits:", digit_count)
print("Spaces:", space_count)
print("Special Characters:", special_count)

# Q7)
# Read incoming email, all email not sent from the "@itm.edu" domain should be moved to the spam box
email = input("Enter email: ")
if "@itm.edu" not in email:
    print("Email moved to spam box")
else:
    print("Email received")

# Q8)
# password validator 
password = input("Enter password: ")
if len(password) < 6:
    print("Password must be atleast 6 characters long")
elif password.isalpha():
    print("Password must contain atleast 1 digit")
elif password.isdigit():
    print("Password must contain atleast 1 letter")
else:
    print("Password is valid")
    print("Password is strong")