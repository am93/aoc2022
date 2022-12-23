from collections import defaultdict

dir_list = ['N', 'S', 'W', 'E']
groove = set()
idx = 0
for y, row in enumerate(open('inputs/day23.txt').readlines()):
    for x, ch in enumerate(row):
        if ch == '#':
            groove.add((x, y))

while True:
    idx += 1
    any_moved = False
    proposal = defaultdict(list)
    for (x, y) in groove:

        has_nbr = False
        for dx in range(-1,2):
            for dy in range(-1,2):
                if (dx != 0 or dy != 0) and (x + dx, y + dy) in groove:
                    has_nbr = True
        if not has_nbr:
            continue

        moved = False
        for dir in dir_list:
            if dir == 'N' and (not moved) and (x, y - 1) not in groove \
                                          and (x - 1, y - 1) not in groove \
                                          and (x + 1, y - 1) not in groove:
                proposal[(x, y - 1)].append((x, y))
                moved = True
            elif dir == 'E' and (not moved) and (x + 1, y) not in groove \
                                            and (x + 1, y - 1) not in groove \
                                            and (x + 1, y + 1) not in groove:
                proposal[(x + 1, y)].append((x, y))
                moved = True
            elif dir == 'S' and (not moved) and (x, y + 1) not in groove \
                                            and (x - 1, y + 1) not in groove \
                                            and (x + 1, y + 1) not in groove:
                proposal[(x, y + 1)].append((x, y))
                moved = True
            elif dir == 'W' and (not moved) and (x - 1, y ) not in groove \
                                            and (x - 1, y - 1) not in groove \
                                            and (x - 1, y + 1) not in groove:
                proposal[(x - 1, y)].append((x, y))
                moved = True

    dir_list = dir_list[1:]+[dir_list[0]]
    for new, old in proposal.items():
        if len(old) == 1:
            any_moved = True
            groove.remove(old[0])
            groove.add(new)

    if not any_moved:
        print('Part2:', idx)
        break

    if idx == 10:
        max_x, max_y = map(max, zip(*groove))
        min_x, min_y = map(min, zip(*groove))
        ans = 0
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if (x, y) not in groove:
                    ans += 1
        print('Part1:', ans)
