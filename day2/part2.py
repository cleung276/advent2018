f = open("input.txt")
lol = []
dcp = 0
for x in range(250):
    d = 0
    ts = f.readline().strip("\n")
    lol.append(ts)
    for c in range(x):
        for i in range(len(lol[c])):
            if lol[c][i] != ts[i]:
                d += 1
                dcp = i
            if d > 1:
                d = 0
                break
        if d == 1:
            ns = lol[c].replace(lol[c][dcp], "", 1)
            print(ns)
            print(lol[c])
            print(ts)
