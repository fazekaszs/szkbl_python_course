# Conditionals allow us to examine the truthiness of an expression
#  and act accordingly.

user_number = input("Give me a whole number: ")
user_number = int(user_number)

# Using an 'if' statement we can run program-blocks conditionally i.e.,
#  only if the evaluated expression is truthy. In our case this expression
#  evaluates to a boolean (True or False value). Code-blocks are "indented"
#  using a TAB character:

if user_number < 10:  # examine the truthiness of the 'user_number < 10' expression

    # Run this code block ONLY IF the expression is truthy!
    # As you can see, this block is indented, which means, a TAB
    #  character is written before every line in the block.
    print("If statement #1: The user input is less than 10!")

# This line is NOT inside the previous block (not indented), so it will
#  run regardless of the previous 'if' statement.
print("This will always be printed!")

# If you highlight a part of your code and press TAB, you can indent the highlighted lines.
# To de-indent them, press 'Shift+TAB'. This way, you can easily organize your code between
#  different indentation levels.

# 'if' statements can be continued with an 'else' block. The content of the 'else' block
#  will only run, if the 'if' statement's block doesn't run!

if user_number < 15:
    print("If statement #2: The user input is less than 15!")
else:
    print("Else statement for if statement #2: The user input is more than 15, or equal to it!")

# As you can see, an 'else' statement is optional, but if we use one, we need an 'if' statement before it!
# Finally, between an 'if' and 'else' statement, we can write as many 'elif' statements as we want.
# The block of the 'elif' statement only runs if the previous blocks before it do not run!

if user_number == 20:
    print("If statement #3: The user input is equal to 20!")
elif user_number == 30:

    # Will run if the first condition fails.
    print("Elif statement #1 for if statement #3: The user input is equal to 30!")

elif user_number < 50:

    # Will run if the first two condition fail.
    print("Elif statement #2 for if statement #3: The user input is smaller than 50, but not 20 or 30!")

else:

    # Will run if all conditions before it fail.
    print("Else statement for if statement #3: The user input is greater than or equal to 50!")

# When we check number-ranges, besides the '<' and '>' ('smaller than' and 'greater than') operators we can
#  use the '<=' and '>=' ('smaller than or equal' and 'greater than or equal') operators. Also, we don't have
#  to write '2 < user_number and user_number < 12', we can shorten this to '2 < user_number < 12'.

if 2 < user_number < 12:
    print("If statement #4: The user input is between 2 and 12 (borders EXCLUDED)!")
elif 12 <= user_number <= 50:
    print("If statement #4: The user input is between 12 and 50 (borders INCLUDED)!")
elif 100 > user_number >= 50:
    print("If statement #4: The user input is between 50 and 100 (lower bound INCLUDED, upper EXCLUDED)!")
else:
    print("Else statement for if statement #4: The user input is not in the range of (2, 100)!")

# We can create complicated boolean expressions, evaluate them first, and THEN use them in a
#  conditional.

my_condition = 5 < 10 and "h" in "Haha" or type("K") is int

if my_condition:
    print("If statement #5: My complicated condition is True")

# We can build up the same condition from its building parts:

my_condition = 5 < 10
my_condition = my_condition and "h" in "Haha"
my_condition = my_condition or type("K") is int

if my_condition:
    print("If statement #6: My complicated condition is (still) True")

# Note, that the 'and' binary operator has precedence over the 'or' binary operator. This means,
#  that first the 'and' operator is applied and only after this the 'or' operator. This is similar
#  to multiplication having precedence over addition:
# - In 'a * b + c' we FIRST multiply 'a' with 'b', and only after this we add 'c' to the result
# - In 'a and b or c' we FIRST 'and' 'a' with 'b', and only after this we 'or' 'c' with the result

# Beware, that there is a common telltale sign of beginner programmers! You do not have to check whether
#  the value of a condition is True in an 'if' statement! This is automatically done by the statement
#  itself!

if my_condition == True:  # this works, but is pretty lame... only 'my_condition' would be enough
    print("If statement #6: My complicated condition is (still... still...) True")

# If you are using PyCharm, you can even see a yellow squiggly line under the expression, indicating
#  that you could simplify the expression!

# You can create nested 'if-elif-else' statements by creating different indentation levels!
# Here is an example for this:

my_sentence = input("Give me a sentence: ")  # query the user
my_sentence = my_sentence.replace(" ", "").replace(".", "").replace(",", "").lower()  # preprocess the sentence

known_palindrome1 = "Yo, banana boy.".replace(" ", "").replace(".", "").replace(",", "").lower()
known_palindrome2 = "Evil olive.".replace(" ", "").replace(".", "").replace(",", "").lower()

if my_sentence == my_sentence[::-1]:

    print("If statement #7: The sentence is a PALINDROME!")
    print("\t\"", my_sentence, "\" and \"", my_sentence[::-1], "\" are equal!", sep="")

    if my_sentence == known_palindrome1:
        print("\tI know this palindrome! This is Palindrome #1!")
    elif my_sentence == known_palindrome2:
        print("\tI know this palindrome! This is Palindrome #2!")
    else:
        print("\tI am not familiar with this palindrome, unfortunately...")

else:

    print("Else statement for if statement #7: The sentence is NOT a PALINDROME!")

# Finally, for really short 'if-else' statements, we can use the ternary operator form of
#  the 'if-else' statement:

evenness = "even" if user_number % 2 == 0 else "odd"  # it is more compact (less indented and fewer lines)

print("Ternary if-else statement result: ", evenness)
