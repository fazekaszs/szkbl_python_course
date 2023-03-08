# As a refresher, we discussed how the "enumerate" iterator works:

my_sentence1 = "This is the first, fairly long, and wordy sentence, as an example."

char_positions = ""
for idx, char in enumerate(my_sentence1):
    char_positions += "char \"" + char + "\" at " + str(idx) + ", "

print(">>> Characters and their positions in the first sentence:")
print(char_positions)

# Next, we iterated over two strings in parallel.
# This can be done using the "range" iterator, until we reach the
#  last valid index of the shorter string. Here, we can use the ternary
#  if-else operator to get the shorter sequence's length.

my_sentence2 = "This is the second, shorter sentence."
min_length = len(my_sentence1) if len(my_sentence1) < len(my_sentence2) else len(my_sentence2)
char_pairs = ""

for idx in range(min_length):

    char1 = my_sentence1[idx]
    char2 = my_sentence2[idx]

    char_pairs += "(" + char1 + ", " + char2 + "), "

print(">>> Character pairs from the two sentences:")
print(char_pairs)

# However, this can be done more easily with the "zip" iterator.
# This creates pairs of characters, when two strings are given to it:

char_pairs = ""
for char1, char2 in zip(my_sentence1, my_sentence2):

    char_pairs += "(" + char1 + ", " + char2 + "), "

print(">>> Character pairs from the two sentences (using zip):")
print(char_pairs)

# A "zip" iterator can take any number of arguments and this way we can iterate
#  over 2, 3, ... etc. number of string simultaneously. So if we had a third string
#  we could write "zip(my_sentence1, my_sentence2, my_sentence3)" in the for loop.
# Of course, in this case we would need three character variables like this:
# "for char1, char2, char3 in zip(...)"

# A not so known syntax of Python is the for-else syntax. In this case if the loop
#  exits with a "break" keyword the "else" part won't run, however, if the loop manages
#  to finish without ever encountering a "break" the "else" arm will execute:

print(">>> Counting: ", end="")
for idx in range(10):

    print(idx, end=" ")

    if idx == 11:
        break  # this will never run, since "idx" will only go until 9

else:
    print("--- The \"else\" part got executed!")

print(">>> Counting (again): ", end="")
for idx in range(10):

    print(idx, end=" ")

    if idx == 5:
        break  # this will be executed!

else:
    print("This \"else\" part should not get executed!")

# A "while" loop is simpler than a "for" loop: it runs, until the condition after the "while"
#  keyword switches from True to False. As soon as the condition is evaluated as False, the
#  inner block of the "while" loop stops executing.

my_number = 0
print(">>> Starting a \"while\" loop:")
while my_number < 100:  # the syntax is the "while" keyword, and then a condition after that

    my_number = 1 + my_number ** 2
    print("\tIn the wile loop my number is:", my_number)
    # "my_number" will be 0, 1, 2, 5, 26, 676

print("\tThe wile loop ended...")

# "while" loops can reproduce the behavior of "for" loops. For this however,
#  we have to introduce an external counter variable (here "idx") and continuously
#  increment it in the loop's body.

idx = 0
print(">>> Starting a \"while\" loop to mimic a \"for\" loop:")
while idx < len(my_sentence1):

    char = my_sentence1[idx]

    if char == " ":
        print("\tFound a space character at index", idx)

    idx += 1  # here is the incrementation

# As a further exercise let's test the Goldbach conjecture on different numbers!
# This conjecture states that if you take a positive whole number "n" and apply the
#  following rules to it iteratively:
#  1) if n is even: n = n / 2
#  2) if n is odd: n = 3 * n + 1
#  then eventually you will always reach the following cycle:
#  1 -> 4 -> 2 -> 1
# For example if you start with the number 3:
# 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

goldbach_number = 7
print(">>> Starting the Goldbach conjecture process with the following number:", goldbach_number)

while goldbach_number != 1:  # we do the iteration until we reach the number 1

    if goldbach_number % 2 == 0:  # n is even
        goldbach_number //= 2

    else:  # n is odd
        goldbach_number *= 3
        goldbach_number += 1

    print("\tThe current number is:", goldbach_number)
