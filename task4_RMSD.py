from math import sqrt
from task3_readPDB import read_pdb_file

def get_rmsd (s1,s2):
    """
    calculate rmds of two sets of coordinates
    :param s1: coordinates of structure 1
    :type list of tuples of x,y,z coordinates
    :param s2: coordinate of structure 2
    :type list of tuples x,y,z coordinates
    :return: rmsd
    """
    if len(s1)>0:
        rmsd = 0.0
        for i in range(len(s1)):
            rmsd += ((s1[i][0]-s2[i][0])**2)+((s1[i][1]-s2[i][1])**2)+((s1[i][2]-s2[i][2])**2)
        rmsd=sqrt(rmsd/float(len(s1)))
        return rmsd
    else:
        return "Error, no coordinates"

if __name__ == '__main__':
    a1 = read_pdb_file("C:\\development\\workdir\\afterSplit\\%s" % ('100a_lig.pdb'))
    a2 = read_pdb_file("C:\\development\\workdir\\afterSplit\\%s" % ('100d_lig.pdb'))
    print(a1,a2)

    coordinates_of_s1=[]
    coordinates_of_s2=[]

    for line in a1:
        coordinates_of_s1.append ((float(line[30:38]), float(line[38:45]), float(line[46:54])))
    for line in a2:
        coordinates_of_s2.append((float(line[30:38]), float(line[38:45]), float(line[46:54])))

    rmsd_of_s1s2 = get_rmsd(coordinates_of_s1,coordinates_of_s2)
    print(rmsd_of_s1s2)