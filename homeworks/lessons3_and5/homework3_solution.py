i1_str = input("Give me an integer: ")

i2 = int(i1_str + i1_str[::-1])
rem1 = i2 % int(i1_str)

i3 = int(i1_str + i1_str[::-1].replace("9", "5").rjust(10, "1"))
rem2 = i3 % int(i1_str)

print("The two remainders are", rem1, "and", rem2)
