# The concept of binary operations: an operator 'R' is a binary operator, that
# can be applied to objects 'a' and 'b' if the following syntax makes sense to the
# Python interpreter: a R b. Examples are the following operations:
# - addition: 1 + 2 (in this example R = +, a = 1, b = 2)
# - subtraction: 10 - 5 or number_of_cookies - 10
# - multiplication, division

# We can use the ** binary operator to exponentiate two numbers:
use_exp_on_ints = 3 * 10 ** 2  # will be equal to 300
use_exp_on_floats = 2.718 ** - 3.0  # will be equal to exp(-3)
print("I calculated", use_exp_on_ints, "and", use_exp_on_floats)

# We can also write floats using the already learned E notation:
e_notation_on_floats = 3E2  # will also be equal to 300, but now it's a float!
print("Using the E notation:", e_notation_on_floats)

# To get the integer part of a division we have already learned how we can use
# the int(...) function. There is an equivalent way for doing this:
int_div_old = int(7 / 2)  # will equal 3
int_div_new = 7 // 2  # will also be equal to 3
print("Doing integer division the old way:", int_div_old, "and the new way:", int_div_new)

# To get the remainder of a division, we can use the modulo operation with the % character.
# This is the opposite operation of integer division:
# With 7 // 2 you will get 3, since 7 contains 2 three times...
# ...with 7 % 2 you will get 1, since 7 contains 2 three times and 7 - 3 * 2 = 1 (the remainder).
# This operation is called modular division:

modular_div = 7 % 2
print("7 contains 2", int_div_new, "times with a remainder of", modular_div)
