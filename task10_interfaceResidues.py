from task3_readPDB import read_pdb_file
from task9_findDistance import get_distance


def get_interface_residues(a1, a2):
    interface = []
    for line1 in a1:
        for line2 in a2:
            distance = get_distance(line1,line2)
            if distance <= 10.0:
                interaction = "%s WITH %s" % (line1[17:26], line2[17:26])
                if interaction not in interface:
                    interface.append(interaction)
    return interface

if __name__ == '__main__':
    a2 = read_pdb_file("C:\\development\\workdir\\afterSplit\\%s" % '0a_lig.pdb')
    a1 = read_pdb_file("C:\\development\\workdir\\afterSplit\\%s" % '0a_rec.pdb')

    interfaces2 = get_interface_residues(a1, a2)
    print(interfaces2)
    print(len(interfaces2))