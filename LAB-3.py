#LAB 3
#Saliha Batool
#BCS21042


# Print multiples of 7 and 5 between 1500 and 2700
# q1
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end="  ")

print("---------------------------------------------------------------------------------------------------")

# Convert Celsius to Fahrenheit and vice versa
# q2
def celsius_to_farenheit(celsius):
    farenheit = (celsius * 9 / 5) + 32
    return farenheit

celsius = float(input("Enter temperature in celsius : "))
print(f"Celsius temperature : {celsius}C --- Farenheit temperature : {round(celsius_to_farenheit(celsius), 2)}F")

def farenheit_to_celsius(farenheit):
    celsius = (farenheit - 32) * 5 / 9
    return celsius
farenheit = float(input("Enter temperature in farenheit : "))
print(f"Celsius temperature : {round(farenheit_to_celsius(farenheit), 2)}C --- Farenheit temperature : {farenheit}F")

print("---------------------------------------------------------------------------------------------------")

# Guess the random number between 1 and 9
# q3
import random
random_guess = random.randint(1, 9)  # includes 9
# random_guess = random.randrange(1, 9) # not includes 9
while True:
    guess = int(input("Enter your guess btw 1-9 : "))
    if random_guess == guess:
        print("Well Guessed")
        break
    else:
        print("prompt again")
print("---------------------------------------------------------------------------------------------------")

# Print star pattern
# q4
# using nested loop
x = '*'
for i in range(1, 4):
    for j in range(1, i + 1):
        print(x, end="")
    print()
for i in range(4, 0, -1):
    for j in range(i, 0, -1):
        print(x, end="")
    print()

# using simple loops
"""
x = int(input("Enter no of rows:"))
for i in range(1, x + 1):
    print("*" * i)
for i in range(x - 1, 0, -1):
    print("*" * i)
"""
print("---------------------------------------------------------------------------------------------------")

# Reverse a string
# q5
def rev_word(word):
    return word[::-1]

s = input("Enter string :")
print(f"String : {s}--- Reversed string : {rev_word(s)}")

print("---------------------------------------------------------------------------------------------------")

# Count even and odd numbers in list
# q6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_num = [x for x in numbers if x % 2 == 0]
odd_num = [x for x in numbers if x % 2 != 0]
print("Even numbers : ", even_num, "  no of even_numbers : ", len(even_num))
print("Odd numbers : ", odd_num, "  no of odd_numbers : ", len(odd_num))
print("---------------------------------------------------------------------------------------------------")

# Identify data types in list
# q7
datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for x in datalist:
    print(x, " Type : ", type(x))

print("---------------------------------------------------------------------------------------------------")

# Skip specific numbers in range
# q8
for x in range(0, 7):
    if x == 3 or x == 6:
        continue
    print(x, end=" ")
print("---------------------------------------------------------------------------------------------------")

# Generate Fibonacci series up to 51
# q9
i = 0
j = 1
k = 0
print(i, end=",")
print(j, end=",")
for x in range(0, 51):
    k = i + j
    if k > 51:
        break

    print(k, end=",")
    i = j
    j = k
print("---------------------------------------------------------------------------------------------------")

# Generate multiplication table matrix
# q10
rows = int(input("Enter no of rows : "))
col = int(input("Enter no of columns : "))

matrix = []
for i in range(rows):
    row = []
    for j in range(col):
        row.append(i * j)
    matrix.append(row)
print()
for row in matrix:
    print(row)
print("---------------------------------------------------------------------------------------------------")

# Convert input lines to lowercase
# q11
list = []
print("Press just Enter to exit ")
while True:
    s = input("Enter lines : ")
    if s == "":
        break
    list.append(s.lower())

for data in list:
    print(data)
print("---------------------------------------------------------------------------------------------------")

# Convert binary to decimal and check divisibility by 5
# q12
def bin_to_dec(bin_no):
    if bin_no.isnumeric() and len(bin_no)==4:
        length=len(bin_no)
        power=0
        dec_no=0
        for i in range(length,0,-1):
            if bin_no[i-1]=='0' or bin_no[i-1]=='1':
                dec_no+=int(bin_no[i-1])*(2**power)
                power+=1
            else:
                print("Invalid binary number")
                return -1
        return dec_no  
    
    else:
        print("Invalid binary number")
        return -1
                

print("To seperate one binary number from another  ,enter comma ")
list=[]
str=""
bin_s=input("Enter 4 digit binary number : ")
bin_seq=bin_s+','
for i in bin_seq:
    if i == ',':
        list.append(str)
        str=""
    else:    
        str+=i
    
print("Binary Numbers Divisible by 5 : ")    
for i in range(len(list)):
    dec_no=bin_to_dec(list[i])
    if dec_no%5==0 and dec_no!=-1:
         print(list[i])
    
#easy code built in bin to dec
""" def bin_to_dec(bin_no):
    for i in bin_no:
        if i=='0' or i=='1':
            check=0
    if check==0:        
        return int(bin_no, 2)
    else:
        return False
            
            
    

print("To separate one binary number from another, enter a comma.")
bin_s = input("Enter 4-digit binary numbers separated by commas: ")
bin_str = bin_s.split(',')

print("Binary Numbers Divisible by 5:")    
for bin_no in bin_str:
    if len(bin_no) == 4 and bin_no.isnumeric():
        if bin_to_dec(bin_no) % 5 == 0:
            print(bin_no)
    else:
        print(f"Invalid binary number: {bin_no}") """

print("---------------------------------------------------------------------------------------------------")

# Count letters and digits in string
# q13
s = input("Enter a string: ")
dig_count = 0
letter_count = 0

for i in s:
    if i.isdigit():
        dig_count += 1
    elif i.isalpha():
        letter_count += 1
    else:
        pass

print("Letters:", letter_count)
print("Digits:", dig_count)
print("---------------------------------------------------------------------------------------------------")

# Validate password based on requirements
# q14
print("Password Requirements:")
print("At least 1 letter between [a-z] and 1 letter between [A-Z]")
print("At least 1 number between [0-9]")
print("At least 1 character from [$#@]")
print("Minimum length: 6")
print("Maximum length: 16")

password = input("Enter a password: ")
valid_password = True

if len(password) < 6 or len(password) > 16:
    print("Password length must be between 6 and 16 characters.")
    valid_password = False

if not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter (a-z).")
    valid_password = False

if not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter (A-Z).")
    valid_password = False

if not any(char.isdigit() for char in password):
    print("Password must contain at least one digit (0-9).")
    valid_password = False

if not any(char in ['$', '#', '@'] for char in password):
    print("Password must contain at least one of the following characters: $, #, @.")
    valid_password = False

if valid_password:
    print("Password is valid.")
else:
    print("Password does not meet the requirements.")

print("---------------------------------------------------------------------------------------------------")
