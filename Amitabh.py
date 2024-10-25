# Q1)
# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# Q2)
# number = int(input("Enter a number: "))
# if 100 <= number <= 999:
#     print(f"{number} is a three-digit number")
# else:
#     print(f"{number} is not a three-digit number")

# Q3)
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# Q4)
# number = int(input("Enter a number: "))
# last_digit = abs(number) % 10
# if last_digit == 3:
#     print(f"{number} is ending with 3")
# else:
#     print(f"{number} is not ending with 3")
# Q5)
# alphabet = input("Enter an alphabet: ")
# if alphabet in "aeiou":
#     print(f"{alphabet} is a vowel")
# else:
#     print(f"{alphabet} is a consonant")

# Q6)
# month_name = input("Enter the name of the month: ")
# if month_name in ["January", "March", "May", "July", "August", "October", "December"]:
#     print(f"{month_name} has 31 days")
# elif month_name in ["April", "June", "September", "November"]:
#     print(f"{month_name} has 30 days")
# elif month_name == "February":
#     print(f"{month_name} has 28 or 29 days")
# else:
#     print("Invalid month name")

# Q7)
# sides1 = float(input("Enter the sides of the triangle: "))
# sides2 = float(input("Enter the sides of the triangle: "))
# sides3 = float(input("Enter the sides of the triangle: "))
# if sides1 == sides2 == sides3:
#     print("Equilateral triangle")
# elif sides1 == sides2 or sides2 == sides3 or sides3 == sides1:
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")

# Q8)
# units = int(input("Enter the number of units consumed: "))
# bill_amount = 0
# if units <= 100:
#     bill_amount = 0
# elif units <= 200:
#     bill_amount = (units - 100) * 5
# else:
#     bill_amount = (100 * 5) + ((units - 200) * 10)
# print(f"Bill amount: {bill_amount}")

# Q9)
# cost_price = float(input("Enter the cost price: "))
# if cost_price > 100000:
#     tax = cost_price * 0.15
# elif cost_price > 50000:
#     tax = cost_price * 0.10
# elif cost_price <= 50000:
#     tax = cost_price * 0.05
# print(f"Tax amount: {tax}")

# Q10)
# Market_price = float(input("Enter the market price: "))
# if Market_price > 7000:
#     discount = Market_price * 0.20
# elif Market_price > 7000 <= 10000:
#     discount = Market_price * 0.15
# else:
#     Market_price < 7000
#     discount = Market_price * 0.10
# print(f"Discount amount: {discount}")

# write a program where to accept number from user until user wants then take sum and calculate the average of the numbers
def calculate_sum_and_average():
    numbers = []
    while True:
        try:
            num = float(input("Enter a number (or type 'done' to finish): "))
            numbers.append(num)
        except ValueError:
            # Check if the user wants to stop entering numbers
            done = input("Do you want to finish? Type 'yes' to stop or 'no' to continue: ").strip().lower()
            if done == 'yes':
                break

    if numbers:
        total_sum = sum(numbers)
        average = total_sum / len(numbers)
        print(f"\nSum of the numbers: {total_sum}")
        print(f"Average of the numbers: {average}")
    else:
        print("\nNo numbers were entered.")

calculate_sum_and_average()

