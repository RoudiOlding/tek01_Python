## 1. VARIABLES

x = 10 # integer
y = 10.5 # float
z = "Hello" # string
a = True # boolean

x1 = int(10)
y1 = float(10.5)
z1 = str("Hello")
a1 = bool(True)

print(type(x), type(y), type(z), type(a))

b1 = 10
B1 = 20
print(b1, B1)

## 2. STRINGS
print("Welcome to Meibzial!")
book = 'Meibzial'
print(book)

paragraph = """This is a paragraph.
It has multiple lines.
It is enclosed in triple quotes."""
print(paragraph)

# String positions
name = "Meibzial"
print('\n' + name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7] + "\n")

# String Concatenation
name = "Meibzial"
age = 25
print("My name is " + name + " and I am " + str(age) + " years old.")

# String lenght
name = "Meibzial"
print(len(name))

# String check
name = "Meibzial"
print("Mei" in name)
print("mei" in name)
print("Mei" not in name)
print("mei" not in name)

# String slicing
name = "Meibzial"
print(name[0:3])
print(name[:3])
print(name[3:])
print(name[:])
print(name[-1])
print(name[-2])

# String methods
phrase = "Welcome to Meibzial"
print(phrase.lower()) # lower
print(phrase.upper()) # mayus
print(phrase.strip()) # remove white spaces
print(phrase.replace("Welcome", "Hello")) # replace
print(phrase.split(" ")) # split with condition

## 3. BOOLEANS
print(10 > 9)
print(10 == 9)
print(10 < 9)

## 4. OPERATORS
# Arithmetic operators
x = 10
y = 5
print(x + y)
print(x - y)

# Assignment operators
x = 10
x += 5
print(x)

# Comparison operators
x = 10
y = 5
print(x == y)
print(x != y)

# Logical operators
x = 10
print(x > 5 and x < 15)
print(x > 5 or x < 15)
print(not(x > 5 and x < 15))

# Identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

# Membership operators
x = ["apple", "banana"]
print("banana" in x)
print("pineapple" not in x)

## 5. LISTS
# List
fruits = ["apple", "banana", "cherry"]
print(fruits)

# List lenght
print(len(fruits))

# List items
print(fruits[0])
print(fruits[1])

# Check if item exists
print("apple" in fruits)
print("orange" in fruits)

# Sort list
fruits.sort()
print(fruits)

# Manipulate list
fruits.append("orange")
print(fruits)
fruits.insert(1, "lemon") # push to position
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.pop() # default, the last one
print(fruits)
del fruits[0] # delete in position 0
print(fruits)
fruits.clear() # delete all
print(fruits)

vegetables = ["carrot", "potato", "onion"]
fruits = ["apple", "banana", "cherry"]
food = fruits + vegetables
print(food)
burgers = ["cheeseburger", "hamburger"]
burgers.extend(fruits)
print(burgers)

## 6. DICTIONARIES
# Dictionary
person = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "travelling"]
}
print(person)

# Dictionary items
print(person["name"])
print(person["hobbies"])
print(len(person)) # number of items

di1_keys = person.keys()
print(di1_keys)
di1_values = person.values()
print(di1_values)
di1_items = person.items()
print(di1_items)

person['name'] = 'Jane'
person['city'] = 'Los Angeles'
person['mail'] = 'mail™@gmail.com'
print(person)

## 7. IF ELSE
a = 33
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# pass statement
a = 33
b = 200
if b > a:
    pass

# break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

## 8. LOOPS
# for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

# range() function
for x in range(6): # range 0 to 5
    print(x)

# else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# while loop
i = 1
while i < 6:
    print(i)
    i += 1

## 9. FUNCTIONS
def my_function(fname):
    print(f"Welcome {fname}, let's go to another day learning Python!")

my_function("Sae")

def fun_identificacion(fname, flast, fage):
    print(f"Hello {fname} {flast}." + "\n" + f"It's looks like you are {fage} years old.")

fun_identificacion("Sae", "Olding", 15)

def show_shopList(items):
    for index, item in enumerate(items): # enumerate() function, create an index
        print(f"{index + 1}. {item}")

items = ['Airpods', 'Bottle', 'Brush', 'Lamp']
show_shopList(items)

def add_function(x, y):
    return x + y

print(add_function(x=5, y=3))

def first_recurstion(x):
    if x > 0:
        result = x + first_recurstion(x - 1)
        print(result)
    else:
        result = 0
    return result

print("\nRecursion Example Results")
first_recurstion(6)

## 10. LAMBA
tripleAdd = lambda x, y, z: x + y + z
print("\n" + f"The result is {tripleAdd(5, 6, 2)}")

## 11. CLASSES

class Simple:
    x = 8

s1 = Simple()
print(s1.x)

class Person:
    def __init__(self, name, age): # __init__ function, constructor
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def scream(self):
        print("AAAA")

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
p1.age = 30
print(p1)
p1.scream()

## 12. TYPE CASTING
var1int = 100 # int
var2float = 25.5 # float
floatVar = var1int + var2float # float
print(floatVar)
print(type(floatVar))   # float

"Here's go an explicit type casting"
num_string = "100"
num_int = 25

print(f'Data type of the num_string before the cast: {type(num_string)}')   # str
num_string = int(num_string) # casting

print(f'Data type of the num_string after the cast: {type(num_string)}')   # int

num_sum = num_string + num_int
print(num_sum)
print(type(num_sum))   # int

## 13. Exceptions

try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(result)

except:
    print("Error: Denominator can be 0")

# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(result)

except:
    print("Error: Denominator can be 0")

finally:
    print("Finally block is executed")

## 14. TUPLES
# Tuple
fruits = ("apple", "banana", "cherry") # immutable // only strings
generalTuple = (1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e') # mixed data types
print(fruits)
print(generalTuple)

# Access Tuple
print(fruits[0])
print(fruits[1:3])

## 15. SETS
# Set
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Access Set
for x in fruits:
    print(x)

# Add Set
fruits.add("orange")
print(fruits)

# Remove Set
fruits.remove("banana")
print(fruits)

# Clear Set
fruits.clear()
print(fruits)

# Union Set
fruits = {"apple", "banana", "cherry"}
vegetables = {"carrot", "potato", "onion"}
food = fruits.union(vegetables)
print(food)

# Intersection Set
food2 = fruits.intersection(vegetables)
print(food)