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
    atoms = read_pdb_file("C:\\development\\sources\\1KXP_dockedPoses\\%s" % ('0a.pdb'))
    seq_A = 0
    seq_B = 0
    coord = []
    for line in atoms:
        spline = line.split()
        if spline[2] == 'CA' and spline[4] == 'B':
            coord.append(line)
    print(coord)
    coordinates =[]
    for line in coord:
        coordinates.append(((float(line[30:38]), float(line[38:45]), float(line[46:54]))))
    print(coordinates)

    centroid_coordinates = get_centroid(coordinates)
    print(centroid_coordinates)