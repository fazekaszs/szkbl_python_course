signs = input("Give me plus and minus signs: ")

for idx in range(10):

    print("Round ", idx + 1, ":", sep="")

    dotted_signs = ""
    counter = 1

    for char1, char2 in zip(signs[:-1], signs[1:]):

        dotted_signs += char1
        if char1 != char2:
            dotted_signs += counter * "."
            counter += 1

    dotted_signs += signs[-1]

    remainder = len(dotted_signs) % len(signs)
    signs += "+" if remainder % 2 == 0 else "-"

    print("The new signs are:", signs)
