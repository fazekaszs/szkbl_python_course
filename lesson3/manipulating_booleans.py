# The 'in' keyword (binary operation) can be used to check whether one
# thing contains another. For example, this is especially useful for
# checking whether a string contains a substring:

contains_mouse = "mouse" in "My house is flooded with mice! They are disgusting!"
contains_mice = "mice" in "My house is flooded with mice! They are disgusting!"
print("The sentence contains the word \"mouse\":", contains_mouse)
print("The sentence contains the word \"mice\":", contains_mice)

# The 'in' keyword can be negated with 'not':

test_not_in = "mouse" not in "My house is flooded with mice! They are disgusting!"
print("The sentence doesn\'t contains the word \"mouse\":", test_not_in)

# Bools can be transformed with the 'and' and 'or' operations.
# These are the classical binary operators from mathematics.
# They work the following way:

# True and True -> True
# True and False = False and True = False and False -> False

# True or True = True or False = False or True -> True
# False or False -> False

my_sentence = "I was learning Python even at 3am. I was finally... happy!"

should_be_true = "Python" in my_sentence and "3am" in my_sentence
print("The sentence contains \"Python\" and also \"3am\":", should_be_true)

should_be_false = "Python" in my_sentence and "festival" in my_sentence
print("The sentence contains \"Python\" and also \"festival\":", should_be_false)

using_or = "Python" in my_sentence and "festival" in my_sentence
print("The sentence contains \"Python\" or \"festival\":", using_or)

# The keywords 'in', 'not', 'and', and 'or' can be used together any times
# with a correct syntax:

complex_bool = not ("festival" in "Python" or "qu" in "equal") or "hello" in "hello world!"
print("I evaluated your complex boolean. The resul is:", complex_bool)

# Checking the type of a variable can be done with the 'type' function.

my_string = "Hello world!"
print("The type of my string is:", type(my_string))

# And to compare it with exact types we can use the 'is' keyword:

my_strin_is_a_string = type(my_string) is str
my_strin_is_an_int = type(my_string) is int
print("This is a string?", my_strin_is_a_string)
print("This is an int?", my_strin_is_an_int)

# We can use type checking along with other boolean operations:

is_a_string_with_world_in_it = type(my_string) and "world" in my_string
print("My string is a string and contains the word \"world\"", is_a_string_with_world_in_it)

# Another, more commonly used comparison operator is the comparing equality operator.
# It is written as 'a == b', where we compare whether 'a' and 'b' are equal objects.

two_and_three_are_equal = 3 == 2
print("Are 2 and 3 equal?", two_and_three_are_equal)

# We can negate this operator two ways: using the already learned 'not' keyword or
# using the not-equal operator:

not_equal1 = not 3 == 2
not_equal2 = 3 != 2
print("Are 2 and 3 NOT equal? The first way:", not_equal1, "and second way:", not_equal2)

# ALL the operators can be used together to create complex boolean expressions!
