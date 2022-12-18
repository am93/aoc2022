import itertools


def get_neighbours(cube):
    x, y, z = cube
    return [(x - 1, y, z), (x + 1, y, z),
            (x, y - 1, z), (x, y + 1, z),
            (x, y, z - 1), (x, y, z + 1)]


def part1(cubes):
    cubes = frozenset(cubes)
    surface_area = 0
    for cube in cubes:
        neighbours = get_neighbours(cube)
        for n in neighbours:
            if n not in cubes:
                surface_area += 1
    return surface_area


def part2(cubes):
    cubes = frozenset(cubes)
    min_x = min(cubes, key=lambda c: c[0])[0] - 1
    min_y = min(cubes, key=lambda c: c[1])[1] - 1
    min_z = min(cubes, key=lambda c: c[2])[2] - 1
    max_x = max(cubes, key=lambda c: c[0])[0] + 1
    max_y = max(cubes, key=lambda c: c[1])[1] + 1
    max_z = max(cubes, key=lambda c: c[2])[2] + 1
    flooded = set()
    to_check = set()
    to_check.add((min_x, min_y, min_z))
    while len(to_check) > 0:
        cand = to_check.pop()
        flooded.add(cand)
        neighbours = get_neighbours(cand)
        for n_x, n_y, n_z in neighbours:
            if min_x <= n_x <= max_x and min_y <= n_y <= max_y and min_z <= n_z <= max_z:
                if (n_x, n_y, n_z) not in cubes and (n_x, n_y, n_z) not in flooded:
                    to_check.add((n_x, n_y, n_z))

    filled_blob = set()
    for cb in itertools.product(range(min_x, max_x + 1), range(min_y, max_y + 1), range(min_z, max_z + 1)):
        if cb not in flooded:
            filled_blob.add(cb)

    return part1(filled_blob)


with open("inputs/day18.txt", "r") as data:
    lines = [eval('('+line+')') for line in data.readlines()]
    print('Part1:', part1(lines))
    print('Part2:', part2(lines))
