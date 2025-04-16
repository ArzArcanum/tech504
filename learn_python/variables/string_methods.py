### Topic: String Methods
# 1. Starting code
str_with_extra_spaces = "   extra spaces at the start and end   "

# Print the count of characters in the string (including spaces)
print (len(str_with_extra_spaces))

# print the string after stripping the white space off each end.
print(str_with_extra_spaces.strip())

# 2. Next use this starting code for the next set of subtasks.
example_text = "here's some text with some words of text"

# count how many times the substring 'text' occurs within example_text & print it to the screen
textOccurs = example_text.count("text")
print(textOccurs)

# convert example_text to lowercase & print it to the screen
example_text_lower = example_text.lower()
print(example_text_lower)

# convert example_text to uppercase & print it to the screen
example_text_upper = example_text.upper()
print(example_text_upper)

# capitalise the first letter in example_text & print it to the screen
example_text_capitalized = example_text.capitalize()
print(example_text_capitalized)

# replace the word 'with' in example_text with a comma (,) instead & print it to the screen
example_text_replaced = example_text.replace("with", ",")
print(example_text_replaced)