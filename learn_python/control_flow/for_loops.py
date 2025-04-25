list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# Under the starting code, write a for loop to print the double of each number in the list 'list_data'.
# 1.	It should loop through the numbers in list_data - each item in the list should be called 'num' (for number)
# 2.	Inside the loop, it should print out the double of each number in the list.

for num in list_data:
    print(num * 2)

# Write another for loop to print the items inside of 'embedded_lists'. Each item in the list should be called 'data'
# It should output this to the screen:
# [1, 2, 3]
# [4, 5, 6]
for data in embedded_lists:
    print(data)

# We need to access the data within the lists, so now we need an embedded loop.
# Create another loop inside of the 'embedded_lists' for loop to list the individual items in the lists.

for data in embedded_lists:
    print(data)
    for inner_data in data:
        print(inner_data)

# Write another for loop to loop through the dictionary 'dict_data'. It should print the keys to the screen.
for data in dict_data:
    print(data)

# Write another for loop to loop through the dictionary 'dict_data'.
# Use to the dictionary's value() method to print the value for each key in the dictionary.

for data in dict_data.values():
    print(data)
# Generate an embedded for loop (a loop within a loop) to extract and print the values within the dictionary of each item in the dictionary.
for outer_item in dict_data.values():
    for inner_item in outer_item.values():
        print(inner_item)

# Write another for loop to loop through the dictionary 'dict_data' but this time only print out the money values
for outer_item in dict_data.values():
    for inner_item in outer_item.values():
        if inner_item.startswith("$"):
            print(inner_item)

# Write another loop to loop through the items in 'list_data' and include a nested (indented) if statement inside the loop so that when it loops it checks the number/item in list:
# •	if the number is less than 3, it prints 'less than 3'
# •	if the number equals 3, it prints 'I found three'
# •	if the number is greater than 3, it prints 'greater than 3'

for num in list_data:
    if num < 3:
        print("less than 3")
    if num == 3:
        print("I found three")
    if num > 3:
        print("greater than 3")