# User queries
pdb_line1 = input("Give me the first PDB line:\n")
pdb_line2 = input("Give me the second PDB line:\n")

# Extracting the x, y, z coordinates for the first atom
x1 = float(pdb_line1[30:38])
y1 = float(pdb_line1[38:46])
z1 = float(pdb_line1[46:54])

# Extracting the x, y, z coordinates for the second atom
x2 = float(pdb_line2[30:38])
y2 = float(pdb_line2[38:46])
z2 = float(pdb_line2[46:54])

# Distance calculation
distance = 0
distance += (x1 - x2) ** 2
distance += (y1 - y2) ** 2
distance += (z1 - z2) ** 2
distance **= 0.5

# Normal output
print("The distance between the atoms is", distance, "angströms.")

# Extracting the atom properties for the first atom
chain1 = pdb_line1[21]
resi_name1 = pdb_line1[17:20].strip()
resi_seq1 = pdb_line1[22:26].strip()
atom_name1 = pdb_line1[12:16].strip()

atom_id1 = chain1 + "/" + resi_name1 + "-" + resi_seq1 + "/" + atom_name1

# Extracting the atom properties for the second atom
chain2 = pdb_line2[21]
resi_name2 = pdb_line2[17:20].strip()
resi_seq2 = pdb_line2[22:26].strip()
atom_name2 = pdb_line2[12:16].strip()

atom_id2 = chain2 + "/" + resi_name2 + "-" + resi_seq2 + "/" + atom_name2

distance = round(distance, 4)

print("More precisely, the distance between atom", atom_id1, "and atom", atom_id2, "is", distance, "angströms.")
