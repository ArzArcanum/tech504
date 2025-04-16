## Topic: List basics

# 1.	Create a list called 'shopping_list' with the following items:
# a.	eggs
# b.	bread
# c.	bananas
# d.	biscuits
# e.	milk
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

# 2.	Print the list to the screen
print (shopping_list)
# 3.	Print the data type of 'shopping_list'
print(type(shopping_list))

# 4.	Print the first item in the list
print(shopping_list[0])

# 5.	Print the last item in the list
print(shopping_list[-1])

# 6.	Change the second item in the list (i.e. 'bread') to 'rice' instead, then print the second item to the screen to prove it's been changed
shopping_list[1] = "rice"
print(shopping_list[1])

# 7.	Use the list's method to add the item 'carrots' to the list (you should not re-assign the list using '='), then check the length of the list (which should now have 6 rather than 5)
shopping_list.append("carrots")
print(len(shopping_list))

# 8.	Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list. Use one of the list's methods to add the two items in one go.
extra_list = ["toffee", "coffee"]
shopping_list.extend(extra_list)

# a.	Print the 'shopping_list' to check 'toffee' and 'coffee' have been added correctly.
print(shopping_list)

# 9.	Remove "bananas" from 'shopping_list'. Print 'shopping_list' to check it's been removed.
shopping_list.remove("bananas")
print(shopping_list)

# 10.	Remove the last item ('coffee') from 'shopping_list' using the pop method. Check it worked by printing 'shopping_list'
shopping_list.pop()
print(shopping_list)

## Task: Mix all the data about a user into a list

# 1.	Use your code from the "Task: Python variable basics" (last subtask) where you asked the user for their name, age and DOB.
from datetime import datetime
str_name = input("What is your name? ")
int_age = int(input("How old are you? "))
string_DOB = input("What is your date of birth? (DD-MM-YYYY)")
date_DOB =  datetime.strptime(string_DOB, "%d-%m-%Y").date()

# 2.	Mix the name, age and DOB into one list user_details_list
user_details = [str_name, int_age, date_DOB]

# 3.	Print the user's name, age and DOB from the list
print(user_details)
# 4.	Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
if type(int_age) == int: print("int_age is stored as an int")

# 5.	Ask the user for their height in cm and save it to the variable height
float_height_cm = float(input("What is your height in cm?"))

# 6.	Save height as a float in the list, and print the height from the list.
user_details.append(float_height_cm)
print(user_details[-1])

## Task: Test you can slice lists

mixture = [1, 2, 3,"one", "two", "three"]

print(mixture)

# Print these list slices to the screen:
# •	Returns the 2nd and 3rd items in the list -> It should return [2, 3]
print(mixture[1:3])

# •	Returns every second item in the list -> It should return [1, 3, 'two']
print(mixture[::2])
# •	Start at the last item, stop at the 3rd last item, and step in reverse order -> It should return ['three', 'two']
print(mixture[-1:-3:-1])