# This script serves as an introduction to lists, just like in the last lesson,
#  but with more details and in an extended fashion.

# Lists are objects that can contain multiple values and are growable/shrinkable
#  as the number of values they hold changes. They can be used when the "number of
#  variables needed" is unknown before running the program.

# Creation of empty lists (both rows are equivalent):
my_list1 = list()
my_list2 = []

# Lists are printable:
print("List", my_list1, "and list", my_list2, "are both emptly...")

# Creation of non-empty lists:
# A list can contain multiple different types:
my_list3 = ["a", 1, 1.2, True]
# And can be defined using multiple rows:
my_list4 = [
    1, 2, 3,
    4, 5,
    6,
    7, 8, 9
]

print("...while list", my_list3, "and list", my_list4, "are NON-empty lists!")

# The addition operation is a valid operation on lists. It produces another list that is
#  the concatenated version of the two arguments:
my_list_sum = my_list3 + my_list4
print("List 3 and 4, concatenated:", my_list_sum)

# In-place addition also works on lists:
my_list_sum += my_list3
print("List 3, 4, and (again) 3, concatenated:", my_list_sum)

# The "list" function is more explicit than the "[]" notation. Also, the "list" function
#  can convert iterable objects into lists of the elements from these iterable objects:
my_list_from_iterable = list("abcd1234")
print("The elements of a list created from a string are the characters of that string:", my_list_from_iterable)

# The "append" method adds singular elements to the list:
my_list_for_append = list()
my_list_for_append.append("Dogs")
my_list_for_append.append("Cats")
my_list_for_append.append("Elephants")
print("A list created using multiple appends:", my_list_for_append)

# Lists can be nested into each other, i.e. lists can contain any number of
#  other lists:

my_list_for_nesting = list()
my_list_for_nesting.append("Just one string")  # add a string to the list
my_list_for_nesting.append([1, 2, 3])  # add a list of integers to the list
my_list_for_nesting.append(["One", "Two", "Three"])  # add a list of strings to the list
my_list_for_nesting.append([[True], [True, True], [True, True, True]])  # add a list of lists to the list

print("My complicated nested list looks like this:", my_list_for_nesting)

# Nested lists can be declared explicitly:
my_list_for_nesting2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("A list of lists (looks like a matrix):", my_list_for_nesting2)

# Multiplication of lists with integers is also possible,
#  which produces as many concatenations of the list to itself,
#  as the integer we are multiplying with:
print("The list [1, 2] multiplied by 3:", 3 * [1, 2])  # will print [1, 2, 1, 2, 1, 2]

# We can use the "in" syntax to check for an element containment:
print("1 is contained in [1, 2]!" if 1 in [1, 2] else "1 is NOT contained in [1, 2]!")
print("3 is contained in [1, 2]!" if 3 in [1, 2] else "3 is NOT contained in [1, 2]!")

# We can index and slice a list using the already learned syntax:

my_list_to_slice = ["1", 2, True, "Ducks", [123, 321], 3.1415, [789, 987, 10], 2.7182]
print("Using the list", my_list_to_slice, "for indexing and slicing...")

print("\tThe fifth element:", my_list_to_slice[4])
print("\tThe last element:", my_list_to_slice[-1])
print("\tA slice:", my_list_to_slice[2:5])
print("\tA slice with steps:", my_list_to_slice[1:6:2])
print("\tA slice of a sublist:", my_list_to_slice[-2][0:2])

# The "extend" method on lists appends more than one element to the list:

my_list_to_extend = [1, 2, [], 1.71]
my_list_to_extend.extend(["1", "2", "3"])  # notice, that the argument is also a list!

print("My list, extended:", my_list_to_extend)

# The "extend" method is equivalent to the += operator:
my_list_to_extend = [1, 2, [], 1.71]
my_list_to_extend += ["1", "2", "3"]

print("My list, extended with += (should be the same):", my_list_to_extend)

# The "extend" method (and also +=) accepts any kind of iterable (like strings for example).
# It adds these elements one-by-one to the list that is to be extended.
my_list_to_extend.extend("characters")
print("My list, further extended with characters:", my_list_to_extend)

# Using the previous syntaxes, it is possible to add elements to lists
#  through many ways:

my_boring_list = list()
my_boring_list += ["w"]
my_boring_list.append("w")
my_boring_list.extend("w")
my_boring_list.extend(["w"])

print("\"w\" characters, added through different ways to my list:", my_boring_list)

# The "index" method of a list finds the index of an element inside the list.
# If it occurs multiple times, then it finds the index of the first occurrence:

structure_levels = ["atom", "residue", "chain", "chain", "model", "structure"]
index_of_residue = structure_levels.index("residue")
index_of_chain = structure_levels.index("chain")
print("I have the following list:", structure_levels)
print("\tThe index of the word \"residue\" is:", index_of_residue)
print("\tThe (first) index of the word \"chain\" is:", index_of_chain)

# If an item is not present inside a list, the "index" method will cause an exception.
# If you uncomment the following line, you can check it out yourself:
# index_of_dogs = structure_levels.index("dogs")

# Throwing/raising exceptions can be done manually, using the following syntax:

if "d" not in [1, 2, 3, "d"]:
    raise Exception("The character is not in the list!")  # this will stop the program with an error

# This can be used to check for the existence of an element inside a list and
#  stop the program if it is or is not present.

# The "pop" and "remove" methods both remove elements from the list.
# With the "pop" method we have to specify the index of the element.
# The "pop" method also returns the value, that we just removed from the list.

my_list_to_shrink = [1, 2, 3, "d", [98, 97], None]
print("My list before shrinking it...:", my_list_to_shrink)

my_list_to_shrink.pop(2)  # removes the third element
my_none_value = my_list_to_shrink.pop(-1)  # removes the last element from the list and stores the removed value
print("My list after shrinking it:", my_list_to_shrink)

# In the "remove" method we have to specify the value of the element
#  we want to remove:
my_list_to_shrink.remove(1)
my_list_to_shrink.remove("d")
print("My list, shrunken even further:", my_list_to_shrink)

# We can sort our list depending on the values it contains.
# There are two functions we can use for this:
#  - the "sorted" function, which creates a new, sorted version of our list and returns it
#  - the "sort" method on lists, which sorts in-place and returns None

my_list_to_sort = [4.5, 3.7, 66.5, 34., 100.75]
print("My list, before sorting:", my_list_to_sort)

my_sorted_list = sorted(my_list_to_sort)  # "sorted" returns a new, sorted list, which is stored in a variable
print("My new, sorted list:", my_sorted_list, "while the old one is:", my_list_to_sort)

my_nothing = my_list_to_sort.sort()  # the "sort" method modifies the variable in-place and doesn't return anything
print("The method \"sort\" returned:", my_nothing, "while the old list became:", my_list_to_sort)

print("The two sorted lists are the same:", my_sorted_list == my_list_to_sort)
