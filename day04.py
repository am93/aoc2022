with open('inputs/day04.txt') as f:
    data = [list(map(int,line.replace(',','-').split('-'))) for line in f.read().splitlines()]

overlap_full = sum(map(lambda x : (x[0] <= x[2] and x[1] >= x[3]) or (x[2] <= x[0] and x[3] >= x[1]), data))
print('Part 1: ', overlap_full)

overlap_count = sum(map(lambda x : (x[0] <= x[2] and x[1] >= x[2]) or (x[2] <= x[0] and x[3] >= x[0]), data))
print('Part 2: ', overlap_count)