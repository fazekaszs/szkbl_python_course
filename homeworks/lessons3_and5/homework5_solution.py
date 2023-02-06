sequence_long = input("Give me a long amino acid sequence: ")
sequence_short = input("Give me a short amino acid sequence: ")

answer1 = sequence_short in sequence_long and sequence_short[::-1] in sequence_long
print("First sub-problem:", answer1)

n_of_occ = sequence_long.count(sequence_short)
answer2 = n_of_occ > 1 and n_of_occ < 6
answer2 = answer2 or sequence_short == sequence_long[:len(sequence_short)]
print("Second sub-problem:", answer2)

first_half = sequence_short[:len(sequence_short) // 2]
second_half = sequence_short[len(sequence_short) // 2:]
answer3 = first_half in sequence_long[1::2] or second_half in sequence_long[1::2]
print("Third sub-problem:", answer3)
