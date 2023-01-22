# Indexing is a concept through which we can extract certain parts of a
# multi-component type, like a string. A string is build from characters,
# so its components are small, length 1 string elements.

my_sentence = "I am angry, because I have cold coffee!"

# This sentence is 39 characters long, each character being a length 1 string.
# To obtain a character at a given position from the string, we can use indexing.
# The first character of the string is at index 0. The second is at index 1, the
# third is at index 2, etc... To index a string use the my_string[index] syntax
# like this:

print("The first character is:", my_sentence[0])
print("The second character is:", my_sentence[1])
print("The third character is:", my_sentence[2])

# The last character of the string is at index len(my_string) - 1. So if we have a
# string with length 39, and we start counting from 0, the last valid index is 38.

print("Method1: the last character is:", my_sentence[38])  # this is a bit restrictive
print("Method2: the last character is:", my_sentence[len(my_sentence) - 1])  # this is more universal

# To write less, we can use negative indices. When using '-a' as an index (where 'a' is an
# integer), Python knows that what we really mean is 'len(my_string) - a'. This way, we can
# omit the len(my_string) part and only write the negative index:

print("Method3: the last character is:", my_sentence[-1])  # universal and short = the best syntax

# Using invalid indices i.e., indices that are greater than or equal to len(my_string) will
# give us an error. If we uncomment the following lines, the scipr will stop there:
# print(my_sentence[39])
# print(my_sentence[50])
# print(my_sentence[len(my_sentence)])

# This is also the case with negative indices:
# print(my_sentence[-100])

# To extract a range from a string, we can use slices. Slices are also written between
# square brackets, but they contain integers separated by colons. We can extract a substring
# with the following syntax: my_string[from:to], where 'from' and 'to' are integers designating
# the first characters index and the last characters index PLUS ONE. This means, that while the
# lower bond of a slice is INCLUDED, the upper bound of a slice is EXCLUDED.

print("First five characters: \'", my_sentence[0:5], "\'", sep="")  # will be 'I am '
print("First ten characters: \'", my_sentence[0:10], "\'", sep="")  # will be 'I am angry'

# Note, that although 'a' is the character with an index of 5, my_sentence[0:5] won't contain
# 'a' as its last character. Also, although ',' is the character with an index of 10,
# my_sentence[0:10] won't contain ',' as its last character.

# Slices shouldn't necessarily start with a 0:
print("Characters going from idx=10 to idx=19: \'", my_sentence[10:20], "\'", sep="")

# If a slice starts with an index of 0, we can omit it:
print("By omitting the first index, we start from the beginning: \'", my_sentence[:10], "\'", sep="")

# Also, if a slice goes until the end of a string, we can omit the second index:
print("By omitting the second index, we go until the end: \'", my_sentence[20:], "\'", sep="")

# A third index can also be used in slices, specifying a step-size. So if we want
# every second element between idx=10 and idx=19 we should write:
print("Skipping every second character: \'", my_sentence[10:20:2], "\'", sep="")

# The default step-size is 1, so we can also omit the step-size:
print("\'", my_sentence[10:20:], "\' and \'", my_sentence[10:20], "\' are equal", sep="")

# We can also omit every index from the slice, getting the original string back:
print("Method 1: full string:\'", my_sentence[:], "\'", sep="")
print("Method 2: full string:\'", my_sentence[::], "\'", sep="")

# Negative step-sizes allow us to go backwards. However, in these cases the starting
# index should be greater than the ending index:
print("Going backwards: \'", my_sentence[20:10:-1], "\'", sep="")
print("Going backwards (full sentence): \'", my_sentence[::-1], "\'", sep="")

# Since indexed and sliced strings are also strings, we can store them in variables, or
# operate on them directly with methods:

my_modified_str = my_sentence[20:10:-1]  # declare a new variable with a substring as its value
my_modified_str = my_modified_str.ljust(50, "/")  # modify the new variable
print("Modifying a string-slice: \'", my_modified_str, "\'", sep="")

# And lastly, since string-slices are also strings, we can slice them again!
print("Chained slices: \'", my_sentence[::-1][5:10:2], "\'", sep="")
print("Chained slices (modified): \'", my_sentence[::-1][5:10:2].center(50, "~"), "\'", sep="")
