# print(3<=9)
# print(7>9)
# print(6>3 and 6>9)
# print(6>3 or 6>9)
# print(not 6>3)
# a = 5
# b = 10
# print(bin(a))
# print(bin(b))
# print(bin(a&b))
# print(a|b)
# print(~a)
# print(a<<1)
# print(b>>1)
# print(bin(8))
# print(8<<1)
# print(bin(16))
# a = 5
# a+=10
# print(a)
# a = [5,7,8,3,9,2]
# print(3 in a)
# print(10 in a)
# print(10 not in a)

# sname = input("Enter your name: ")
# contact = input("Enter your contact number: ")
# address = input("Enter your address: ")

# print = ("Name: ", sname)
# print = ("Contact: ", contact)
# print = ("Address: ", address)

# amount = float(input("Enter the amount: "))
# year = float(input("Enter the number of years: "))
# rate = float(input("Enter the rate of interest: "))
# simple_interest = amount*year*rate/100
# print("The simple interest is:", simple_interest)

# email = input("Enter your email address: ")
# print = ("Your domain name is: ", email.split('@')[-1])
# print = ("Your email provider is: ", email.split('@')[0]) 

# colour = input("Enter your favourite colour: ")

# if colour == "red":
#     print("I like red too!")
# print("End of program")

# marks = int(input("Enter your marks: "))
# if marks >= 80:
#     print("You got an A")
# elif marks >= 60:
#     print("You got a B")

# number = int(input("Enter a number: "))
# if number%2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# a = 10
# b = 20
# min = "a is minimum" if a<b else "b is minimum"
# print(min)

# a = 10
# b = 20
# even = "a is even" if a%2 == 0 else "b is even"
# print(even)

# Built in String Methods
# capitalize()
# casefold()
# center()
# count()
# encode()  
# endswith()
# expandtabs()
# find()
# format()
# format_map()
# index()
# isalnum()
# isalpha()
# isascii()
# isdecimal()
# isdigit()
# isidentifier()
# islower()
# isnumeric()
# index()
# isupper()
# join()

# s1 = 'Python Programming'
# print(s1.isupper())
# print(s1.islower())
# print(s1.istitle())

# s1 = 'Python Programming'
# print(s1.startswith('Py'))
# print(s1.endswith('ing'))
# str.isalnum()
# str.isalpha()
# str.isascii()
# str.isdecimal()
# str.isdigit()
# str.isidentifier()
# str.islower()
# str.isnumeric()

# L1=('ITM',',','BTECH',',','CSE')
# print('',join(L1))

# Python Functions
# def sum(numbers):
#     s=0
#     for n in numbers:
#         s=s+n
#     print("sum of ", numbers,"=",s)
# sum([1,2,3,4,5])

# write a program where to accept number from user until user wants then take sum and calculate the average of the numbers
# def sum(numbers):
#     s=0
#     for n in numbers:
#         s=s+n
#     print("sum of ", numbers,"=",s)
#     print("Average of ", numbers,"=",s/len(numbers))
# numbers = []
# while True:
#     num = int(input("Enter a number: "))
#     numbers.append(num)
#     choice = input("Do you want to enter another number? (yes/no): ")
#     if choice == 'no':
#         break
# sum(numbers)

# def calculator(a, b):
#     sum = a+b
#     diff = a-b
#     prod = a*b
#     div = a/b
#     return sum, diff, prod, div
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# s, d, p, q = calculator(a, b)
# print("Sum: ", s)
# print("Difference: ", d)
# print("Product: ", p)
# print("Division: ", q)

# def calculator(a, b): # without using print
#     sum = a+b
#     diff = a-b
#     prod = a*b
#     div = a/b
#     return sum, diff, prod, div
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# s, d, p, q = calculator(a, b)

# G1 = 10
# def sample(n):
#     L1 = 0 
#     global G2
#     G2 = 20
#     L1 = L1 + n + G1 + G2
#     print("L1 = ", L1)
# sample(5)
# print("G1 = ", G1)
# print("G2 = ", G2)
 
# global a
# def scopeDemo():
#     a = 10
    
#     print("a =", a)
# scopeDemo()

# def factorial(n):
#     if n == 1:
#         return
#     else:
#         return n * factorial(n-1)

# create a menu to add, view and remove a member in group
# def add_member(group):
#     member = input("Enter the member name: ")
#     group.append(member)
#     print("Member added successfully!")
#     return group
# def view_member(group):
#     print("The members in the group are: ", group)
# def remove_member(group):
#     member = input("Enter the member name to remove: ")
#     group.remove(member)
#     print("Member removed successfully!")
#     return group
# group = []
# while True:
#     print("1. Add member")
#     print("2. View member")
#     print("3. Remove member")
#     print("4. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         group = add_member(group)
#     elif choice == 2:
#         view_member(group)
#     elif choice == 3:
#         group = remove_member(group)
#     elif choice == 4:
#         break
#     else:
#         print("Invalid choice! Please enter a valid choice.")

# thisdict ={
#     "brand": "Ford",
#     "model": "Mustang",
#     "year" :  1964
# }
# x = thisdict["model"]
# print(x)

# Types of inheritance
# 1. Single inheritance
# 2. Multiple inheritance
# 3. Multilevel inheritance
# 4. Hierarchical inheritance
# 5. Hybrid inheritance

# class vehicle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def DisplayDetails(self):
#         print("brand: ", "model: ",  "year: ")
# class swift(vehicle):
#     def __init__(self, brand, model, year):
#         super().__init__(brand, model, year)
#         self.brand =  "Hundai"
#         self.model =  "i20"
#         self.year = 2020
#     def DisplayDetails(self):
#         print("brand: ", self.brand, "model: ", self.model, "year: ", self.year)
#         swift1 = swift("Hundai", "i20", 2020)
#         swift1.DisplayDetails()
#         vehicle1 = vehicle("Ford", "Mustang", 1964)
#         vehicle1.DisplayDetails() 
#         print("brand: ", vehicle1.brand, "model: ", vehicle1.model, "year: ",  vehicle1.year)    

# class vehicle:
#     speed = 50
#     def __init__(self, mk, md):
#         self.make = mk
#         self.modle = md
    
#     def DisplayDetails(self):
#         print("make: ", self.make, "model: ", self.modle)

# class swift(vehicle):
#     speed = 100
#     def __init__(self, mk, md):
#         super().__init__(mk, md)
    
#     def speed_details(self):
#         print("speed: ", self.speed)

# o2 = swift('Hundai', 'Dezire')
# o2.DisplayDetails()
# o2.speed_details()  

# Hierarchial
# class student:
#     def setPersonal(self):
#         self.name = input("Enter name: ")
#         self.rollno = int(input("Enter roll no: "))

#     def getPersonal(self):
#         print("Name: ", self.name, "Roll No: ", self.rollno)

# class fy(student):
#     def getmarks(self):
#         self.s1 = int(input("Enter subject marks: "))
#         self.s2 = int(input("Enter subject marks: "))
#         self.s3 = int(input("Enter subject marks: "))

# Access Codes
