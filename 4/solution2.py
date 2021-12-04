import sys

with open(sys.argv[1], "r") as f:
    draws = [int(x) for x in f.readline().split(",")]
    f.readline()
    lines = [x for x in f.readlines()]

result = []

def part1():
    count = 0
    temp2 = []
    bingos = []
    for line in lines:
        temp = []
        if line == "\n":
            bingos.append((temp2, count))
            count += 1
            temp2 = []
        else:
            for num in line.split():
                temp.append(int(num))
            temp2.append(temp)
    bingos.append((temp2, count))

    for draw in draws:
        for bingo, num in bingos:
            for line in bingo:
                for i in range(0,len(line)):
                    if line[i] == draw:
                        line[i] = -1
            temp = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            for i in range(0,len(bingo)):
                if bingo[i].count(-1) == 5:
                    bingoF(bingo,num,draw)
                for j in range(0,len(bingo[i])):
                    temp[j][i] = bingo[i][j]
            for line in temp:
                if line.count(-1) == 5:
                    bingoF(bingo,num,draw)

def bingoF(bingo, num, draw):
    b = True
    for res, n in result:
        if n == num:
            b = False
    if b:
        countT = 0
        for l in bingo:
            for n in l:
                if n != -1:
                    countT += n
        result.append((draw*countT,num))
        print(draw*countT,num)
                    
part1()

