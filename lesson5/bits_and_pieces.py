# With the 'del' keyword, we can un-assign the variable name and
# make it undefined. After deleting a variable, we cannot use it,
# unless we declare it again.
my_var = 10
print(my_var)
del my_var

# If we uncomment the following line, the script will raise an error:
# print(my_var)
# This is because my_var became undefined after the deletion, and printing
# (or generally using) an undefined value will stop the script with an error.

# We can declare multiple variables in one line using the following syntax:
my_var1, my_var2 = 5, "Hello"
print("my_var1 is: ", my_var1, ", my_var2 is: ", my_var2, sep="")

# This way the value 5 is bound to the variable my_var1, and the value "Hello"
# is bound to my_var2. We can also declare three or any number of variables this
# way.

# Sometimes it is crucial to cut down on the runtime of scripts. Although right now
# it seems that these programs run almost instantaneously, longer and more complicated
# scripts can run for longer times.

# For example, if we need the integer division between 12 and 7, and also the remainder
# of this division, we can calculate these separately:
integer_div_result = 12 // 7
modular_div_result = 12 % 7
print("12 divided by 7 is", integer_div_result, "with a remainder of", modular_div_result)

# However note, that we calculate the division two times to obtain the two results! This should
# be unnecessary, since the two results can be calculated in one round, saving us a little computation
# time. For this, we have a function called 'divmod'. This function has two return values, and we can
# capture each one using the 'multiple variable declaration' syntax seen above.
integer_div_result, modular_div_result = divmod(12, 7)
print("12 divided by 7 is", integer_div_result, "with a remainder of", modular_div_result)

# This will give us the same result, but through only one division round (and is, thus, faster).
