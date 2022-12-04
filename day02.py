# part1
scores1 = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6,
}

# part2
scores2 = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7,
}

with open('inputs/day02.txt', 'r') as data:
    match_data = data.read().split('\n')
    print('Part1: ',sum(map(lambda match : scores1[match], match_data)))
    print('Part2: ',sum(map(lambda match : scores2[match], match_data)))