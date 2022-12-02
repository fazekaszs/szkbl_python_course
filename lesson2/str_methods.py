my_var = "Hello"

# A method is a function bound to a certain variable type.
# Methods are either called on literals or on variables.

# The "lower" method lowers all the characters in a string.
print("All characters in lower case (lower on a variable):", my_var.lower())
print("All characters in lower case (lower on a literal):", "HeHe LOL".lower())

# As it can be seen, it has a string type return value.
my_var_lower = my_var.lower()

# There is also an "upper" method, which is the opposite of "lower".
print(my_var.upper())

# It is important not to forget to use the ( and ) characters at the end
# of function and method calls. If we forget to use it, we won't store the
# return value of the function/method in a variable, but rather we will store
# the function/method itself!
upper_function = my_var.upper
print("The type of upper_function is:", type(upper_function))

# The "strip" method deletes spaces, enters, and tabs at the beginning
# and at the end of the string it's called on. It won't "hurt" spaces/enters/tabs
# that are between other characters.
print(" a lot of things  ".strip())  # equivalent to print("a lot of things")

# To replace characters and substrings within a string, use the "replace" method.
# This method takes two arguments, first the substring to be replaced, and then
# the replacing string.
print("Árvíztűrő tükörfúrógép".replace("é", "e"))  # replace one character
print("Árvíztűrő tükörfúrógép".replace("fúró", "túró"))  # replace multiple characters

# We can chain methods one after another, since they can also have a return type.
# For example "replace" returns with a string on which we can call "replace" again.
my_var2 = "Tiny car: the tank is full"
print(my_var2.replace(":", "-").replace("car", "miny"))

# The "capitalize" method makes the first character of the string a capital character.
my_var3 = "smAll Car. the tank is full. but until when? sure! haha"
print(my_var3.capitalize())

# The methods "ljust", "rjust", and "center" justify strings to the left, right, or center.
# It uses spaces for this by default, but we can also specify our filling character (preferably
# different, than a space). The first argument is an integer, that specifies the length of the
# justification.
my_var4 = "OlIvEs"
print(my_var4.ljust(40))  # will print "OlIvEs                                  "
print(my_var4.rjust(40))  # will print "                                  OlIvEs"
print(my_var4.center(40))  # will print "                 OlIvEs                 "
print(my_var4.center(40, "~"))  # will print "~~~~~~~~~~~~~~~~~OlIvEs~~~~~~~~~~~~~~~~~"

# Until this point we've only met string methods that also return string values.
# The "count" method on a string returns an integer, that is the number of occurrences
# of a substring within the string it's called on.
print("Number of e characters within my_var3:", my_var3.count("e"))  # will print out 3

# The "isupper" method returns a boolean value (either True or False), representing whether
# all characters within the string are uppercase characters.
print("Are all characters in my_var3 uppercase characters? -", my_var3.isupper())
print("What about now? -", my_var3.upper().isupper())

# This code part wouldn't run:
# print(my_var3.isupper().upper())
# If you uncomment it, the program will run with an error.
# This is because "isupper" returns a boolean, on which the "upper" method does not
# exist! The "upper" method is bound to strings, NOT booleans!

# There is also an "islower" method, which is the opposite of the "isupper" method.
print(my_var3.upper().islower())
print(my_var3.lower().islower())
