# 🎯 Outcome (By doing this you should): Practice using separate functions to do each of the different operations of a mini calculator
# Recommended: Make a 'functions' folder inside your PyCharm project for storing learning about functions.
# Create a Python file called calculator.py and complete a viable basic calculator using functions.
# MVP (each of these should be in a separate function):
# •	Can add 2 numbers
# •	Can subtract 2 numbers
# •	Can multiply 2 numbers
# •	Can divide 2 numbers
#
# Taking it to the next level:
# •	Implement more complex operations, such as handling parentheses, exponentiation
# •	More advanced operations should continue to be broken into separate functions

import re

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}

def compute(expression):
    match = re.split(r'([+\-*/])', expression, maxsplit=1)
    if len(match) == 3:
        left, operator, right = match
        result = operations.get(operator)(int(left), int(right))
        if result:
            print(result)
            return result
        else: print("Invalid operator")
    else:
        print("Invalid input")

def evaluate_parentheses(expression):
    match = re.findall(r'\([^()]*\)', expression) # Find all pairs of parentheses
    if len(match) > 0:
        for i in match:
            resolved_parentheses = str(compute(i[1:-1]))
            if resolved_parentheses:
                expression = expression.replace(i, resolved_parentheses)
        compute(expression)
    else:
        compute(expression)

# user_input = input("Enter your equation: ")
evaluate_parentheses("(2 * 8 ) / (4 - 1)")