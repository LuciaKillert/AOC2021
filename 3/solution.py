import sys
with open(sys.argv[1], "r") as f:
    input = [x for x in f.readlines()]

def part1():
    count = [0,0,0,0,0,0,0,0,0,0,0,0]
    for line in input:
        for i in range(0, len(line)):
            if line[i] == "1":
                count[i] += 1

    size = len(input)
    gamma = ""
    epsilon = ""
    for c in count:
        if (c > size/2):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print("Part 1: ", int(gamma, 2)* int(epsilon, 2))


def part2():
    gammaList = input.copy()
    index = 0
    while(len(gammaList) != 1):
        list1 = []
        list0 = []
        for line in gammaList:
            if line[index] == "1":
                list1.append(line)
            else:
                list0.append(line)
        if len(list1) >= len(list0):
            gammaList = list1
        else:
            gammaList = list0
        index += 1
    epsilList = input.copy()
    index = 0

    while(len(epsilList) != 1):
        list1 = []
        list0 = []
        for line in epsilList:
            if line[index] == "1":
                list1.append(line)
            else:
                list0.append(line)
        if len(list1) >= len(list0):
            epsilList = list0
        else:
            epsilList = list1
        index += 1

    print(int(gammaList[0],2) * int(epsilList[0],2))

part1()
part2()
