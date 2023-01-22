# Homeworks for lesson 1 and 2

__Remark__: it should be somewhat trivial, but every homework should be written using 
knowledge only obtained during the lesson(s) it is assined for. If you know more about 
Python than where we are currently at, and you use more "complicated"/"advanced" concepts,
then you are __not__ practicing the things we learned, but rather the things you already
know. I intend to formulate each homework so that they can be solved through methods we
practiced during the lesson(s). I'm not saying it is a forbidden thing to solve a problem
more than one way (on the contrary), but try solving the homeworks using the methods
outlined in the `README.md` files and scriptfiles first! Have fun!

## Homework 1

Ask the user for inputting her/his first and last name! ("Asking the user for input" is
called __querying__.) Then, print out the user's full name
- with the two names separated by a space,
- with the two names separated by a hyphen,
- with the two names separated by a semicolon.

In case of a good solution, you should see something like this:

```text
First name: Huba
Second name: Buba
Huba Buba
Huba-Buba
Huba;Buba
```

Try solving this homework two different ways:
- by storing the user's first and last name in variables and using these for each `print`
  (you can also try using `print` different ways i.e., solve string-concatenation through
  different means),
- by storing the user's first and last name in variables, creating a variable with the
  two names concatenated using a space, and then replacing the space character with the
  other characters ("-" and ";").

## Homework 2

Query a number from the user and write down that number as many times as the number itself!
Here are some examples:

```text
Give me a number: 5
55555
```

or

```text
Give me a number: 10
10101010101010101010
```

For a more complicated task, add a trailing character after each number-section, like this:

```text
Give me a number: 7
7@7@7@7@7@7@7@
```

or

```text
Give me a number: 12
12-12-12-12-12-12-12-12-12-12-12-12-
```

## Homework 3

Query the user for a whole number. Then, count the number of 2s (the __character__ "2") and
3s in that number. Divide the number of 3s with the number of 2s, round it __down__ to an
integer value and multiply the resulting integer with the original inputted integer. Print
out the result! You should see something like this:

```text
My number: 1333322
Result: 2666644
```

because 1333322 contains 4 3s and 2 2s, so 4/2 = 2, and 2 * 1333322 = 2666644. Another
example:

```text
My number: 32323333392
Result: 64646666784
```

because 32323333392 contains 7 3s and 3 2s, so 7/3 = 2.33, which is rounded down to 2, and
2 * 32323333392 = 64646666784.

## Homework 4

Query a string from the user. Remove the leading and trailing whitespaces from this string.
Then, add tilde ("~") characters to this string, so that A) it should be right justified and
B) it should span 30 characters. Use the resulting string again, now for centering
with percentage ("%") characters until 50 character spans. Use method chaining to achieve
this! Here are some samples:

```text
My input:   Hello Sir!   
%%%%%%%%%%~~~~~~~~~~~~~~~~~~~~Hello Sir!%%%%%%%%%%
```

or

```text
My input:      134Monkeys?----         
%%%%%%%%%%~~~~~~~~~~~~~~~134Monkeys?----%%%%%%%%%%
```

For a more complicated problem, you can try to ditch the `rjust` and `center` methods and
use only the `len` function.

## Homework 5

Query the birth-year of the user and of the user's dog and also the current year! Print the
ratio of their age currently and in 17 years! Use the numbers within a sentence and only print
3 decimal places at most! Samples:

```text
Current year: 2022
My birthyear: 1994
My dogs birthyear: 2017
You are 5.6 times older than your dog.
However, you will only be 2.045 times older in 17 years!
```