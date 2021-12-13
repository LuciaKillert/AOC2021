import sys
with open(sys.argv[1], "r") as f:
    inp = f.readlines()

arr = []
f = False
folds = []

for i in inp:
    if f:
        x,y,z = i.split()
        x,y = z.strip().split("=")
        folds.append((x, int(y)))
    elif i != "\n":
        x, y = i.strip().split(",")
        arr.append((int(x), int(y)))
    else:
        f = True

def solve(arr):
    for i, fold in enumerate(folds):
        line = fold[1]
        if fold[0] == "x":
            for j in range(len(arr)):
                point = arr[j]
                if point[0] > line:
                    newX = line - (point[0] - line)
                    arr[j] = (newX, point[1])
        if fold[0] == "y":
            for j in range(len(arr)):
                point = arr[j]
                if point[1] > line:
                    newY = line - (point[1] - line)
                    arr[j] = (point[0], newY)
        arr = list(set(arr))
        if i == 0:
            print(len(arr))
    minX, maxX, minY, maxY = findArrSize(arr)
    X = maxX - minX
    Y = maxY - minY
    ret = [[" " for x in range(X+1)] for x in range(Y+1)]
    for k in arr:
        ret[k[1]-minY][k[0]-minX] = "#"
    for k in ret:
        print(k)

def findArrSize(arr):
    minX = 100
    minY = 100
    maxX = 0
    maxY = 0
    for k in arr:
        if k[0] > maxX:
            maxX = k[0]
        if k[0] < minX:
            minX = k[0]
        if k[1] > maxY:
            maxY = k[1]
        if k[1] < minY:
            minY = k[1]
    return minX, maxX, minY, maxY

solve(arr)
