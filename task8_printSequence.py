from task3_readPDB import read_pdb_file

res3lett = ['GLY', 'ALA', 'LEU', 'ILE', 'VAL', 'ASP', 'GLU', 'ASN', 'GLN', 'ARG', 'LYS', 'SER', 'THR', 'CYS', 'MET', 'PHE', 'TYR', 'HIS', 'TRP', 'PRO']
res1lett = ['G',   'A',   'L',   'I',   'V',   'D',   'E',   'N',   'Q',   'R',   'K',   'S',   'T',   'C',   'M',   'F',   'Y',   'H',   'W',   'P']

for line in atoms:
    if line[13:16] == 'CA' and line[4] =="A":

    if line [13:16] == 'CA' and line[4] == 'B':



def get_sequence (atoms):
    residues = []
    seq_A = ""
    seq_B = ""
    for line in atoms:
        if line[17:26] not in residues:
            residues.append(line[17:26])
    for res in residues:
        index = res3lett.index(res[0:3])
        if res[4] == "A" :
            seq_A += str(res1lett[index])
        if res[4] == "B" :
            seq_B += str(res1lett[index])
        if index == -1:
            return "%s sequence does not exist" % (res [0:3])
    final_seq_A = ""
    final_seq_B = ""
    for i in range(0,len(seq_A)):
        if i>0 and i%80 == 0:
            final_seq_A += '\n'
        final_seq_A += seq_A[i]
    for i in range (0, len(seq_B)):
        if i>0 and i%80 == 0:
            final_seq_B += '\n'
        final_seq_B += seq_B[i]
    return "%s\n\n%s" % (final_seq_A,final_seq_B)

if __name__ == '__main__':
    atoms = read_pdb_file("C:\\development\\sources\\1KXP_dockedPoses\\%s" % ('0a.pdb'))
    print(get_sequence(atoms))