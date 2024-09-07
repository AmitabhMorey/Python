f = open("/Users/amitabhmorey/Documents/Python folder/file input & output.txt", "rt")

data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

f = open("/Users/amitabhmorey/Documents/Python folder/file input & output.txt", "w")

f.write("I want to lean Javascript. 10092024")

f.close()

f = open("/Users/amitabhmorey/Documents/Python folder/file input & output.txt", "a")

f.write("Then I want to learn C++.")

f.close()


f = open("/Users/amitabhmorey/Documents/Python folder/file input & output.txt", "a")

f.write("\nAfter that Rust.")

f.close()

f = open("sample.txt", "a")
f.close()  #sample.txt does not exist but we open it with write or append new file is created

f = open("file input & output.txt", "r+") #r+ writes from start of file
f.write("a,b,c")
print(f.read())
f.close()

f = open("file input & output.txt", "a+") #a+ start write from end

print(f.read())
f.write("abc")
f.close()

# with syntax, while using with syntax there is no need to close syntax
with open("file input & output.txt", "r") as f:
    data = f.read()
    print(data) 

with open("file input & output.txt", "w") as f:
    f.write("new data")

# deleting a file
import os

os.remove("sample.txt")

# Practise Questions
with open("practise.txt", "w") as f:
    f.write("Hi everyone\nI am learning File I/O.\n")
    f.write("using java\nI like programing in java.")

with open("practise.txt", "r") as f:
    data = f.read()

new_data= data.replace("java", "Python")
print(new_data)

with open("practise.txt", "w") as f:
    f.write(new_data)

def check_for_word():
    word = "learning"
    with open("practise.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("not found")

check_for_word()

def check_for_line():
    word = "programing"
    data = True
    line_no =  1
    with open("practise.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

check_for_line()

def check_for_line():
    word = "opr"
    data = True
    line_no =  1
    with open("practise.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

print(check_for_line()) 

with open("practise.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]

count = 0
with open("practise.txt", "r") as f:
    data = f.read()
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)

