#LAB 1
#Saliha Batool
#BCS21042

#Execute Python Syntax
print ("Hello World")

#Comments in Python
# Hash is used for single line comments
""" Double quotations is used for 
multi line comments """

#Input/Output
txt = input("Type something to test this out: ")
print(txt)

#Multiple Statements on a Single line
print("Statement1")
print("Statement2")
print("Statement1"); print("Statement2")

#Indentation
x = 1
if x > 0:
    print("This Statement has a single tab indentation")

#Reserve Words in Python (ifelse)
number = int(input("Enter your numbers: "))
if number >= 90:
    print("Your grade is A+")
elif number >= 80 and number < 90:
    print("Your grade is B")
elif number >= 70 and number < 80:
    print("Your grade is C")
elif number >= 60 and number < 70:
    print("Your grade is D")
elif number >= 50 and number < 60:
    print("Your grade is E")    
else:
    print("You are fail")

#Variables Type
a = 123                                #integer
b = 1.1                                #float
c = complex(1, 2)                      #complex
d = True                               #boolean
e = "String"                           #string
f = e[0:2]                             #substring
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

#Special Characters in String
special_chars_string = "This is a string with special characters:\n"
special_chars_string += "Backslash: \\\n"
special_chars_string += "Single quote: \'\n"
special_chars_string += "Double quote: \"\n"
special_chars_string += "Tab: \tTabbed text\n"
special_chars_string += "Newline: \nNew line text"
print(special_chars_string)


#Indices in Strings
string = "Hello World"
print(string)
print(string[0])
print(string[2])
print(string[-1])
print(string[-7])

#Lists
integers = [10, 20, 30]               
floats = [1.1, 2.2, 3.3]                     
strings = ['RED', 'GREEN', 'BLUE']              
mixed = [50, 6.6, 'BLACK']                 
print(integers)
print(floats)
print(strings)
print(mixed)

#Slicing in Lists
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original list:", my_list)
print("Positive index slice (2:5):", my_list[2:5])
print("Negative index slice (-7:-4):", my_list[-7:-4])

#Conditional Statements
number = 5
if number == 10:
    print("The number is equal to 10.")
elif number != 10:
    print("The number is not equal to 10.")