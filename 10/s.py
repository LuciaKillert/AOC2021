import sys

with open(sys.argv[1], "r") as f:
    arr = [x.strip() for x in f.readlines()]

opening = {'<':4, '(':1, '[':2, '{':3}
closing = {'>':25137, ')':3, ']':57, '}':1197}

incomplete = []
corrupt = []

def part1():
    ans1 = 0
    ans2 = []
    for line in arr:
        stack = []
        count = 0
        for l in line:
            if l in opening.keys():
                stack.append(l)
            else:
                top = stack.pop()
                if top == '<' and l == '>':
                    continue
                elif top == '(' and l == ')':
                    continue
                elif top == '[' and l == ']':
                    continue
                elif top == '{' and l == '}':
                    continue
                else:
                    ans1 += closing[l]
                    corrupt.append(line)
        if line not in corrupt:
            while len(stack) > 0: 
                count *= 5
                count += opening[stack.pop()]
        if count != 0:
            ans2.append(count)

    print(ans1)
    ans2.sort()
    print(ans2[len(ans2)//2])




part1()
