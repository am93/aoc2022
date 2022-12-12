def coords(hm, letter):
    return [(x, y) for x in range(len(hm)) for y in range(len(hm[0])) if hm[x][y] == letter]


def height(hm, x, y):
    if hm[x][y] == 'S':
        return ord('a')
    elif hm[x][y] == 'E':
        return ord('z')
    else:
        return ord(hm[x][y])


def fewest_steps(hm, sx, sy, ex, ey):
    rows, cols = len(hm), len(hm[0])
    steps = [[float('inf')]*cols for _ in range(rows)]
    steps[sx][sy] = 0
    queue = [(sx, sy)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            n_x, n_y = x + dx, y + dy
            if n_x in range(0, rows) and n_y in range(0, cols) and steps[n_x][n_y] > steps[x][y] + 1:
                if height(hm, n_x, n_y) <= height(hm, x, y) + 1:
                    steps[n_x][n_y] = steps[x][y] + 1
                    queue.append((n_x, n_y))
            if (n_x, n_y) == (ex, ey):
                break
    return steps[ex][ey]


with open('inputs/day12.txt') as data:
    heightmap = data.read().splitlines()
    s_x, s_y = coords(heightmap, 'S')[0]
    e_x, e_y = coords(heightmap, 'E')[0]

    part1 = fewest_steps(heightmap, s_x, s_y, e_x, e_y)
    print('Part 1:', part1)
    part2 = min(fewest_steps(heightmap, sx, sy, e_x, e_y) for sx, sy in coords(heightmap, 'a'))
    print('Part 2:', part2)
