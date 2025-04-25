# 1.	Create a new file named 'while_loops.py' or similar.
# 2.	Initialise x with the value of 0
# 3.	Create a while statement so that it loops while x is less than 10. Everytime it loops it should:
#       a.	    Print the value of x to the screen in an f-string
#       b.	    Increment (add 1 to x)

x = 0
while x < 10:
    print(f"x -> " + str(x))
    # without incrementing x, the loop will iterate forever
    x += 1

# Modify the second copy of the 'while loop' so that it breaks out of the loop when x equals 4.
x = 0
while x != 4:
    print(f"x -> " + str(x))
    # without incrementing x, the loop will iterate forever
    x += 1