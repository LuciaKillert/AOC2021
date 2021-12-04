import sys

with open(sys.argv[1], "r") as f:
    draws = [int(x) for x in f.readline().split(",")]
    f.readline()
    lines = [x for x in f.readlines()]

result = []

def part1():
    temp2 = []
    bingos = []
    for line in lines:
        temp = []
        if line == "\n":
            bingos.append(temp2)
            temp2 = []
        else:
            for num in line.split():
                temp.append(int(num))
            temp2.append(temp)
    bingos.append(temp2)

    for draw in draws:
        for bingo in bingos:
            for line in bingo:
                for i in range(0,len(line)):
                    if line[i] == draw:
                        line[i] = -1
            temp = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            for i in range(0,len(bingo)):
                if bingo[i].count(-1) == 5:
                    bingoF(bingo,draw)
                    return
                for j in range(0,len(bingo[i])):
                    temp[j][i] = bingo[i][j]
            for line in temp:
                if line.count(-1) == 5:
                    bingoF(bingo,draw)
                    return

def bingoF(bingo, draw):
    count = 0
    for line in bingo:
        for i in line:
            if i != -1:
                count += i
    print(count*draw)
part1()

