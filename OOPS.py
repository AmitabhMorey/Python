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

# OOPS part-2 Inheritance and Polymorphism

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Don")
# print(s1.name)
# del s1.name
# print(s1.name)

# # Private attributes and methods
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("23785", "dvjn")

# print(acc1.acc_no)
# print(acc1.reset_pass())

# class Person:
#     __name = "Kizaru"

#     def __hello(self):
#         print("hello world")

#     def welcome(self):
#         self.__hello

# p1 = Person()

# print(p1.welcome())

# class Car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()

# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C() 

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# class Car:
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1 = ToyotaCar("prius", "electric")
# print(car1.type)

# class Person:
#     name = "Kinn"

#     # def changeName(self, name):
#     #     self.name = name

#     @classmethod 
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Ambrish Verma")
# print(Person.name )

# class Student:
#     def __init__(self, phy, bio, chem):
#         self.phy = phy
#         self.chem = chem
#         self.bio = bio

#     # def calcPercentage(self):
#     #     self.percentage = str((self.phy + self.chem + self.bio) / 3) + "%"
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.bio) / 3) + "%"
        
# stu1 = Student(87, 95, 94)
# print(stu1.percentage)

# stu1.phy = 95
# # print(stu1.phy)
# # stu1.calcPercentage()
# print(stu1.percentage)

# # POLYMORPHISM: Operator Overloading
# print(2 + 5)
# print("one" + "piece")  # concatenation
# print([4, 7, 3] + [5, 8, 6])   # list concatenation

# class Complex:
#     def __init__(self, real,  imag):
#         self.real = real
#         self.imag = imag

#     def showNumber(self):
#         print(self.real,"i +", self.imag,"j") 

#     # def add(self, num2):
#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImag = self.imag - num2.imag
#         return Complex(newReal, newImag)

# num1 = Complex(2, 5)
# num1.showNumber()

# num2 = Complex(9, 11)
# num2.showNumber()

# # num3 = num1.add(num2)
# num3 = num1 - num2
# num3.showNumber()  

# #Question
# class Circle:
#     def  __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius
    
# c1 = Circle(28)
# print(c1.area())
# print(c1.perimeter())  

# #Question
# class Employee:
#     def  __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role =", self.role)
#         print("dept =", self.dept)
#         print("salary =", self.salary)

# class  Manager(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Manager", "IT", 50000)

# mana = Manager("Arunabh Kumar", 35)
# mana.showDetails()   

# # Question 
# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, odr2):
#         return self.price > odr2.price

# odr1 = Order("Jam", 50)
# odr2 = Order("coffee", 60)  

# print(odr1 > odr2)