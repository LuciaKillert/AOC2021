import sys

def solve(num):
    with open(sys.argv[1], "r") as f:
        arr2 = [int(x) for x in f.readline().split(",")]
    
    arr = [0,0,0,0,0,0,0,0,0]
    for i in range(0,9):
        arr[i] = arr2.count(i)

    for i in range(num):
        temp = arr[0]
        for j in range(8):
            arr[j] = arr[j+1]
            if j == 6:
                arr[j] += temp
        arr[8] = temp

    print(sum(arr))


solve(80)
solve(256)
