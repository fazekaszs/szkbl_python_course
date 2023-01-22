# Homeworks for lesson 3 and 5

This homework builds on the things learned on lesson 4 and 5, as well as things
learned on the lessons before! Don't be afraid to check out the `README.md` files,
the scripts, or even to search on the internet for sub-solutions. However, always
try to ponder on the questions for a little before you peak inside these 
helping materials. Don't try to find the full solution to these questions, but rather
try to piece them together from smaller parts.

## Homework 1

A Hungarian archer fires an arrow forward from the back of a moving horse.
Query the user for both the velocity of the arrow and the horse in miles per hour.
Your job will be to calculate the new velocity of the arrow, from a non-moving 
observer's point of view. However, since we, Hungarians are so good at firing arrows, 
and also our horses are really-really fast, we have to use relativistic corrections.
In Einstein's special relativity, velocities do not simply add up, but rather behave
in a way described by 
[this equation](https://en.wikipedia.org/wiki/Velocity-addition_formula#Special_relativity):

![velocity addition](https://wikimedia.org/api/rest_v1/media/math/render/svg/6eb3091ed58441a1f81b65cdc3911cc471084ee4)

where _v_ and _u\'_ are the horse's and the arrow's velocities, _c_ is the speed of
light, and _u_ is the velocity of the arrow from the non-moving observer's point of
view. For the calculation of _c_<sup>2</sup> use Python exponentiation! Also, for the
calculation of the final answer use in-place operators! Print out the final answer in
kilometers per hour! Print out the non-relativistic velocity addition answer too!

Here is an example for the program:

```text
Velocity of the horse (in mph): 10
Velocity of the arrow (in mph): 15
The observed velocity without corrections in km/h: 40.2335
The observed velocity with corrections in km/h: 40.23349999999998
```

or

```text
Velocity of the horse (in mph): 30000
Velocity of the arrow (in mph): 50000
The observed velocity without corrections in km/h: 128747.2
The observed velocity with corrections in km/h: 128747.19957058397
```

(That is one hell of a fast horse and arrow, if I say so myself.)

## Homework 2

Query the user for two string inputs! Both of these inputs should be `ATOM` lines from a PDB file.
The structure of a line like this is described
[here](https://www.wwpdb.org/documentation/file-format-content/format33/sect9.html#ATOM). What we will
use from these lines are the atom's x, y, and z coordinates. See the __Record Format__ section from the
link, how you can extract these numbers! Calculate the distance between these atoms and
print out the answer! You can simply open a PDB file using a simple text editor, like Notepad 
("Jegyzettömb") and copy out your favorite two atoms' lines!

__Important__: use a calculator to calculate the distance manually too, to check if the script's
answer is correct!

Example:

```text
Give me the first PDB line:
ATOM    307  CA  GLU A  42      18.100  15.145  39.281  1.00 21.49           C  
Give me the second PDB line:
ATOM    312  CD  GLU A  42      15.257  13.101  37.556  0.50 24.62           C  
The distance between the atoms is 3.9033588100506478 angströms.
```

Note the __newline__ characters after the colons! You should also try to incorporate it!

For a more advanced output excercise, also print out the atoms' chain, residue name, residue sequence number, 
and atom name! Also, we should probably round the answer to a more pleasant number of decimals.
Here is an example for this advanced output:

```text
Give me the first PDB line:
ATOM    307  CA  GLU A  42      18.100  15.145  39.281  1.00 21.49           C  
Give me the second PDB line:
ATOM    312  CD  GLU A  42      15.257  13.101  37.556  0.50 24.62           C  
The distance between atom A/GLU-42/CA and atom A/GLU-42/CD is 3.9034 angströms.
```

As a last resort, if you can't open a PDB file with a text editor, you can also use 
the sample PDB lines above for testing.

## Homework 3

Query an integer `i1` from the user! Flip the digits of the integer (`i1_reversed`) and 
write it behind the original one (creating `i2`). Now, calculate the remainder when we divide this 
new integer with the original (creating `rem1`).

Do this calculation again, but before writing the flipped digits behind the original int, 
replace every 9 with a 5 in it, and complete it with 1s from the front to get a 10-digit number 
(`i1_rev_complete`). After writing this behind the original int (getting `i3`) and getting 
the remainder again, print out both remainders.

Here are some examples:

```text
Give me an integer: 1395
The two remainders are 351 and 821
```

since the remainder for 13955931 / 1395 is 351, while for 13951111115531 / 1395 is 821.

Another example:

```text
Give me an integer: 919293
The two remainders are 392919 and 846571
```

## Homework 4

Query an amino acid sequence from the user. If there are an even number of aromatic residues
in the sequence, print out the number of charged residues, else print out the sequence without
glycines and prolines. __Important:__ do NOT use the `if`-`else` syntax (since we haven't learned
it yet)! Try to solve it in a different way, using only the things we have already learned 
(yes, it's possible).

Here are some examples:

```text
Give me the amino acid sequence: EEEAVRLYIQWLKEGGPSSGRPPPS
The result is this: 7
```

```text
Give me the amino acid sequence: EEEAVRLYIQWLKEGGPSSGRPPPW
The result is this: EEEAVRLYIQWLKESSRW
```

```text
Give me the amino acid sequence: EPERKAVIARGITAR
The result is this: 6
```

```text
Give me the amino acid sequence: EPERKAVIARGITARGATYA
The result is this: EERKAVIARITARATYA
```

## Homework 5

Query a long and a short amino acid sequence from the user! Print out
the values (`True` or `False`) for the following logical evaluations:
- the long sequence contains the short sequence, and also it's reverse
  sequence,
- the number of occurrences of the short sequence in the long one is between
  2 and 5 (both bounds including), or the long sequence starts with the short one 
  (don't use `startswith`, since we haven't learned it yet),
- if we leave out every character with an even index from the long sequence,
  the resulting sequence contains either the first half or the second half
  of the short sequence

Here are examples:

```text
Give me a long amino acid sequence: EEEAVRLYIQWLKEGGPSSGRPPPS
Give me a short amino acid sequence: IQWL
First sub-problem: False
Second sub-problem: False
Third sub-problem: False
```

```text
Give me a long amino acid sequence: EEEAVRLYIQWLKEGGPSSGRPPPS
Give me a short amino acid sequence: EEEA
First sub-problem: False
Second sub-problem: True
Third sub-problem: True
```

```text
Give me a long amino acid sequence: EEEAVRLYIQWLKEGGPSSGRPPPS
Give me a short amino acid sequence: EAKK
First sub-problem: False
Second sub-problem: False
Third sub-problem: True
```

```text
Give me a long amino acid sequence: EEEAVRLYIQWLKEGGPSSGRPPPS
Give me a short amino acid sequence: PP
First sub-problem: True
Second sub-problem: False
Third sub-problem: True
```