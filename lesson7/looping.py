# Using loops, one can iterate over all the components of an iterable.
# Strings are good examples for this: the whole string is composed of
#  characters, and with looping we can do something with each character.
# Loops have a similar structure to if statements: we start the line with
#  the statement name (in our case, with the keyword 'for'), at the end of
#  the line we write a colon character, and then we start a new codeblock in
#  the next line (i.e., we indent everything contained inside the 'for' loop.

my_sentence = "A sentence, containing a lot of characters."  # define the iterable (in this case, a string)

for character in my_sentence:  # start of the 'for' loop

    # This is a new block, already inside the 'for' loop!
    print("Printing a character in my_string:", character)  # do this 'print' for every character inside the string

print()  # this is outside the 'for' loop's block

# The word 'character' can be anything that is a valid variable name, since in the first
#  line of a 'for' loop we really declare a new variable! However, in contrast to the
#  variable declaration scheme we are already familiar with ('my_var = something'), this
#  is a different syntax. The new variable declared in a 'for' loop will take on each value
#  inside the iterable, one-by-one, sequentially.

# We can use external variables, if-else statements, and other loops inside loops.
# This way, it is possible to build a string, depending on the different characters
#  encountered inside another string:

new_string = ""  # in the beginning, this string is empty

for character in my_sentence:

    new_string += character
    # This is equivalent to 'new_string = new_string + character'. See
    #  lesson3 for in-place operators.

    # If the current character is an 'n', we also add a hyphen to the new string.
    if character == "n":
        new_string += "-"

# This will print the same as 'my_string', but will contain a hyphen after every 'n' character:
print("Writing a hyphen after every \'n\' character:", new_string)
# "A sen-ten-ce, con-tain-in-g a lot of characters."

# In another example, we can build a string, that points to the charged residues inside a
#  protein sequence:

my_protein = "EEEAVRLYIQWLKEGGPSSGRPPPS"
charged_residues = "EDKR"
charged_residue_arrows = ""
for residue in my_protein:

    if residue in charged_residues:
        charged_residue_arrows += "^"
    else:
        charged_residue_arrows += " "

print("Searching charged residues inside my protein:")
print("\t" + my_protein)
print("\t" + charged_residue_arrows)

# We can also count the number of 'G' and 'C' characters inside a DNA sequence:

my_dna_sequence = "AGCCCATTCCAG"
count_of_gc = 0
for nucleotide in my_dna_sequence:
    if nucleotide == "G" or nucleotide == "C":
        count_of_gc += 1

print("The GC ratio is:", count_of_gc / len(my_dna_sequence))

# This is equivalent to the following "more elegant" solution:
count_of_gc = my_dna_sequence.count("G") + my_dna_sequence.count("C")
print("The GC ratio is (with the more elegant method):", count_of_gc / len(my_dna_sequence))

# Another iterable we can use is a 'range' object. This provides us whole numbers
#  up until a certain number, which we specify inside the 'range' function. It works like
#  this:

print("Printing squared values:")
for idx in range(10):  # idx will go from 0 to 9 (NOT including 10!)
    print("\t", idx, "\t", idx ** 2, sep="")  # we print 'idx' and it's square

# This will result in the following output:
# 0 0
# 1 1
# 2 4
# 3 9
# ...
# 8 64
# 9 81
# We can use copy these numbers and paste them into Excel for plotting.
# Ranges provide us an easy and standard way to iterate through a range of integers.
# We can also specify a starting index, along with a stepsize in a similar way than
#  in slices:

print("Printing squared values (from 5):")
for idx in range(5, 10):  # idx will go from 5 to 9
    print("\t", idx, "\t", idx ** 2, sep="")

print("Printing squared values (from 5, only odd numbers):")
for idx in range(5, 10, 2):  # idx will go from 5 to 9 with a stepsize of 2
    print("\t", idx, "\t", idx ** 2, sep="")

# Inside loops, we can use the 'break' keyword, which forces the loop to quit
#  prematurely i.e., before reaching the end of our iterable.

my_sentence_first_part = ""
for character in my_sentence:

    my_sentence_first_part += character  # build our string from the characters of 'my_sentence'

    if character == ",":  # if we encounter a ',' character during iteration...
        break  # ...we stop the loop

# This will only print 'A sentence,', since we exit when we see a ',' character:
print("The first part of our sentence is", my_sentence_first_part)

# Another keyword commonly used inside loops, along with the 'break', is the 'continue'
#  keyword. When a 'continue' keyword is encountered by the program, the loop skips the loop's code
#  block after the 'continue' keyword and continues the loop with the next element.

numbers_str = "0123456789"
modified_numbers_str = ""

for digit in numbers_str:

    modified_numbers_str += digit

    if int(digit) % 2 != 0:  # if the digit is not even...
        continue  # ...continue with the next digit and next iteration

    modified_numbers_str += "."  # this will only be added, if the digit is even!

    if int(digit) % 3 != 0:  # if the digit is not divisible by 3...
        continue  # ...again, continue with the next digit and next iteration

    modified_numbers_str += ":"  # this will only be added, if the digit is divisible by 6!

# This should print "0.:12.34.56.:78.9"
print("The digits with their flags are:", modified_numbers_str)

# We can reimplement our 'GC' counter using the 'continue' keyword (again, this
#  is NOT the preferred way):

count_of_gc = 0
for nucleotide in my_dna_sequence:

    if nucleotide == "A" or nucleotide == "T":  # if the nucleotide is NOT a 'G' or 'C'...
        continue  # ...don't do anything and continue with the next nucleotide...

    count_of_gc += 1  # ...else, add 1 to our counter!

print("The GC ratio is (with the \'continue\' method:", count_of_gc / len(my_dna_sequence))

# Ranges are commonly used to iterate over an iterable, while also knowing the
#  current index of the element taken out from the iterable. For example, if we simply use
#  'for character in my_string'
#  we cannot know the index of our character inside the loop. To overcome this, one can use ranges:

print("Nucleotides with their indices:")
for idx in range(len(my_dna_sequence)):  # 'idx' will go from 0 to 'len(my_dna_sequence) - 1'

    nucleotide = my_dna_sequence[idx]  # we take out the nucleotide at position 'idx'

    # Now, we can operate BOTH with 'idx' and 'nucleotide' as valid variables!

    print("\tI have a nucleotide \"", nucleotide, "\" at index ", idx, sep="")

# An easier way to do this is through the usage of 'enumerate' objects. We add an iterable to
#  the 'enumerate' function as its argument and this will provide us BOTH the index of the element
#  and the element itself_

print("Nucleotides with their indices (with enumerate):")
for idx, nucleotide in enumerate(my_dna_sequence):
    print("\tI have a nucleotide", nucleotide, "at index", idx)

# Using 'enumerate', the positions of the guanines can be printed out the following way:

positions_of_g = ""
for idx, nucleotide in enumerate(my_dna_sequence):

    if nucleotide == "G":
        positions_of_g += str(idx + 1) + " "

print("The positions of guanines in the DNA sequence are: ", positions_of_g)

# Finally, here is a more complicated code for searching the indices of a certain substring
#  inside a longer string:

search_sequence = "CC"  # we are searching for the occurrences of GAT inside our DNA sequence

print("Searching for the substring", search_sequence, "in the DNA sequence", my_dna_sequence)
for idx in range(len(my_dna_sequence) - len(search_sequence) + 1):

    # 'idx' is the start index of a subsequence inside 'my_dna_sequence'.
    # For example, if we search for a length 3 subsequence inside a length 10 string,
    #  we have to check the subsequences with indices 0..3, 1..4, 2..5, ... up until
    #  7..10 (upper index excluded). This way, the upper bound should be 10 - 3 + 1 = 8
    #  (the +1 is necessary, since the upper bound is excluded from 'range').

    current_subsequence = my_dna_sequence[idx:idx+len(search_sequence)]  # this is our substring

    if current_subsequence == search_sequence:
        print("\tSearch sequence found at index", idx)
