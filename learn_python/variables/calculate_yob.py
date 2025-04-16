# Write a Python script to calculate the user's year of birth
# First part
# •	define the variables age_int and name_str (set dummy/default/initial values)
# •	make a calculation for the year in which the person was born
# •	print out "OMG , you are years old so you were born in " with the correct values
#
# Second Part
# •	prompt the user for inputs and assign the variable age_int and name_str
# •	remove the initial values set
#
# Third Part
# •	calculate and print out the total number of hours this person has lived

from datetime import datetime
current_year = datetime.now().year
name_str = input("What is your name? ")
age_int = int(input("What is your age? "))
approx_yob = current_year - age_int
print(f"OMG , you are {age_int} years old so you were born in {approx_yob}")
approx_hours_lived = age_int * 8760
print(f"You are approximately {approx_hours_lived} hours old.")
