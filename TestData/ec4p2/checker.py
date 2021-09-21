d = open("data.in", "r")
g = open("data.out", "r")

n = int(d.readline())
da = list(map(int, d.readline().split()))
s = g.readline()

ga = None
try:
    ga = list(map(int, s.split()))
except:
    ga = None

dif = False
for i in range(1, n):
    if da[i] != da[0]:
        dif = True
        break

if (not dif) and s.strip() == "none":
    print("AC")
elif len(ga) == n:
    f = False
    for i in range(n):
        if da[i] != ga[i]:
            f = True
            break

    if f:
        da.sort()
        ga.sort()

        good = True
        for i in range(n):
            if da[i] != ga[i]:
                good = False
                break
        
        if good:
            print("AC")