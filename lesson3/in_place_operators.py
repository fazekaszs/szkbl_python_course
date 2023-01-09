# In-place operators can make our codes shorter by removing redundant variable names.
# For example, let's say I want to define a variable, and then add 2 to it:

my_really_long_variable_name_123 = 100
my_really_long_variable_name_123 = my_really_long_variable_name_123 + 2  # redefined as 102
print("My lucky value is:", my_really_long_variable_name_123)

# Using an in-place operator instead, I can save some space and make my code more readable:

my_really_long_variable_name_123 = 100
my_really_long_variable_name_123 += 2
print("My lucky value is (again):", my_really_long_variable_name_123)

# Using the 'a += b' syntax, I can add 'b' to 'a', thus modifying 'a' in-place.
# This way, I don't have to write out the name of 'a' two times, which can be a
# time saver, and also creates shorter code-lines.

# There are other in-place operators, working similarly:

my_value = 5
my_value = my_value + 2  # NOT an in-place op., my_value is now 7
my_value += 2  # equivalent to the previous line, my_value is now 9
my_value -= 2  # my_value is 7 again
my_value *= 3  # my_value is 21
print("The value of my variable is:", my_value)  # still an int
print("The type of my variable is:", type(my_value))

my_value /= 3  # becomes a float, my_value is 7.0
print("The value of my variable is:", my_value)
print("The type of my variable is:", type(my_value))

my_value **= 2  # also works with exponentiation
my_value **= 0.5  # square roots can be taken ALSO through exponentiation

print("My variable now has a value of", my_value, "Not much has changed, huh?")
