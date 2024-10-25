# amount = 1019
# years = 3
# rate = 5.5
# print("Simple Interest = ",(amount*years*rate)/100)

# n = 10
# a, b = 0, 1
# count = 0
# while count < n:
#     print(a)
#     a, b = b, a+b
#     count += 1
# print()

# write a program where to accept number from user until user wants then take sum and calculate the average of the numbers
# def calculate_sum_and_average(num):
#     numbers = []
#     while True:
#         try:
#             num = float(input("Enter a number (or type 'done' to finish): "))
#             numbers.append(num)
#         except ValueError:
#             # Check if the user wants to stop entering numbers
#             done = input("Do you want to finish? Type 'yes' to stop or 'no' to continue: ").strip().lower()
#             if done == 'yes':
#                 break

#     if numbers:
#         total_sum = sum(numbers)
#         average = total_sum / len(numbers)
#         print(f"\nSum of the numbers: {total_sum}")
#         print(f"Average of the numbers: {average}")
#     else:
#         print("\nNo numbers were entered.")

# student = {'rollno.':101, 'sname':'Ajay', 'contact':9987651780, 'fees':758978.86}
# print(student['rollno.'])

# class student:
#     roll = 0
#     sname = ''
#     marks = 95

#     def setdata(self):
#         self.roll = int(input("Enter roll no: "))
#         self.sname = input("Enter student name: ")
#         self.marks = int(input("Enter marks: "))

#     def getdata(self):
#         print("Roll no: ", self.roll)
#         print("Student name: ", self.sname)
#         print("Marks: ", self.marks)

# s1 =  student()
# s2 =  student()
# s1.setdata()
# s2.setdata()

# class sample:
#     def __init__(self):
#         self.n = 10

#     def display(self):
#         print("Number",self.n)

#     def __del__(self):
#         print("Object is destroyed")

# obj1 = sample()
# obj1.display()

# class StringManipulation:
#     def __init__(self):
#         self.string = ""
    
#     def get_String(self):
#         self.string = input("Enter a string: ")
    
#     def print_String(self):
#         print(self.string.upper())

# obj = StringManipulation()
# obj.get_String()
# obj.print_String()

# class Employee:
#     def __init__(self, emp_id, emp_name, emp_salary, emp_department):
#         self.emp_id = emp_id
#         self.emp_name = emp_name
#         self.emp_salary = emp_salary
#         self.emp_department = emp_department
    
#     def calculate_emp_salary(self, hours_worked):
#         if hours_worked > 50:
#             overtime = hours_worked - 50
#             overtime_amount = overtime * (self.emp_salary / 50)
#             total_salary = self.emp_salary + overtime_amount
#         else:
#             total_salary = self.emp_salary
#         return total_salary
    
#     def emp_assign_department(self, new_department):
#         self.emp_department = new_department
    
#     def print_employee_details(self):
#         print(f"Employee ID: {self.emp_id}")
#         print(f"Employee Name: {self.emp_name}")
#         print(f"Employee Salary: {self.emp_salary}")
#         print(f"Employee Department: {self.emp_department}")

# # Sample Employee Data
# employee1 = Employee("E7876", "ADAMS", 50000, "ACCOUNTING")
# employee2 = Employee("E7499", "JONES", 45000, "RESEARCH")
# employee3 = Employee("E7900", "MARTIN", 50000, "SALES")
# employee4 = Employee("E7698", "SMITH", 55000, "OPERATIONS")

# # (A) Assign a new department
# employee1.emp_assign_department("FINANCE")

# # (B) Print employee details
# employee1.print_employee_details()

# # (C) Calculate the salary with overtime
# hours_worked = 60
# new_salary = employee1.calculate_emp_salary(hours_worked)
# print(f"New salary after {hours_worked} hours worked: {new_salary}")

# Base Class
class Shape:
    def __init__(self, color):
        self.color = color
        self.area = 0
    
    def calculate_area(self):
        pass
    
    def print_details(self):
        print(f"Color: {self.color}")
        print(f"Area: {self.area}")

# Subclass for Circle
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        self.calculate_area()
    
    def calculate_area(self):
        # π ≈ 22/7
        self.area = (22 / 7) * self.radius * self.radius
    
    def print_details(self):
        super().print_details()
        print(f"Radius: {self.radius}")

# Subclass for Rectangle
# class Rectangle(Shape):
#     def __init__(self, color, width, height):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#         self.calculate_area()
    
#     def calculate_area(self):
#         self.area = self.width * self.height
    
#     def print_details(self):
#         super().print_details()
#         print(f"Width: {self.width}")
#         print(f"Height: {self.height}")

# # Subclass for Square (inherits from Rectangle)
# class Square(Rectangle):
#     def __init__(self, color, side_length):
#         super().__init__(color, side_length, side_length)

# # Subclass for Parallelogram (inherits from Rectangle)
# class Parallelogram(Rectangle):
#     def __init__(self, color, base, height):
#         super().__init__(color, base, height)
#         self.base = base
#         self.height = height

# # Subclass for Triangle
# class Triangle(Shape):
#     def __init__(self, color, base, height):
#         super().__init__(color)
#         self.base = base
#         self.height = height
#         self.calculate_area()
    
#     def calculate_area(self):
#         self.area = 0.5 * self.base * self.height
    
#     def print_details(self):
#         super().print_details()
#         print(f"Base: {self.base}")
#         print(f"Height: {self.height}")

# # Testing the classes
# circle = Circle("Red", 7)
# circle.print_details()

# rectangle = Rectangle("Blue", 4, 6)
# rectangle.print_details()

# square = Square("Green", 5)
# square.print_details()

# parallelogram = Parallelogram("Yellow", 8, 4)
# parallelogram.print_details()

# triangle = Triangle("Purple", 6, 3)
# triangle.print_details()

class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity
    
    def fare(self):
        return self.seating_capacity * 100

# Subclass Bus that inherits from Vehicle
class Bus(Vehicle):
    def __init__(self, name, seating_capacity=50):
        super().__init__(name, seating_capacity)
    
    def fare(self):
        # Get the base fare from the Vehicle class
        total_fare = super().fare()
        # Add 10% maintenance charge
        maintenance_charge = 0.1 * total_fare
        final_amount = total_fare + maintenance_charge
        return final_amount

# Example usage
bus = Bus("City Bus")
print(f"Total Bus fare is: {bus.fare()}")