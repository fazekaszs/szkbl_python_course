pairs = input("Give me the character+number pairs: ")
char_list = input("Give me a string of characters: ")

total = 0
for query_char in char_list:

    build_number = False
    current_number = ""

    for p_char in pairs:

        if p_char == "," and build_number:
            break

        elif p_char != ":" and build_number:
            current_number += p_char

        elif p_char == query_char:
            build_number = True

    total += float(current_number)

print("The sum is:", total)
