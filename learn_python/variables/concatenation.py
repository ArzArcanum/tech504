# What is concatenation?
# Concatenation is the act of joining strings together.
string1 = "Concate"
string2 = "nation"
string3 = string1 + string2
print(string3)

x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"

# print(x + y + z)

# This should not work
# Make it work:
#   Make the print statement work using concatenation (+) to join x, y and z so that it prints this to the screen: `25.4 there's now a number 25.4 unless we put a space in!"
#   Explain: The problem and the solution
print(str(x) + str(y) + z)
#   The problem was due to the fact that x and y were numbers, adding numbers adds their values.
#   Casting them to a string causes the + operator to concatenate the strings.

