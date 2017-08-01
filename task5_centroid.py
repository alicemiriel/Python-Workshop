import argparse
#import sys
from task3_readPDB import read_pdb_file

def get_centroid (s):
    x = 0.0
    y = 0.0
    z = 0.0
    for i in range(0, len(s)):
        x += s[i][0]
        y += s[i][1]
        z += s[i][2]
    x /= float(len(s))
    y /= float(len(s))
    z /= float(len(s))
    return round(x, 3), round(y, 3), round(z, 3)


if __name__ == '__main__':
    #file_name = sys.argv[1]
    a1 = read_pdb_file("C:\\development\\workdir\\afterSplit\\%s" % ('0a_lig.pdb'))
    #a1 = read_pdb_file("C:\\development\\workdir\\afterSplit\\%s" % (file_name))

    #parser = argparse.ArgumentParser(description='Calculate centroid.')
    #parser.add_argument('filename', help='a name of PDB file')
    #args = parser.parse_args()
    #a1 = read_pdb_file("C:\\development\\workdir\\afterSplit\\%s" % (args.filename))

    coordinates = []
    for line in a1:
        coordinates.append(((float(line[30:38]), float(line[38:45]), float(line[46:54]))))
centroid_coordinates = get_centroid(coordinates)
print(centroid_coordinates)