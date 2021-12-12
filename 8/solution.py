import sys
with open(sys.argv[1], "r") as f:
    arr2 = [x for x in f.readlines()]

arr = []
for a in arr2:
    x, y = a.split(" | ")
    arr.append((x,y))

def part1():
    counter = 0

    for a in arr:
        line = a[1].split()
        line = list(map(lambda x: len(x), line))
        for i in range(2,5):
            counter += line.count(i)
        counter += line.count(7)
    print(counter)

def part2():
    res = 0 
    for i in arr:
        nums = [0]*10
        for word in i[0].split():
            if len(word) == 2:
                nums[1] = set(word)
            if len(word) == 3:
                nums[7] = set(word)
            if len(word) == 4:
                nums[4] = set(word)
            if len(word) == 7:
                nums[8] = set(word)
        for word in i[0].split():
            word = set(word)
            if len(word) == 6:
                if nums[4].issubset(word): 
                    nums[9] = word
                elif nums[7].issubset(word):
                    nums[0] = word
                else:
                    nums[6] = word
            elif len(word) == 5:
                if nums[1].issubset(word): 
                    nums[3] = word
                elif len(nums[4] & word) == 3:
                    nums[5] = word
                else:
                    nums[2] = word
        line = i[1]
        count = ""
        for x in line.split():
            x = set(x)
            for y in range(len(nums)):
                if set(nums[y]) == x:
                    count += str(y)
        res += int(count)

    print(res)
part1()
part2()
