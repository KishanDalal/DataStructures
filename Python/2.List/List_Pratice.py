# Practice Task: Working with Python Lists

# 1. Create a Python list named 'my_info' that stores the following information about you
#    (as strings or appropriate data types):
#    - your name
#    - your favorite color
#    - the number of siblings you have
#    - a list of your favorite hobbies.
#    Example: my_info = ["Alice", "blue", 2, ["reading", "hiking"]]

my_info = ["Kis", "orange", 1, ["gyming", "reading", "coding"]]

# 2. Print the entire 'my_info' list.

print(my_info)

# 3. Print just your favorite color from the list.
#    Hint: Remember how to access elements by index.

print(my_info[1])

# 4. Change the number of siblings in your list to be one more than it currently is.
#    Hint: You'll need to access the element by index and then update its value.

my_info[2] = 2

# 5. Add another hobby to your list of hobbies within 'my_info'.
#    Hint: You'll need to access the list of hobbies (which is an element within 'my_info')
#    and then use a list method to add the new hobby.

my_info[3].append("eating")


# 6. Print the updated 'my_info' list.

print(my_info)