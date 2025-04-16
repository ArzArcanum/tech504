# 1. What is a variable?
# A variable is a mutable, stored value, it can be read and written to.
myFirstVariable = "hello"
mySecondVariable = 42

# 2. Why is it called a variable?
# Because it is mutable. The value it holds can vary.
exampleVariable = "first value"
exampleVariable = "new value"

# 3a. Set/assign a variable [number, decimal, string]
myNum = 1
myDecimal = 2.4
myString = "hello"

#3b What does '==' mean?
# '==' means "is equal to", while '=' assigns a new value.
string1 = "abc"
if string1 == "abc": print("True")

# 4. Print the values and data types of the variables above.
print(myNum)
print(type(myNum))
print(myDecimal)
print(type(myDecimal))
print(myString)
print(type(myString))

# 5a. What is a strongly typed language? Compare to a weakly typed language. Include a code example
#
# A strongly typed language enforces strict rules about how variables and values of different types interact.
# If an operation is not explicitly defined for a certain type combination, the language will not attempt to "fix" it automatically.
# (Like weakly typed languages do)
## JS:
## let num = 2;
## let str = "5";
## let result = num * str; // JS automatically converts the string "5" to a number
## console.log(result); // Output: 10
#
## Python
## num = 2
## str = "5"
## result = num + str
## print(result)
## Runtime Error

# 5b. What is a dynamically typed language? Compare to a statically typed language.
#     Include a code example
#
# A statically typed language checks variable types at compile time,
# meaning type-related errors are caught before the program runs.
## Java
## int number = "10";
## Compile-time error
#
# A dynamically typed language checks types at runtime,
# meaning variables can change types freely, and errors related to types appear only when the program runs.
## Python - Dynamically typed
## num = 2
## str = "5"
## result = num + str
## print(result)
## Runtime Error
#
# 6. Overwrite the value of one of your variables which stores a number
# 6a. Check the id() of the variable before and after you overwrite the variable with a new number
q6num = 10
print(id(q6num))
q6num = 3
print(id(q6num))
# 6b. Why does the id change?
# id() returns the memory address of a variable.
# As integers are immutable, a new object, with a new memory address must be created to represent the new value.
# The variable now references the new value's memory address.

# 7. Assign one variable to another
# 7a. Start with this code:
x = 10
y = x
# check the id of x and y
print(id(x))
print(id(y))
# Explain why x and y are the same.
# Answer: y has the same id as x because y is now refer to the same object in memory as x.
# Q: What happens if after assigning x = y, I give x a different value? Does the id of y change also?
x = 15
print(y)
# A: No, we have changed the value x points too, but not the value itself.
# 8. Ask the user for some input.
# name = input("What is your name? ")
# age = input("What is your age? ")
# DOB = input("What is your date of birth? ")
# print("Hello " + name + ", you are " + str(age) + " years old, born on " + str(DOB))

## Topic Data types and operators
# 1. What is the difference between operators and operands?
# A.    Operators refers to an action or process that manipulates data to perform a specific task.
#       Operands are the values or variables that the operators act upon during an operation.
x = 5
y = 1
# 2. Demonstrate that you understand how to use operators to:
# Add
z = x + y
# Subtract
z = x - y
# Multiply
z = x * y
# Divide
z = x / y
# Find the remainder part of the division
z = x % y
# 3. Add code to demonstrate that you understand how to use comparison operators to:
# Greater than
if x > y: print("true")
# Less than
if x < y: print("true")
# Check if equal
if x == y: print("true")
# Check if not equal
if x != y: print("true")
# Greater than or equal to
if x >= y: print("true")
# Less than or equal to
if x <= y: print("true")

### Topic Creating strings and using quotes appropriately
## Starting code
##bad_string = 'I said 'wow!''
##print(bad_string)

# 1.    Why does this fail?
# A.    The second use of single quotes inside the string causes a parsing error that escapes the 'wow!' string.
# 2.    Find three ways to make this string work.
#       Condition: The Wow! must be surrounded in quotes when it prints to the screen.
# Solution 1.
my_string = "I said 'wow!'"
print(my_string)
# Solution 2.
my_string = 'I said \'wow!\''
print(my_string)
# Solution 3
my_string = "I said " + "'" + "wow!" + "'"
print(my_string)

# 3.    Opinion: What is best practice when deciding what quotes to use around strings in Python?
# A.    While this is mostly up to personal preference, the most important thing is to be consistent in which ones you use.

### Topic Slice strings
# 1.    What is slicing strings
# A.    Slicing a string is to extract a section of a string.

Hw = "Hello world!"
print(Hw)

#       Find out how many characters Hw has
count = len(Hw)

#       Get the character in the first position in Hw
firstChar = Hw[0]
#      Get the last character
lastChar = Hw[-1]
#      Get the 2nd last character
secondLastChar = Hw[-2]
#       Write a comment to EXPLAIN what these examples do:
print(Hw[2:])
# Take the string Hw and slice it from index 2 to the end.
# Output: 'llo world!'
print(Hw[-3:])
# Take the string Hw and slice if from the 3rd last index to the end.
# Output: 'ld!'
print(Hw[:5])
# Take the string and slice it from the beginning to the 5th index.
# Output: 'Hello'
print(Hw[2:5])
# Starts at the second, stops at the fifth.
# Output: 'llo'






