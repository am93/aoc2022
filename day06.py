with open("inputs/day06.txt", "r") as data:
    chrs = data.read()
    print('Part1: ', min(map(lambda i : i+4 if len(set(chrs[i:i+4])) == 4 else float('inf'), range(len(chrs)))))
    print('Part2: ', min(map(lambda i : i+14 if len(set(chrs[i:i+14])) == 14 else float('inf'), range(len(chrs)))))