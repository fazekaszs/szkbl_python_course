# Query a user input. This could be for example:
# 20,10,40,30,90,5,100,7,5
list_of_numbers = input("Give me a number list: ")

# In the first loop, we check and swap (if necessary) the following elements:
#  idx 0 with idx 1
#  idx 2 with idx 3
#  ...
#  idx N-1 with idx N OR idx N-2 with idx N-1 (if N is odd)

# Create two buffer strings for the number pairs we will encounter.
snumber1 = ""
snumber2 = ""

# 'build_snumber1' will be True, if we are currently building the 'snumber1' buffer,
#  and False, if we are currently building the 'snumber2' buffer.
build_snumber1 = True

# In the end of every loop, this will contain the pairwise-sorted number list.
new_number_list = ""

# The main loop.
for char in list_of_numbers:

    # If we encounter a comma character, and we are currently building 'snumber1',
    #  we switch from building 'snumber1' to building 'snumber2'.
    if char == "," and build_snumber1:
        build_snumber1 = False

    # If we encounter a comma, but we are not currently building 'snumber1', then this means
    #  we finished building 'snumber2' too! Thus, we can make the comparison between the two
    #  numbers built.
    elif char == ",":

        # Reset the 'snumber1' builder flag.
        build_snumber1 = True

        # Convert to int.
        inumber1 = int(snumber1)
        inumber2 = int(snumber2)

        # Make comparison.
        if inumber1 <= inumber2:
            new_number_list += snumber1 + "," + snumber2 + ","
        else:
            new_number_list += snumber2 + "," + snumber1 + ","

        # Reset the buffer strings.
        snumber1 = ""
        snumber2 = ""

    # The current character is NOT a space, and we are building 'snumber1'.
    elif build_snumber1:
        snumber1 += char

    # The current character is NOT a space, and we are building 'snumber2'.
    else:
        snumber2 += char

# We also need some final corrections.

# If the user didn't add a comma to the end of the number list string, then it didn't trigger
#  the last comparison. This can be noticed if the 'snumber2' buffer is not empty.
if snumber2 != "":

    inumber1 = int(snumber1)
    inumber2 = int(snumber2)

    if inumber1 <= inumber2:
        new_number_list += snumber1 + "," + snumber2 + ","
    else:
        new_number_list += snumber2 + "," + snumber1 + ","

# Also, if the user gave an odd length list of numbers, we can lose the last number during the process.
# To overcome this, we have to check whether 'snumber1' is empty, and if it isn't, then we add its content
#  to the new list of numbers.
elif snumber1 != "":

    new_number_list += snumber1

# Shows the new list with pairwise ordering.
print(new_number_list)
