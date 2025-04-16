# Task: Working with dictionaries

# 1.	Make a dictionary called "student_1" containing the following information:
# a.	name: susan
# b.	stream: tech
# c.	completed_lessons: 4 (should be saved as an integer not a string)
# d.	completed_lesson_names: value should be list of these 3 items: "variables", "data_types", "set up"
student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set up"]
}

# 2.	Explain how a dictionary saves/structures data? Example, what does each value need to be accompanied/associated with?
#   Each entry is stored as a key/value pair. The key is an identifier for the value. Keys must be unique and immutable.

# 3.	Print the dictionary to the screen
print(student_1)
# 4.	Print it's data type to the screen to check it's a dictionary
print(type(student_1))
# 5.	Print the value for the key-value pair having the key "stream"
print(student_1["stream"])
# 6.	Print the value for 'completed_lesson_names' - check you can see the list of 3 items
print(student_1["completed_lesson_names"])
# 7.	Print the data type for the value for 'completed_lesson_names' - check it is a list
print(type(student_1["completed_lesson_names"]))
# 8.	Print the first element/item in the list of 'completed_lesson_names' (should output "variables")
print(student_1["completed_lesson_names"][0])
# 9.	Change the value of "completed_lessons" to 3 (an integer not string). Make sure you change was successful by printing your dictionary to the screen again.
student_1["completed_lessons"] = 3
print(student_1)
# 10.	Delete "data_types" from the list under the key 'completed_lesson_names'
student_1["completed_lesson_names"].remove("data_types")
# 11.	Use the keys() method on your dictionary to list all the keys
print(student_1.keys())
