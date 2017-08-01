def classification (irmsd, lmrsd, fnat):
    if fnat < 0.1 or lmrsd > 10.0 and irmsd > 4.0:
        return "incorrect"
    elif (fnat >= 0.3 and lmrsd > 5.0 and irmsd > 2.0):
        return "acceptable"
    elif(fnat >= 0.1 and fnat < 0.3) and (lmrsd <= 10.0 or irmsd <= 4.0):
        return "acceptable"
    elif (fnat >= 0.5 and lmrsd > 1.0 and irmsd> 1.0):
        return "medium"
    elif (fnat >= 0.3 and fnat < 0.5) and lmrsd <= 5.0 or irmsd <= 2.0:
        return "medium"
    elif (fnat >= 0.5 and lmrsd <= 1.0 and irmsd <= 1.0):
        return "high"
    else:
        return "No category"

number_to_structure ={}
map_file = open("C:\\development\\sources\\task0_mapfile.txt").readlines()
for line in map_file:
    spline = line.strip().split()
    number = spline[1]
    name = spline[0].replace("1kxp_", "").replace("la", "a").replace("lb", "b").replace("lc", "c").replace("ld", "d")
    number_to_structure[number] = name

properties_file = open("C:\\development\\sources\\task0_properties.txt").readlines()
output = open("C:\\development\\workdir\\task0_output.txt", "w")
for line in properties_file:
    spline = line.split()
    number = spline[1]
    irmsd = float(spline[3])
    lmrsd = float(spline[4])
    fnat = float(spline[5])
    property = classification(irmsd,lmrsd,fnat)
    output.write("%s\t%s\n" % (number_to_structure[number],property))

output.close()