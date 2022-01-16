f = open("input.txt")
lol = []
d = 0
t = 0
tc = 0
dc = 0
for x in range(250):
    i = f.readline()
    for k in i:
        lol.append(k)
    for j in i:
        if lol.count(j) == 3 and tc < 1:
            t += 1
            lol.remove(j)
            lol.remove(j)
            lol.remove(j)
            print(j)
            tc += 1
        if lol.count(j) == 2 and dc < 1:
            d += 1
            lol.remove(j)
            lol.remove(j)
            print(j)
            dc += 1
    lol = []
    dc = 0
    tc = 0
    print(d, t)
print(d*t)