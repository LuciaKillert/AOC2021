import sys
with open(sys.argv[1], "r") as f:
    inp = [x.strip() for x in f.readlines()]

arr = []
for i in inp:
    arr.append([int(x) for x in i])


def part1():
    ans = 0
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            flag = True
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    if (x + dx > -1 and x + dx < len(arr[y])) and (y + dy > -1 and y + dy < len(arr)):
                        if arr[y][x] > arr[y+dy][x+dx]:
                            flag = False
            if flag:
                ans += arr[y][x] + 1
    print(ans)

def part2():
    groups = []
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            basin = []
            if arr[y][x] != 9:
                arr[y][x] = 9
                basin.append((y,x))
                count = 0
                while count < len(basin):
                    bX = basin[count][1]
                    bY = basin[count][0]
                    count += 1
                    for dx in [-1,1]:
                        newX = bX+dx
                        if newX > -1 and newX < len(arr[y]):
                            if arr[bY][newX] != 9:
                                basin.append((bY,newX))
                                arr[bY][newX] = 9

                    for dy in [-1,1]:
                        newY = bY+dy
                        if newY > -1 and newY < len(arr):
                            if arr[newY][bX] != 9:
                                basin.append((newY,bX))
                                arr[newY][bX] = 9
                groups.append(count)
    groups.sort()
    gLen = len(groups)
    print(groups[gLen-1] * groups[gLen-2] * groups[gLen-3])

part1()
part2()
