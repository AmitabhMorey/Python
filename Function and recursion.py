def cal_sum(a, b):
    sum = a + b
    print(sum)
    return(sum)

cal_sum(25,18)

cal_sum(9678,4567)

cal_sum(498, 890)

def cal_sum(a, b):
    return a + b

sum = cal_sum(3,7)
print(sum)

def print_hello():
    print("hello")

print_hello()

def print_hello():
    print("hello")

output = print_hello()
print(output)

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(96, 94, 98)

print("one piece", end = " ")
print("straw hat crew")

def cal_prod(a=19, b=187):
    print(a * b)
    return a * b

# cal_prod()

# def cal_prod(a=19, b): we will always give default values from last
#     print(a * b)
#     return a * b

# cal_prod()

cities = ["delhi", "pune", "mmumbai", "chennai", "noida", "nagpur"] 
heros = ["iron man", "batman", "superman", "captain america"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heros)

cities = ["delhi", "pune", "mmumbai", "chennai", "noida", "nagpur"] 
heros = ["iron man", "batman", "superman", "captain america"]

print(heros[0], end=" ")
print(heros[1], end=" ")

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heros)

cities = ["delhi", "pune", "mmumbai", "chennai", "noida", "nagpur"] 
heros = ["iron man", "batman", "superman", "captain america"]

def print_len(list):
    print(len(list))

def print_list(list):
    for  item in list:
        print(item, end=" ")

print_list(cities)
print()

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i 
    print(fact)

cal_fact(5)

def converter(usd_val):
    inr_val = usd_val * 83.9
    print(usd_val, "USD =", inr_val, "INR")

converter(89) 

def check_even_odd(num):
    if num % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

check_even_odd(4)  
check_even_odd(7)  

def show(n):
    if(n == -1):
        return
    print(n)
    show(n - 1)

show(5)

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(8))

def cal_sum(n):
    if(n == 0):
        return 0
    return cal_sum(n-1) + n

sum = cal_sum(9)
print(sum)

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx +1)

fruits = ["apple", "mango", "banana", "orange", "gauva"]

print_list(fruits)