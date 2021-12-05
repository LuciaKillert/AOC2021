import sys
with open(sys.argv[1], "r") as f:
    arr = f.readlines()

coors = []
for a in arr:
    x, y = a.split(" -> ")
    coor = x.split(",") + y.split(",")
    coors.append(list(map(lambda x: int(x),coor)))

maxi = 0
for c in coors:
    if max(c) > maxi:
        maxi = max(c)

def solve(part2):
    field = [[0 for x in range(0,maxi+1)] for x in range(0,maxi+1)]

    for c in coors:
        x1 = c[0]
        x2 = c[2]
        y1 = c[1]
        y2 = c[3]
        dy = 1 if y1 < y2 else -1 
        dx = 1 if x1 < x2 else -1
        if x1 == x2:
            for i in range(y1, y2+dy, dy):
                field[i][x1] += 1
        elif y1 == y2:
            for i in range(x1, x2+dx, dx):
                field[y1][i] += 1
        elif part2:
            for i in range(0,abs(x2+dx - x1)):
                field[y1+(i*dy)][x1+(i*dx)] += 1

    res = 0
    for f in field:
        for g in f:
            if g > 1:
                res += 1
    print(res)

solve(False)
solve(True)
