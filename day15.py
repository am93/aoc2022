def parse_input(s):
    coords = []
    for line in s.splitlines():
        s_x = int(line.split('=')[1].split(',')[0])
        s_y = int(line.split('=')[2].split(':')[0])
        b_x = int(line.split('=')[-2].split(',')[0])
        b_y = int(line.split('=')[-1])
        mnhtn = abs(s_x-b_x) + abs(s_y-b_y)
        coords.append(((s_x, s_y), (b_x, b_y), mnhtn))
    return coords


def part1(data):
    trgt = 2000000
    beacons = set((b_x, b_y) for _, (b_x, b_y), _ in data)
    signal = set()

    for (s_x, s_y), _, mnhtn in data:
        for dx in (-1, 1):
            d_trgt = abs(s_y - trgt)
            x = s_x
            while d_trgt <= mnhtn:
                signal.add((x, trgt))
                x += dx
                d_trgt += 1
    return len(signal - beacons)


def part2(data):
    for (sx, sy), _, mnhtn in data:
        for perim in range(mnhtn + 1):
            for cx, cy in ((sx - mnhtn - 1 + perim, sy - perim), (sx + mnhtn + 1 - perim, sy - perim),
                           (sx - mnhtn - 1 + perim, sy + perim), (sx + mnhtn + 1 - perim, sy + perim)):
                if 0 < cx < 4000000 and 0 < cy < 4000000:
                    for (s1x, s1y), _, m1 in data:
                        if abs(cx - s1x) + abs(cy - s1y) < m1:
                            break
                    else:
                        return cx * 4000000 + cy


coords = parse_input(open('inputs/day15.txt').read())
print('Part1: ', part1(coords))
print('Part2: ', part2(coords))
