result_str = "5.67"

# The "float" function can convert other types into float typed values.
# When applied to a string, it converts the string into a float:
result_float = float(result_str)

# The "int" function does the same, just creates an int typed value.
# Applying the "int" function on a float value rounds the value down to
# the closest smaller integer.
result_int = int(float(result_str))
print("First float, then int:", result_int)

# To round a float in a "traditional" way use the "round" function.
# You can also use "round" to round to a certain number of decimal digits.
print("Rounding:", round(5.67))
print("Rounding (1 decimal value):", round(5.67, 1))
print("Rounding (5 decimal values):", round(1 / 7, 5))

# The "len" function, when applied to a string typed value, returns the length
# of a string measured in the number of characters.
print("Length of a string:", len(result_str))

# The "type" function returns the type of the value.
print("Type of the Hello text:", type("Hello"))
print("Type of the result_float variable:", type(result_float))
print("Type of the result_int variable:", type(result_int))

# The "str" function returns the string representation of a variable.
print("str on an int: " + str(5))
print("str on a float: " + str(3.1415))
print("str on a None value: " + str(None))
