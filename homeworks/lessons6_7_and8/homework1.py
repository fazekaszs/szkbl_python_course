number_list = input("Give me the numbers: ")

current_smallest = None
number_buffer = ""

for char in number_list:

    if char == " ":
        continue

    elif char == ",":

        number_buffer = float(number_buffer)

        if current_smallest is None or number_buffer < current_smallest:
            current_smallest = number_buffer

        number_buffer = ""

    else:

        number_buffer += char

print("The smallest number is:", current_smallest)
