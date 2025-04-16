# •	How are tuples similar to lists?
# Tuples are similar to lists in that they:
#   Are ordered
#   Are indexed
#   Can contain any data type
#   Can be nested
#   Can be looped over

# •	Are tuples immutable and what does this mean?
# Yes, tuples are immutable, unlike lists. This means you cannot change tuples after they are created.

# •	What other data types are immutable?
# int, float, bool, str, tuple, frozenset, bytes, NoneType

# •	What are good use cases for tuples instead of lists?
# Tuples are good for when the contents of the collection should be changeable.

# •	What does the following piece of code do?
essentials = ("bread", "eggs", "milk")

print(essentials)
print(essentials.count("bread"))
# This code creates a tuple containing three strings, prints the tuple, then prints the number of items in the tuple with a value of "bread".

# The task
# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code
print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")
# save the items as a tuple
essentials_tuple = essential_item1, essential_item2, essential_item3
# print the tuple
print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")
# try to add the 4th item to the tuple
# if you can't add the 4th item, work out how to save the 4th item to the tuple
essentials_tuple += (essential_item4,)

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)

