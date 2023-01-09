# To add a newline character ("enter") into our string variable we cannot
# just press enter. PyCharm will break the line IN THE CODE, but NOT in the
# string itself. Also, it will add a \ character at the place where we pressed
# enter.
not_two_lines = "This is the first line. " \
                "This is ALSO in the first line!"
print("Are these two lines?", not_two_lines)

# To really add a newline into our string we have to ESCAPE the newline character.
# This can be done by writing \n into our string. Although in the code this will
# appear as two characters, the Python interpreter will format our string to contain
# a single newline character instead of \n.
really_two_lines = "This is the first line.\nThis is a second line!"
print("Are these two lines?", really_two_lines)

# As you can see it also highlights \n in an orange color, indicating that we escaped
# a character. Other examples using the \n char:

print("Hello", "\n", "world!")  # This will write additional, unwanted spaces!
print("Hello", "\n", "world!", sep="")  # This will not.

# There are other characters that need to be escaped. One obvious one is the " character,
# since the interpreter uses these chars to denote the beginning and the end of the string.
# To tell the interpreter, that we don't start or end a string, but rather want to write the
# char ", we have to escape it like this: \".

escaping_double_quotation = "My quote for the day is: \"Drinking milk is awesome!\""  # Using the \" syntax
escaping_single_quotation = "My quote for the day is: \'Drinking milk is awesome!\'"  # Using the \' syntax
print("Using double quotation:", escaping_double_quotation)
print("Using single quotation:", escaping_single_quotation)

# We also have to escape tabs with \t and backslashes with \\:

escaping_tab = "Tab separated:\t\'Haha\'"
print("Using tabs:", escaping_tab)

escaping_backslash = "C:\\Windows\\System32"
print("Using a backslash:", escaping_backslash)
