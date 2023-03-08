# Lists are able to collect multiple objects into one single object.
# Empty lists can be created in the following ways:

my_list1 = list()
my_list2 = []

# Both of these result in empty lists.

# We can add items to these empty lists with the "append" method:

my_list1.append("First element")
my_list1.append("Second element")
my_list1.append("Something else...")

print("My list contains the following elements:", my_list1)

# To create a non-empty list "in situ", we can use the following syntax:

non_empty_list = ["1", 2, 3.0]  # a three element list, containing different types

# We can extend existing lists with another list:

my_list1.extend([10, 43])  # This adds two new elements to "my_list1".
my_list1.extend(non_empty_list)  # This adds three new elements to "my_list1".

print("My list grew and it looks like this now:", my_list1)
# "my_list1" is now: ["First element", "Second element", "Something else...", 10, 43, "1", 2, 3.0]

# With indexing, we can access elements of a list at specific indices:

print("The fifth element is:", my_list1[4])
print("The fourth element squared is:", my_list1[3] ** 2)

# We can even take slices of lists, like in case of strings:

print("This is a 2:5 slice of my list:", my_list1[2:5])
