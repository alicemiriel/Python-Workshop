def read_pdb_file(path):
    """
    :param path:
    :return:
    """
    atom_lines = []
    input_file = open(path).readlines()
    for line in input_file:
        if line[0:4] == 'ATOM':
            atom_lines.append(line[:-1])
    return atom_lines

if __name__ == '__main__':
    atoms = read_pdb_file("C:\\development\\workdir\\afterSplit\\%s" % ('0a_lig.pdb'))
    print(atoms)

