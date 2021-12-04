import sys

with open(sys.argv[1], "r") as f:
    input = [x.split(" ") for x in f.readlines()]

def part1():
    print(sum(list(map(lambda x: int(x[1]), filter(lambda line: line[0] == "forward", input))))
            * ( sum(list(map(lambda x: int(x[1]), filter(lambda line: line[0] == "down", input))))
                - sum(list(map(lambda x: int(x[1]), filter(lambda line: line[0] == "up", input))))))
def part2():
    print("Part 2")

part1()
