

infile = open("Elontweets/2021.csv", 'r', encoding='utf8').readlines()
outfile = open("2021UTF8.csv", 'w')
exceptioncount = 0

for line in infile:
    newline = []
    for symbol in line:
        try:
            print(symbol, end="")
            newline.append(symbol)
        except Exception:
            exceptioncount += 1
            print(exceptioncount, end="")
    outfile.write("".join(newline))
print(f"\n\n")
print(exceptioncount)
