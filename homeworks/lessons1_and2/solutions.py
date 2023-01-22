# Homework 1, solution 1
first_name = input("First name: ")
last_name = input("Last name: ")
print(first_name, last_name)
print(first_name + "-" + last_name)
print(first_name, ";", last_name, sep="")

# Homework 1, solution 2
full_name = first_name + " " + last_name
print(full_name)
print(full_name.replace(" ", "-"))
print(full_name.replace(" ", ";"))

# Homework 2
my_number_str = input("Give me a number: ")
my_number_int = int(my_number_str)
print(my_number_str * my_number_int)
print((my_number_str + "@") * my_number_int)

# Homework 3
my_number_str = input("Give me a number: ")
my_number_int = int(my_number_str)
number_of_2s = my_number_str.count("2")
number_of_3s = my_number_str.count("3")
print(my_number_int * int(number_of_3s / number_of_2s))

# Homework 4, solution 1
my_input = input("My input: ")
print(my_input.strip().rjust(30, "~").center(50, "%"))

# Homework 4, solution 2
stripped = my_input.strip()
rjusted = "~" * (30 - len(stripped)) + stripped
centered = 10 * "%" + rjusted + 10 * "%"
print(centered)

# Homework 5
current_year = int(input("Current year: "))
my_birthyear = int(input("My birthyear: "))
my_dogs_birthyear = int(input("My dogs birthyear: "))
ratio1 = (current_year - my_birthyear) / (current_year - my_dogs_birthyear)
ratio2 = (current_year + 17 - my_birthyear) / (current_year + 17 - my_dogs_birthyear)
print("You are", round(ratio1, 3), "times older than your dog.")
print("However, you will only be", round(ratio2, 3), "times older in 17 years!")
