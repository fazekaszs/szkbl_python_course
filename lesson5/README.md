# Summary for the fifth lesson

## Bits and pieces
- how to __delete variables__ using the `del` keyword
- multiple variable declarations with one line
- a function with multiple return values: the `divmod` function
- save time without calling unnecessarily redundant code

## Indexing and slicing strings
- what is indexing good for?
- what is the syntax for indexing? Using the `var[idx]` syntax.
- how to count with indexing? Starting from 0, going up to `len(var)`.
- indexing out causes an error
- negative indices
- slices: getting out substrings with the `var[idx1:idx2]` syntax. Inclusion and exclusion of bounds.
- leaving out the starting index and/or the ending index. Formats with `var[:idx2]`, `var[idx1:]` and `var[:]`.
- slicing with step-sizes. Formats with `var[idx1:idx2:step_size]` and `var[::]`.
- negative step-sizes. Reversing the string with `var[::-1]`.
- string slices are just strings. Calling methods on slices and slicing string-slices.