readfile = open("elonmuskutf8.csv").readlines()
newfile = open("elonmuskPruned.csv", 'w')
newfile.write(readfile[0])

i = 1

while i < len(readfile):
    try:
        int(readfile[i][0:9])
        newfile.write(readfile[i])
        i += 1
    except:
        print(readfile[i])
        i += 1
