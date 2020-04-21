# Anything after hash (#) symbol is a comment (single line comment)
"""
Anything between 3 quotes (single or double) is a multi line comment
"""

# Simply print a string using print() built-in function (came pre-coded with standard python installation)
print( "Hello Ajanthan, Welcome to the world of Python Programming")

# Let us declare some variables here
name = 'Ajanthan'
language = 'Python'

# Print the string with formatting options - 1 (string concatenation with the declared variables)
print("Hello "+ name + ", Welcome to the world of " + language + " Programming")

# Print the string with formatting options - 2 (format method - Positional arguments)
print("Hello {}, Welcome to the world of {} Programming".format(name, language))

# Print the string with formatting options - 3 (format method - Named arguments)
print("Hello {username}, Welcome to the world of {lang} Programming".format(lang=language, username=name))