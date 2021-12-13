import sys
from copy import deepcopy
with open(sys.argv[1], "r") as f:
    arr = f.readlines()

dic = {}
for line in arr:
    line = line.strip()
    x,y = line.split("-")
    if x in dic.keys():
        t = dic[x]
        t.append(y)
        dic[x] = t
    else:
        dic[x] = [y]
    if y in dic.keys():
        t = dic[y]
        t.append(x)
        dic[y] = t
    else:
        dic[y] = [x]

def part1():
    visited = []
    print(find1("start", visited))
    print(find2("start", visited))

def find1(key, visited):
    if key == "end":
        return 1
    visit = deepcopy(visited)
    if key.islower():
        visit.append(key)
    nodes = dic[key]
    count = 0
    nodes = list(filter(lambda node: node not in visit, nodes))
    if len(nodes) == 0:
        return 0
    for node in nodes:
        count += find1(node, visit)
    return count

def find2(key, visited):
    visit = deepcopy(visited)
    if key == "end":
        visit.append("end")
        return 1
    if key.islower():
        visit.append(key)
    else:
        visit.append(key)
    l = list(filter(lambda x: x.islower(), visit))
    if len(l) != len(set(l)):
        alreadyDONE = True
    else:
        alreadyDONE = False
    nodes = dic[key]
    count = 0
    if alreadyDONE == True:
        nodes = list(filter(lambda node: node.islower() == False or node not in visit, nodes))
    if len(nodes) == 0:
        return 0
    if (key == "dc" or key == "kj") and visit.count("dc") == 2:
    for node in nodes:
        if node != "start":
            count += find2(node, visit)
            
    return count

part1()
