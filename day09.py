def calc_pos(hd,tl):
    dx = hd[0]-tl[0]
    dy = hd[1]-tl[1]
    if abs(dx)<=1 and abs(dy)<=1:
        pass
    elif abs(dx)>=2 and abs(dy)>=2:
        tl = (hd[0]+1 if tl[0]>hd[0] else hd[0]-1, hd[1]+1 if tl[1]>hd[1] else hd[1]-1)
    elif abs(dx)>=2:
        tl = (hd[0]+1 if tl[0]>hd[0] else hd[0]-1, hd[1])
    elif abs(dy)>=2:
        tl = (hd[0], hd[1]+1 if tl[1]>hd[1] else hd[1]-1)
    return tl


head = (0,0)
tail = [(0,0)]*9
cords = { "R": (1,0), "U": (0,1), "L":(-1,0), "D":(0,-1)}
part1 = set([(0,0)])
part2 = set([(0,0)])
with open("inputs/day09.txt", "r") as data:
    for movement in data.read().splitlines():
        steps = 0
        length = int(movement.split(" ")[1])
        while steps < length:
            steps += 1
            move = cords[movement.split(" ")[0]]
            head = tuple(map(sum, zip(head, move)))
            tail[0] = calc_pos(head, tail[0])
            for i in range(1, 9):
                tail[i] = calc_pos(tail[i-1], tail[i])
            part1.add(tail[0])
            part2.add(tail[8])
print('Part1: ',len(part1))
print('Part2: ', len(part2))