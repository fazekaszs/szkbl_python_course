# Homeworks for lessons 7, 8, and 9

This homework set is supposed to help you practice the material learned on
lessons 7, 8, and 9 __except__ for the parts with `list`s! During solving these
homeworks __do not use__ lists, since these tasks aim to teach you algorithmic
concepts, which would be much easier to solve with `list` objects (and hence,
you wouldn't learn as much). Have fun!

## Homework 1

A string sould be provided by the user, which contains positive numbers, separated by
commas. These numbers are __not necessarily__ whole numbers, thus the string
may contain dots denoting the start of the fractional parts. Your job is to find
the smallest number in this string. Remember: __do not use__ lists for this task!

Here is an example:
```text
Give me the numbers: 2,3,12.45,1.23,92,0.2,134.1
The smallest number is: 0.2
```

If you want a (slightly) more challanging task, try to implement the following
functionalities into the script:
- the script shoud tolerate spaces in the user input, 
- the script should tolerate a trailing comma

Here is the previous example with the more "complicated" input:
```text
Give me the numbers: 2,  3,12.45  ,1.2 3  ,92 , 0.2,  13 4.1
The smallest number is: 0.2
```

(Be aware, that `13 4.1` is 134.1, since our separators are commas, NOT spaces!)

## Homework 2

Query a user for two text inputs! The first input should be a string of character
and number pairs! The characters and numbers should be separated by colons, while
the pairs should be separated by commas. This input should look something like
this:
```text
Give me the character+number pairs: A:0.2,B:13.5,C:55.7,D:100
```
So in this case the caracters are `A, B, C` and `D`, while the numbers are
0.2, 13.5, 55.7, and 100. Obviously, the characters given cannot be `:` or `,` 
characters.

The second input is a string constructed from the caracters specified above. So
and example for the full input is like this: 
```text
Give me the character+number pairs: A:0.2,B:13.5,C:55.7,D:100
Give me a string of characters: ABDBAC
```

Your job is to return the sum of the numbers belonging to the specified characters.
In this case this is A + B + D + B + A + C, meaning 0.2 + 13.5 + 100 + 
13.5 + 0.2 + 55.7 = 183.1. The output should look like this:
```text
Give me the character+number pairs: A:0.2,B:13.5,C:55.7,D:100
Give me a string of characters: ABDBAC
The sum is: 183.1
```

## Homework 3

Again, query the user for an input! This input should contain only "+" or "-"
characters. Next, detect the places inside the string, where the plus and minus
signs meet (so, where a "+-" or "-+" motif is present). Then, write one dot between
the first occurrence, two dots between the second occurrence, etc... This way, the
following string: `++-++++---+` becomes `++.-..++++...---....+`. Then, calculate the
remainder when the length of the long string is divided by the length of the original
one. If the remainder is even, add a "+" sign at the end of the "dotless" string,
if it's odd, add a "-" sing to it. Repeat this process 10 times and print out the
"dotless" strings. Try to use the `zip` iterator when solving this task!
(Hint: you can use `zip` together with string slices.)
You should see something like this:

```text
Give me plus and minus signs: ++-++++---+
Round 1:
The new signs are: ++-++++---++
Round 2:
The new signs are: ++-++++---+++
Round 3:
The new signs are: ++-++++---++++
Round 4:
The new signs are: ++-++++---+++++
Round 5:
The new signs are: ++-++++---++++++
Round 6:
The new signs are: ++-++++---+++++++
Round 7:
The new signs are: ++-++++---++++++++
Round 8:
The new signs are: ++-++++---+++++++++
Round 9:
The new signs are: ++-++++---++++++++++
Round 10:
The new signs are: ++-++++---+++++++++++
```

Or in case of a more "exciting" input:

```text
Give me plus and minus signs: ++-++++---+-
Round 1:
The new signs are: ++-++++---+--
Round 2:
The new signs are: ++-++++---+--+
Round 3:
The new signs are: ++-++++---+--+-
Round 4:
The new signs are: ++-++++---+--+--
Round 5:
The new signs are: ++-++++---+--+--+
Round 6:
The new signs are: ++-++++---+--+--++
Round 7:
The new signs are: ++-++++---+--+--+++
Round 8:
The new signs are: ++-++++---+--+--+++-
Round 9:
The new signs are: ++-++++---+--+--+++--
Round 10:
The new signs are: ++-++++---+--+--+++---
```
