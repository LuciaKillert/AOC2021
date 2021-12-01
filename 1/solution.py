import sys
with open(sys.argv[1], "r") as f:
    listA = [int(x) for x in f.readlines()]
    
def part1():
    counter = 0
    for i in range(0, len(listA) - 1):
        if listA[i] < listA[i+1]:
            counter += 1
    return counter

def part2():
    counter = 0
    listB = []

    #computing the sums and putting them into a list
    for i in range(0, len(listA) - 2):
        sum = listA[i] + listA[i+1] + listA[i+2]
        listB.append(sum)

    #comparing each sum and increasing the counter
    for i in range(0, len(listB) - 1):
        if listB[i] < listB[i+1]:
            counter += 1
    return counter

print("Part 1: ", part1())
print("Part 2: ", part2())
