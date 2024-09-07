# # Class and Object

# class Student:
#     name = "Mob Pyscho"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class Car:
#     color = "black"
#     brand = "Bentley"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# # __init__ Function

# class Student:
    
#     # Default Parameters
#     def __init__(self):
#         pass

#     # parameterized constructors
#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#         print("adding new student in Database")

# s1 = Student("Mob Pyscho", 85)
# print(s1.name, s1.marks)
 
# s2 = Student("Yuji Itadori", 95)
# print(s2.name, s2.marks)

# class Student:
#     college_name = "ITM Skills University"
#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#         print("adding new student in Database")

# s1 = Student("Mob Pyscho", 85)
# print(s1.name, s1.marks)
 
# s2 = Student("Yuji Itadori", 95)
# print(s1.name, s2.marks)

# print(Student.college_name)

# class Student:
#     college_name = "ITM Skills University"
#     name = "anonymous" #class attr
#     def __init__(self, fullname, marks):
#         self.name = fullname  #obj attr > class attr
#         self.marks = marks
#         print("adding new student in Database")

# s1 = Student("Mob Pyscho", 85)
# print(s1.name)

# class Student:
#     college_name = "ITM Skills University"
    
#     def __init__(self, fullname, marks):
#         self.name = fullname  #obj attr > class attr
#         self.marks = marks
    
#     def welcome(self):
#         print("welcome student", self.name)

#     def get_marks(self):
#         return self.marks 

# s1 = Student("Mob Pyscho", 85)
# s1.welcome()
# print(s1.get_marks())

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hello", self.name, "your avg score is:", sum/3)

# s1 = Student("Bruce Wayne", [97, 99, 98])
# s1.get_avg()
# s1.hello()

# s1.name = "Batman"
# s1.get_avg()

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started...")

# car1 = Car()
# car1.start()


# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("Total balance =", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("Total balance =", self.get_balance())

#     def get_balance(self):
#         return self.balance


# # Taking input from the user
# initial_balance = float(input("Enter initial balance: "))
# account_number = input("Enter account number: ")

# # Creating an Account object
# acc1 = Account(initial_balance, account_number)

# # Performing debit and credit operations
# debit_amount = float(input("Enter the amount to debit: "))
# acc1.debit(debit_amount)

# credit_amount = float(input("Enter the amount to credit: "))
# acc1.credit(credit_amount)

# del keyword
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Don")
# print(s1.name)
# del s1.name
# print(s1.name)

# Private attributes and methods
