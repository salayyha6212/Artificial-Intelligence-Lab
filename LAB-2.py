#LAB 2
#Saliha Batool
#BCS21042

#WHILE LOOP
print("-----WHILE LOOPS------")

count=0
while ( count < 3):
    count = count + 1
    print("Hello world! ")

print("----SINGLE STATEMENT WHILE BLOCK-----")
count=0
while(count!=0):print("Hello World!")

#For loops in lists
print("----FOR LOOPS----")
list = ['geeks', 'for', 'geeks']
for i in list:
    print(i)

#for loops in tuples
tuple=('geeks', 'for', 'geeks')
for i in tuple:
    print(i)
    
#for loop for strings
print("---ITERATING OVER A STRING---")
string = "geeks"
for i in string:
    print(i)
    
#Iterating by index
print("---ITERATING BY INDEX----")
list = ['geeks', 'for', 'geeks']
for i in range(len(list)):
    print(i)
   
#Loop Control
print("---LOOP CONTROL----")
s="geeksforgeeks"
for letter in s:
    if letter=='e' or letter=='s':
        continue
    print ('current letter: ', letter)

#Functions
print("---FUNCTIONS---")
def my_function():
    print("Hello from a function")
    
my_function()

#Function with parameters
print("\nFunctions with parameters\n")
def my_function(fname):
    print(fname + " was the parameter that you passed to the function")

my_function("Linux")
#default parameter value
print("\nFunctions with default parameter value\n")
def my_function(country="Norway"):
    print("I am from :", country)

my_function("sweden")
my_function()

#passing a list as a parameter
print("\nFunctions with list as a parameter\n")
def my_function(food):
    for x in food:
        print(x)

fruits = ['apple', 'banana', 'oranges', 'mangoes']
my_function(fruits)

#function with return values
print("\nFunctions with return values\n")
def my_function(x):
    return 5*x
    
print(my_function(3))

#functions with keyword arguments
print("\nFunctions with keyword arguments\n")
def my_function(child1, child2, child3):
    print("The youngest child is:", child3)
    
my_function (child1= "Emil",child2="Tobia", child3 = "Linus")

#classes and objects
print("\n --CLASSES AND OBJECTS---")
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

#nit function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)