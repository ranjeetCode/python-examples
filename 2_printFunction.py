# print() function prints the message to the screen or any other standard output device.
# You can pass variables, strings, numbers, or other data types as one or more parameters when using the print().
# Then, these parameters are represented as strings by their respective str() functions.
# To create a single output string, the transformed strings are concatenated with spaces between them.
# Example 1:
print("Example 1:")
name = "Ranjeet kumar"
age = 35
print("Name:", name)
print("Age:", age)

# Example 2:
print("Example 2:")
name = "Manjeet kumar"
age = 30
print("Hello, my name is", name, "and i am", age, "years old")

#########***** Python String Literals *****###########
# String literals in Python’s print statement are primarily used to format or design how a specific string appears when printed using the print() function.
    # \n: This string literal is used to add a new blank line while printing a statement.
    # “”: An empty quote (“”) is used to print an empty line.

# Example 3:
print("Example 3:")
print("This is an example of string literals \n in python")

######**** Python “end” parameter in print() *******#########
# The end keyword is used to specify the content that is to be printed at the end of the execution of the print() function.
# By default, it is set to “\n”, which leads to the change of line after the execution of print() statement.

# Example 4:
print("Example 4:")
# This line will automatically add a new line before the next print statement
print("This line will automatically add a new line before the next print statement")

# This print() function ends with ** as set in the end argument.
print("This print() function ends with ** as set in the end argument", end="**")
print("Python print() function")

#########***** Print Concatenated Strings *****##########
# In this example, we are concatenating strings inside print() function in Python.
# Example 5:
print("Example 5:")
print("Example for " + "Concatenation")
