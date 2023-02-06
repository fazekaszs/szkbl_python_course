sequence = input("Give me the amino acid sequence: ")

# Counting the aromatics.
aromatics = sequence.count("W")
aromatics += sequence.count("Y")
aromatics += sequence.count("F")
aromatics += sequence.count("H")

# These can either be 0/1 or 1/0. We will use these to
# create the output string.
evenness = (aromatics + 1) % 2
oddness = aromatics % 2

# Counting the charged residues.
charged = sequence.count("K")
charged += sequence.count("R")
charged += sequence.count("E")
charged += sequence.count("D")

# Stringify the charged count, so we can use it later
# during the output string generation.
charged = str(charged)

# The sequence without prolines and glycines.
sequence_no_pg = sequence.replace("P", "").replace("G", "")

# If evenness is 1, then oddness is 0. In this case, we will
# multiply charged (the string) with 1 and the PG-less sequence
# with 0. This way, result_str will be equal to charged. In the
# opposite case (evenness is 0, oddness is 1) result_str will
# be the PG-less sequence.
result_str = evenness * charged + oddness * sequence_no_pg

print("The result is this:", result_str)
