count = 1
while count <=7 :
    print("Hello")
    count += 1 

i = 1
while i <= 1000000:
    print("one piece", i)
    i += 1

i = 10
while i >= 1:
    print(i)
    i -= 1

print("loop ended")

i = 1
while i <= 100:
    print(i)
    i+=1

i = 100
while i>=1:
    print(i)
    i-=1

n =int (input("enter number : "))
i = 1
while i<= 10:
    print(n * i)
    i += 1

nums  = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
strawhatcrew = ["luffy", "zoro", "sanji", "nami", "robin"]

idx = 0
while idx < len(strawhatcrew):
    print(strawhatcrew[idx])
    idx += 1 

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1
  
nums  = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 49

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND INDEX", i)
        break
    else:
        print("finding")
    i += 1

print("end of loop")

i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

print("end of loop")

i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

i = 0
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1

nums = [65,78,90,103,75,84]

for val in nums:
    print(val)

tup = (3,7,8,5,0,1,6,4,2,5)

for num in tup:
    print(num)

str = "monkey luffy"

for cha in str:
    print(cha)
else:
    print("end")

str = "monkey luffy"

for cha in str:
    if(cha == 'o'):
        print("o found")
        break
    print(cha)
else:
    print("end")

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 81)
x = 81
idx = 0
for val in num:
    if(val == x):
        print("number found at index", idx) 
        break
    idx += 1

for i in range(10):
    print(i)

for i in range(2,10):
    print(i)

for i in range(2,10,2):
    print(i)

for i in range(1,101,2):
    print(i)

for i in range(101):
    print(i)

for i in range(101,0,-1):
    print(i)

n = int(input("enter number : "))

for i in range(1,11):
    print(n * i)

for i in range(7):
    pass

if i > 5:
    pass

print("to be continued")

n = 89

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total sum=", sum)

n = 7
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print("factorial=", fact)

n =  12
fact = 1

for i in range(1, n+1):
    fact *= i

print("factorial=", fact)