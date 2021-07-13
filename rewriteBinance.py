binance = open("Binance_1h.csv", 'r').readlines()[1:]
newfile = open("Binanceproper.csv", 'w')

for line in binance:
    if ".0" in line.split()[0]:
        newfile.write(line.replace(".0", "", 1))
    else:
        line = line.split(',')
        line[0] = line[0][:-3]
        newfile.write(",".join(line))
