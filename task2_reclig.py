import os

main_directory = ("C:\\development")
directory = ("C:\\development\\sources\\1KXP_dockedPoses")
receptor = ["A"]
ligand = ["B"]

input= open("%s\\filelist.txt" % directory).readlines()
os.system ("mkdir %s\\workdir\\afterSplit"%main_directory)

for file_name in input:
    file_name = file_name.strip()
    pdb_file = open('%s\\sources\\1KXP_dockedPoses\\%s' % (main_directory, file_name))
    receptor_file_name = '%s_rec.pdb' % file_name[0:-4]
    ligand_file_name = '%s_lig.pdb' % file_name[0:-4]
    receptor_file = open('%s\\workdir\\afterSplit\\%s' % (main_directory, receptor_file_name), 'w')
    ligand_file = open('%s\\workdir\\afterSplit\\%s' % (main_directory, ligand_file_name), 'w')
    for line in pdb_file:
        if line[0:4] == 'ATOM' and line[21] in receptor:
            receptor_file.write(line)
        elif line[0:4] == 'ATOM' and line[21] in ligand:
            ligand_file.write(line)
    receptor_file.write('TER\n')
    receptor_file.close()
    ligand_file.write('TER\n')
    ligand_file.close()