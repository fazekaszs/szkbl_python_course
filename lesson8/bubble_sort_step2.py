list_of_numbers = input("Give me a number list: ")

# In the first loop, we check and swap (if necessary) the following elements:
#  idx 0 with idx 1
#  idx 2 with idx 3
#  ...
#  idx N-1 with idx N OR idx N-2 with idx N-1 (if N is odd)

snumber1 = ""
snumber2 = ""
build_snumber1 = True

new_number_list = ""
for char in list_of_numbers:

    if char == "," and build_snumber1:
        build_snumber1 = False

    elif char == ",":

        build_snumber1 = True

        inumber1 = int(snumber1)
        inumber2 = int(snumber2)

        if inumber1 <= inumber2:
            new_number_list += snumber1 + "," + snumber2 + ","
        else:
            new_number_list += snumber2 + "," + snumber1 + ","

        snumber1 = ""
        snumber2 = ""

    elif build_snumber1:
        snumber1 += char
    else:
        snumber2 += char

# END OF FIST LOOP

if snumber2 != "":

    inumber1 = int(snumber1)
    inumber2 = int(snumber2)

    if inumber1 <= inumber2:
        new_number_list += snumber1 + "," + snumber2 + ","
    else:
        new_number_list += snumber2 + "," + snumber1 + ","

elif snumber1 != "":
    new_number_list += snumber1

# END OF FIRST LOOP POST-PROCESSING

# In the second loop, we check and swap (if necessary) the following elements:
#  SKIP idx 0
#  idx 1 with idx 2
#  idx 3 with idx 4
#  ...
#  idx N-2 with idx N-1 OR idx N-1 with idx N (if N is odd)

list_of_numbers = new_number_list

snumber1 = ""
snumber2 = ""
build_snumber1 = False  # now we start by building 'snumber2' first

new_number_list = ""
for char in list_of_numbers:

    if char == "," and build_snumber1:
        build_snumber1 = False

    elif char == ",":

        build_snumber1 = True

        # THIS is the new part! In the first case when 'snumber2' is built, 'snumber1' will be
        #  empty! This is a special case we have to handle!
        if snumber1 == "":

            new_number_list += snumber2 + ","
            snumber2 = ""
            continue

        # Here, we continue as usual...
        inumber1 = int(snumber1)
        inumber2 = int(snumber2)

        if inumber1 <= inumber2:
            new_number_list += snumber1 + "," + snumber2 + ","
        else:
            new_number_list += snumber2 + "," + snumber1 + ","

        snumber1 = ""
        snumber2 = ""

    elif build_snumber1:
        snumber1 += char
    else:
        snumber2 += char

# END OF SECOND LOOP

if snumber2 != "":

    inumber1 = int(snumber1)
    inumber2 = int(snumber2)

    if inumber1 <= inumber2:
        new_number_list += snumber1 + "," + snumber2 + ","
    else:
        new_number_list += snumber2 + "," + snumber1 + ","

elif snumber1 != "":
    new_number_list += snumber1

# END OF SECOND LOOP POST-PROCESSING (same as in the first case)

print(new_number_list)
