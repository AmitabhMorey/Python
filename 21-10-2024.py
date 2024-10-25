# 1. Write a Python class that has two methods: get_String and print_String , get_String accept a string from the user and print_String prints the string in upper case.
class StringManipulator:
    def __init__(self):
        self.string = ""
        
    def get_String(self):
        self.string = input("Enter a string: ")
        
    def print_String(self):
        print(self.string.upper())

obj =  StringManipulator()
obj.get_String()
obj.print_String()

# 2. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed"
        
calc =  Calculator()

result =  calc.add(10, 5)
print("10 + 5:", result)

result =  calc.subtract(20, 7)
print("20  - 7:", result)

result =  calc.multiply(50, 56)
print("50  * 56:", result)

result =  calc.divide(78, 91)
print("78   / 91:", result)

# 3. Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle.
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
if  __name__ == "__main__":
    circle = Circle(5)
    print("Area of circle:", circle.area())
    print("Perimeter of circle:", circle.perimeter()) 

# 4. Write a Python class to implement pow(x, n).
class Power:
    def __init__(self, x, n):
        self.x = x
        self.n = n
        
    def pow(self):
        if self.n == 0:
            return 1
        elif self.n < 0:
            return 1 / (self.x ** -self.n)
        else:
            return self.x ** self.n
        
    def _power_helper(self, x, n):
        if n == 0:
            return 1
        half = self._power_helper(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
        
if __name__ ==  "__main__":
    power_calculator = Power(2, 10)
    print("2 ^ 10:", power_calculator.pow())
    
    power_calculator_neg =  Power(2, -7)
    print("2 ^ -7:", power_calculator_neg.pow())

# 5. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
class ShoppingCart:
    def __init__(self):
        # Initialize an empty cart
        self.items = {}

    def add_item(self, name, price, quantity=1):
        """Add an item to the cart."""
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}

    def remove_item(self, name, quantity=1):
        """Remove an item from the cart."""
        if name in self.items:
            if self.items[name]['quantity'] > quantity:
                self.items[name]['quantity'] -= quantity
            elif self.items[name]['quantity'] == quantity:
                del self.items[name]  # Remove item completely if quantity is zero
            else:
                print(f"Cannot remove {quantity} of {name}. Only {self.items[name]['quantity']} in cart.")
        else:
            print(f"{name} not found in the cart.")

    def calculate_total(self):
        """Calculate the total price of items in the cart."""
        total = 0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total

    def display_cart(self):
        """Display items in the cart."""
        if not self.items:
            print("Cart is empty.")
        else:
            for name, info in self.items.items():
                print(f"{name}: ${info['price']} x {info['quantity']}")

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Apple", 0.99, 3)
    cart.add_item("Banana", 0.50, 2)
    cart.display_cart()
    print(f"Total: ${cart.calculate_total():.2f}")
    cart.remove_item("Apple", 1)
    cart.display_cart()
    print(f"Total: ${cart.calculate_total():.2f}")

# 6. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details. 
# Sample Employee Data:
# "ADAMS", 'E7876', 50000, "ACCOUNTING"
# "JONES", 'E7499', 45000, "RESEARCH"
# "MARTIN", 'E7900', 50000, "SALES"
# "SMITH", 'E7698', 55000, "OPERATIONS"
# (A)Use 'assign_department' method to change the department of an employee.
# (B)Use 'print_employee_details' method to print the details of an employee.
# (C)Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following
# formula:
# overtime = hours_worked - 50
# Overtime amount = (overtime * (salary / 50))
class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (self.emp_salary / 50))
            total_salary  = self.emp_salary + overtime_amount

        else:
            total_salary = self.emp_salary
        return total_salary
        
    def emp_assign_department(self, new_department):
        self.emp_department = new_department
    
    def print_employee_details(self):
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")
        
employee1 = Employee("ADAMS", 'E7876', 50000, "ACCOUNTING")
employee2 = Employee("JONES", 'E7499', 45000, "RESEARCH")
employee3 = Employee("MARTIN", 'E7900', 50000, "SALES")
employee4 = Employee("SMITH", 'E7698', 55000, "OPERATIONS")

employee1.emp_assign_department("Finance")
employee1.print_employee_details()

hours_worked = 60
new_salary = employee1.calculate_emp_salary(hours_worked)
print(f"New salary after {hours_worked} hours_worked: {new_salary}")  

# 7. Write a  Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.
class BankAccount:
    def __init__(self, account_number,customer_name, date_of_opening, balance = 0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit sucessful! New Balance: {self.balance}")
        else:
            print("Invalid amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal successful! New Balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount. Please enter a positive number.")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

account1  = BankAccount('123456789', 'Amitabh Morey', '2020-01-01', 56000000)
account1.deposit(780000)
account1.withdraw(500000)
account1.check_balance()
account1.display_account_details()  

# 8. Create a class hierarchy for different types of geometric shapes, including circles, rectangles, and triangles, using inheritance.
# Tasks:
# A. Define a base class called Shape with common attributes like colour and area.
# B. Implement subclasses for specific shape types such as Circle, Rectangle,
# and Triangle. Each subclass should inherit from the Shape class.
# C. Incorporate additional attributes and methods specific to each shape type. For
# example, a Circle class might have attributes like radius and methods
# like calculate_area.

# D. Use inheritance to create subclasses representing variations within each shape
# type. For example, within the Rectangle class, create subclasses
# for Square and Parallelogram.
# E. Implement methods or attributes in the subclasses to demonstrate how inheritance
# allows for the sharing of attributes and methods from parent classes.
# F. Create instances of the various shape classes and test their functionality to ensure
# that attributes and methods work as expected. 
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

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
        self.calculate_area()
    
    def calculate_area(self):
        self.area = self.width * self.height
    
    def print_details(self):
        super().print_details()
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")

class Square(Rectangle):
    def __init__(self, color, side_length):
        super().__init__(color, side_length, side_length)

class Parallelogram(Rectangle):
    def __init__(self, color, base, height):
        super().__init__(color, base, height)
        self.base = base
        self.height = height

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height
        self.calculate_area()
    
    def calculate_area(self):
        self.area = 0.5 * self.base * self.height
    
    def print_details(self):
        super().print_details()
        print(f"Base: {self.base}")
        print(f"Height: {self.height}")

circle = Circle("Red", 45)
circle.print_details()

rectangle = Rectangle("Blue", 74, 66)
rectangle.print_details()

square = Square("Green", 25)
square.print_details()

parallelogram = Parallelogram("Yellow", 38, 94)
parallelogram.print_details()

triangle = Triangle("Purple", 86, 43)
triangle.print_details()

# 9. Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
# Note: The bus seating capacity is 50. so the final fare amount should be 5550. You need to override the fare() method of a Vehicle class in Bus class.
class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name 
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity *100
    
class Bus(Vehicle):
    def __init__(self, name, seating_capacity = 70):
        super().__init__(name, seating_capacity)

    def fare(self):
        total_fare = super().fare()
        maintenance_charge = 0.2 * total_fare
        final_amount = total_fare + maintenance_charge
        return final_amount
    
bus = Bus("City Bus")
print(f"Total bus fare is: {bus.fare()}")
# END