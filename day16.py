best_p1 = 0
best_p2 = 0
start = 'AA'


def parse_input(s):
    valves = {}
    for line in s.splitlines():
        valve = line.split(' ')[1]
        rate = int(line.split('=')[-1].split(';')[0])
        if len(line.split('to valves')) > 1:
            neigh = [n.strip() for n in line.split('to valves')[1].split(',')]
        else:
            neigh = [line.split(' ')[-1]]
        valves[valve] = {'rate': rate, 'neigh': neigh, 'cand': {}}
    return valves


def path_cost(crr, end):
    cost = 1
    while True:
        next = set()
        for x in crr:
            if x == end:
                return cost
            for n in valves[x]['neigh']:
                next.add(n)
        crr = next
        cost += 1
        if len(next) == 0:
            return -1


def search_part1(crr, opened, total, time_to_go):
    global best_p1
    if total > best_p1:
        best_p1 = total

    if time_to_go <= 0:
        return best_p1

    if crr not in opened:
        search_part1(crr, opened.union([crr]), total + valves[crr]['rate'] * time_to_go, time_to_go - 1)
    else:
        for c in valves[crr]['cand'].keys():
            if c not in opened:
                search_part1(c, opened, total, time_to_go - valves[crr]['cand'][c])


def search_part2(crr, opened, total, time_to_go, elephant):
    global best_p2
    if total > best_p2:
        best_p2 = total

    if time_to_go <= 0:
        return

    if crr not in opened:
        if not elephant:
            search_part2('AA', opened.union([crr]), total + valves[crr]['rate'] * time_to_go, 26 - 1, True)
        search_part2(crr, opened.union([crr]), total + valves[crr]['rate'] * time_to_go, time_to_go - 1, elephant)
    else:
        for c in valves[crr]['cand'].keys():
            if c not in opened:
                search_part2(c, opened, total, time_to_go - valves[crr]['cand'][c], elephant)


valves = parse_input(open('inputs/day16.txt').read())
non_zeros = [x for x in list(valves.keys()) if valves[x]['rate'] != 0]

for v1 in non_zeros + [start]:
    for v2 in non_zeros:
        if v1 != v2:
            valves[v1]['cand'][v2] = path_cost(valves[v1]['neigh'], v2)

search_part1(start, set(), 0, 30)
print('Part1:', best_p1)
search_part2(start, set(), 0, 26, False)
print('Part2:', best_p2)
