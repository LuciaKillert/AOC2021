import sys
with open(sys.argv[1], "r") as f:
    arr = [int(x) for x in f.readline().split(",")]
maxi = max(arr)
def part1():
    arr2 = [0]*maxi
    for i in range(maxi):
        for j in arr:
            arr2[i] += abs(i-j)

    print(min(arr2))
        
def part2():
    arr2 = [0]*maxi
    for i in range(maxi):
        for j in arr:
            n = abs(i-j)
            arr2[i] += (n*(n+1))//2

    print(min(arr2))

part1()
part2()

