def sandfall(part1, paths, max_y):
    occupied = paths.copy()
    while True:
        sand_x, sand_y = 500, 0

        if (500, 0) in occupied:
            return len(occupied - paths)

        while True:
            if (sand_x, sand_y + 1) not in occupied and sand_y < max_y:
                sand_y += 1
            elif (sand_x - 1, sand_y + 1) not in occupied and sand_y < max_y:
                sand_y += 1
                sand_x -= 1
                if sand_y == max_y and part1:
                    return len(occupied - paths)-1
            elif (sand_x + 1, sand_y + 1) not in occupied and sand_y < max_y:
                sand_y += 1
                sand_x += 1
                if sand_y == max_y and part1:
                    return len(occupied - paths)-1
            else:
                occupied.add((sand_x, sand_y))
                break


with open('inputs/day14.txt') as data:
    paths = set()
    max_y = 0
    for path in data.read().splitlines():
        path = path.split(" -> ")
        for i in range(1, len(path)):
            x, y = [int(p) for p in path[i].split(",")]
            prev_x, prev_y = [int(p) for p in path[i - 1].split(",")]
            max_y = max(y, prev_y, max_y)
            if x == prev_x:
                for dy in range(min(prev_y, y), max(prev_y, y) + 1):
                    paths.add((x, dy))
            else:
                for dx in range(min(prev_x, x), max(prev_x, x) + 1):
                    paths.add((dx, y))

    print("Part 1:", sandfall(True, paths, max_y))
    max_y += 1
    print("Part 2:", sandfall(False, paths, max_y))
