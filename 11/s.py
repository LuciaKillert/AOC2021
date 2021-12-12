import sys

with open(sys.argv[1], "r") as f:
    inp = [x.strip() for x in f.readlines()]

arr = []
for line in inp:
    arr.append(list(map(lambda x: int(x), line)))

def part1():
    ans1 = 0
    for i in range(10000000):
        flash = []
        for y in range(len(arr)):
            for x in range(len(arr[y])):
                arr[y][x] += 1
                if arr[y][x] > 9:
                    flash.append((y,x))
        index = 0
        while len(flash) > index:
            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    nY = dy + flash[index][0]
                    nX = dx + flash[index][1]
                    if -1 < nY < len(arr) and -1 < nX < len(arr[y]):
                        arr[nY][nX] += 1
                        if arr[nY][nX] > 9 and (nY,nX) not in flash:
                            flash.append((nY,nX))
            index += 1
        for inc in flash:
            arr[inc[0]][inc[1]] = 0
        ans1 += len(flash)
        if i == 100:
            print(ans1)
        if len(flash) == 100:
            print(i+1)
            return
part1()
