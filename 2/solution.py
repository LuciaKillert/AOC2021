import sys

with open(sys.argv[1], "r") as f:
    input = [x.split(" ") for x in f.readlines()]

def part1():
    forward = sum(list(map(lambda x: int(x[1]), filter(lambda line: line[0] == "forward", input))))
    up = sum(list(map(lambda x: int(x[1]), filter(lambda line: line[0] == "up", input))))
    down = sum(list(map(lambda x: int(x[1]), filter(lambda line: line[0] == "down", input))))
    print(forward * (down - up))

def part2():
    aim = 0
    depth = 0
    position = 0
    for i in input:
        i[1] = int(i[1])
        if i[0] == "forward":
            position += i[1]
            depth += i[1] * aim
        elif i[0] == "down":
            aim += i[1]
        else:
            aim -= i[1]
    print(depth * position)
part1()
part2()
