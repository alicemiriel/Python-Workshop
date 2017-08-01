from task3_readPDB import read_pdb_file
from math import sqrt

def get_distance (a1, a2):
    coord_s1 = ((float(a1[30:38].strip()), float(a1[38:45].strip()), float(a1[46:54].strip())))
    coord_s2 = ((float(a2[30:38].strip()), float(a2[38:45].strip()), float(a2[46:54].strip())))
    return sqrt((coord_s1[0] - coord_s2[0]) ** 2 + (coord_s1[1] - coord_s2[1]) ** 2 + (coord_s1[2] - coord_s2[2]) ** 2)

if __name__ == '__main__':
    atoms_lig = read_pdb_file("C:\\development\\workdir\\afterSplit\\%s" % ('0a_lig.pdb'))
    atoms_rec = read_pdb_file("C:\\development\\workdir\\afterSplit\\%s" % ('0a_rec.pdb'))
    print(round(get_distance(atoms_rec[0],atoms_lig[0]),3))
    print("%.3f"%get_distance(atoms_rec[0],atoms_lig[0]))

