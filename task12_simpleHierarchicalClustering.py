from task3_readPDB import read_pdb_file
from task4_RMSD import get_rmsd


main_directory = ("C:\\development")
directory = ("C:\\development\\sources")

energy_file = open("%s\\1KXP_energies_reduced.txt" % directory).readlines()
energies = []
clusters =[]
threshold = 3.0
for line in energy_file:
    spline = line.split()
    energies.append((spline[0], spline[1]))
    energies.sort(key=lambda x: x[1])
print(energies)

structures = read_pdb_file("C:\\development\\workdir\\afterSplit\\%s" % (energies[0]))
for i in energies:
    if get_rmsd(energies[0][i], energies[0][i+1]) <3:
        clusters.append()

coordinates_of_s1 = []
for line in structures:
    coordinates_of_s1.append((float(line[30:38]), float(line[38:45]), float(line[46:54])))
