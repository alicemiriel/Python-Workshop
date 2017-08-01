import os

directory = ("C:\\development\\sources\\1KXP_dockedPoses")
list = os.listdir(directory)
output = open("%s\\filelist.txt" % directory, "w")
print(list)

for file in list:
    if "pdb" in file:
        output.write("%s\n" % file)
output.close()
