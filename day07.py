import collections
paths = [""]
sizes = collections.Counter()
req_space = 30000000 - 70000000
with open("inputs/day07.txt", "r") as data:
    for line in data:
        line = line.strip()
        if line.startswith("$ cd "):
            paths.append(paths[-1]+"/"+line.split(" ")[-1])
        elif line[0].isnumeric():
            fsize = int(line.split(" ")[0])
            req_space += fsize
            sizes.update({p: fsize for p in paths})
        elif line.startswith("$ cd .."):
            paths = paths[:-1]

print('Part1: ', sum(x for x in sizes.values() if x <= 100000))
print('Part2: ', min(x for x in sizes.values() if x >= req_space))
