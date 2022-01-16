f = open("input.txt", "r")
flvl = 0
for x in range(965):
    x = f.readline()
    x = x.strip("\n")
    if x[0] == "-":
        flvl -= int(x[1:])
    else:
        flvl += int(x[1:])
print(flvl)