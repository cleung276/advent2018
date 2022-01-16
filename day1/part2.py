f = open("input.txt")
flvl = 0
lon = []
while True:
    x = f.readline()
    x = x.strip("\n")
    if x == "":
        f.seek(0)
        continue
    if x[0] == "-":
        flvl -= int(x[1:])
    else:
        flvl += int(x[1:])
    if flvl in lon:
        print(flvl)
        break
    else:
        lon.append(flvl)

