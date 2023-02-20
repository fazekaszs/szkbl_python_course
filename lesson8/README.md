# The Bubble-sort algorithm

## Outline
- Our goal is to sort a list of numbers given by the user.
- The sorted list is ascending.
- __NOTE__: we haven't learned about `list` yet, so we cannot use it!
- User input format requirements:
  - the numbers are separated __only__ by commas
  - the numbers must be integers
  - a trailing comma at the end of the user input has to be tolerated
  - no spaces are allowed in the user input 

## The algorithm
1. Query the user for the input! The input must be a list of numbers in a given format.
2. Compare the number at index `i` with the number at index `i+1`, and
   if the former one is bigger, swap the two numbers. Do this for every
   __even__ `i`!
3. Compare the number at index `i` with the number at index `i+1`, and
   if the former one is bigger, swap the two numbers. Do this for every
   __odd__ `i`!
4. Repeat steps 2. and 3. until no swaps happen anymore! When this happens,
   the algorithm converged, the numbers are in increasing order,
   and we can stop.

## Step 1 - implementing the "even index" swaps
- We have to use strings as growable types, since lists are not available for us yet.
- We can only iterate through strings character-wise and "do things" with the
  currently available character.
- The variables needed are the following:
  - we need a string buffer for the `i`th number &rarr; `snumber1`, initially empty
  - we need a string buffer for the `i+1`th number &rarr; `snumber2`, initially empty
  - we need to know which number we are building currently &rarr; `build_snumber1`.
    This is a boolean (i.e. either `True` or `False`). Initially, this is `True`.
  - we need a result string, that will contain the sorted number list at the end &rarr; 
    `new_number_list`, initially empty
- The steps are the following:
  1. we start building `snumber1`, character by character
  2. when we encounter a comma character, we flip the `build_snumber1` switch
     to `False`
  3. we start building `snumber2`, character by character
  4. when we encounter a comma character, we convert the string buffers
     to integers, compare them, swap them if necessary, build the current part of
     `new_number_list` string accordingly, empty the buffers,
     and flip the `build_snumber1` switch to `True` again
  5. repeat steps 1. ... 4. until the end of the user input
  6. if `snumber2` is not empty in the end, do step 4. again
  7. if `snumber1` is not empty in the end, add it to `new_number_list`
- If everything is implemented correctly, the script will result in the
  second point of the algorithm specification (see above)

## Step 2 - implementing the "odd index" swaps
- Almost identical to "Step 1", but we start with `build_snumber1 = False`.
- When we first finish building `snumber2`, `snumber1` will be empty! In this
  case we have to simply add `snumber2` to `new_number_list`, flip the
  `build_snumber1` switch to `True`, and continue the loop without any comparisons.
- The post-processing steps ("Step 1/vi" and "Step 1/vii") are the same.

## Full Bubble-sort
- Step 1 and 2 are used alternally in a main loop, until the maximal
  iteration number is reached, or until no swaps are performed.
- The boolean variable `swap_happened` keeps track of whether a 
  swap is performed or not.