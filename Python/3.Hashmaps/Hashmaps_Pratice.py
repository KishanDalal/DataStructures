# Learning Python Dictionaries (Hash Maps)

# Task 1: Creating a Dictionary
# Create a dictionary called 'student' to store the following information:
# - name: "John Doe"
# - age: 20
# - major: "Computer Science"
# - grades: [85, 92, 78]
# Print the 'student' dictionary.
student = {} # Start with an empty dictionary
# Add the key-value pairs here
student = {"name" : "John Doe", "Age" : "20", "major" : "Computer Science", "Grades" : [85, 92, 78]}
print("Student Dictionary:", student)

# Task 2: Accessing Values
# Using the 'student' dictionary you created:
# - Print the student's name.
# - Print the student's major using the .get() method. What happens if you try to access a key that doesn't exist using .get()?
# - Try to access a key that doesn't exist using the square bracket notation (e.g., student["city"]). What happens?
# Accessing name: 
print("Student name: ", student["name"])
# Accessing major using .get():
print("Student Major: ", student.get("major"))
# Trying to access a non-existent key with []:
#print("Student City ", student["city"])

# Task 3: Adding and Modifying Key-Value Pairs
# - Add a new key-value pair to the 'student' dictionary: "city": "New York".
# - Change the student's age to 21.
# - Add a new grade of 95 to the 'grades' list within the 'student' dictionary.

# Adding "city":
student["city"] = "Toronto"
# Changing age:
student["Age"] = 34
# Adding a grade:
student["Grades"].append(22)

print("Updated Student Dictionary:", student)

# Task 4: Checking for Keys
# - Check if the key "major" exists in the 'student' dictionary and print the result (True or False).
# - Check if the key "country" exists in the 'student' dictionary and print the result.

# Checking for "major": 
print("major" in student)
# Checking for "country":
print("country" in student)

# Task 5: Exploring Keys, Values, and Items
# - Print all the keys in the 'student' dictionary.
# - Print all the values in the 'student' dictionary.
# - Print all the key-value pairs (items) in the 'student' dictionary.

# Printing keys:
print(student.keys())
# Printing values:
print(student.values())
# Printing items:
print(student.items())