import sys
with open(sys.argv[1], "r") as f:
    arr = [x for x in f.readlines()]

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
        if c[0] == c[2]:
            x = c[0]
            if c[1] < c[3]:
                y1 = c[1]
                y2 = c[3]
            else:
                y1 = c[3]
                y2 = c[1]
            for i in range(y1, y2+1):
                field[i][x] += 1
        elif c[1] == c[3]:
            y = c[1]
            if c[0] < c[2]:
                x1 = c[0]
                x2 = c[2]
            else:
                x1 = c[2]
                x2 = c[0]
            for i in range(x1, x2+1):
                field[y][i] += 1
        elif part2:
            x1 = c[0]
            x2 = c[2]
            if c[0] < c[2]:
                xi = 1 
            else:
                xi = -1
            y1 = c[1]
            y2 = c[3]
            if c[1] < c[3]:
                yi = 1
            else:
                yi = -1
            for i in range(0,abs(x2+xi - x1)):
                field[y1+(i*yi)][x1+(i*xi)] += 1



    res = 0
    for f in field:
        for g in f:
            if g > 1:
                res += 1

    print(res)

solve(False)
solve(True)
