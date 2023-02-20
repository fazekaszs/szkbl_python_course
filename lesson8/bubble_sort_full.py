list_of_numbers = input("Give me a number list: ")
max_iter = int(input("Give me the maximum number of iterations: "))

# This 'for' loop will do two swap-cycles consecutively.
# NOTICE that this loop is at the TOP of the "loop hierarchy", i.e. there are two
#  sub-loops inside it (the two previously written swapping loops, see bubble_sort_step1.py and
#  bubble_sort_step2.py).
for idx in range(max_iter):

    # With this variable, we track whether a swap happened during the current iteration.
    # We start by defining this as False, but if a swap happens during the iteration, we
    #  set it to True.
    # At the end of the iteration we check whether this variable is False, and if it is,
    #  we break out of the loop (since we don't need to continue further).
    swap_happened = False

    # START OF FIRST SUB-LOOP

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
                swap_happened = True

            snumber1 = ""
            snumber2 = ""

        elif build_snumber1:
            snumber1 += char
        else:
            snumber2 += char

    # END OF FIST SUB-LOOP

    if snumber2 != "":

        inumber1 = int(snumber1)
        inumber2 = int(snumber2)

        if inumber1 <= inumber2:
            new_number_list += snumber1 + "," + snumber2 + ","
        else:
            new_number_list += snumber2 + "," + snumber1 + ","
            swap_happened = True

    elif snumber1 != "":
        new_number_list += snumber1

    # END OF FIRST SUB-LOOP POST-PROCESSING

    # START OF SECOND SUB-LOOP

    list_of_numbers = new_number_list

    snumber1 = ""
    snumber2 = ""
    build_snumber1 = False

    new_number_list = ""
    for char in list_of_numbers:

        if char == "," and build_snumber1:
            build_snumber1 = False

        elif char == ",":

            build_snumber1 = True

            if snumber1 == "":

                new_number_list += snumber2 + ","
                snumber2 = ""
                continue

            inumber1 = int(snumber1)
            inumber2 = int(snumber2)

            if inumber1 <= inumber2:
                new_number_list += snumber1 + "," + snumber2 + ","
            else:
                new_number_list += snumber2 + "," + snumber1 + ","
                swap_happened = True

            snumber1 = ""
            snumber2 = ""

        elif build_snumber1:
            snumber1 += char
        else:
            snumber2 += char

    # END OF SECOND SUB-LOOP

    if snumber2 != "":

        inumber1 = int(snumber1)
        inumber2 = int(snumber2)

        if inumber1 <= inumber2:
            new_number_list += snumber1 + "," + snumber2 + ","
        else:
            new_number_list += snumber2 + "," + snumber1 + ","
            swap_happened = True

    elif snumber1 != "":
        new_number_list += snumber1

    list_of_numbers = new_number_list

    # END OF SECOND SUB-LOOP POST-PROCESSING

    # If a swap didn't happen during the iteration, this means we are done and
    #  exit the 'for' loop.
    if not swap_happened:
        break

print(list_of_numbers)
