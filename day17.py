def generate_piece(seq, y):
    if seq == 0:
        return set([(x, y) for x in range(2, 6)])
    elif seq == 1:
        return set([(3, y+2), (2, y+1), (3, y+1), (4, y+1), (3, y)])
    elif seq == 2:
        return set([(2, y), (3, y), (4, y), (4, y+1), (4, y+2)])
    elif seq == 3:
        return set([(2, y+i) for i in range(4)])
    else:
        return set([(2, y + 1), (2, y), (3, y+1), (3, y)])


def move(piece, dir):
    if dir == 'left' and any([x == 0 for (x, y) in piece]):
        return piece
    elif dir == 'left':
        return set([(x - 1, y) for (x, y) in piece])
    elif dir == 'right' and any([x == 6 for (x, y) in piece]):
        return piece
    elif dir == 'right':
        return set([(x + 1, y) for (x, y) in piece])
    elif dir == 'down':
        return set([(x, y-1) for (x, y) in piece])
    elif dir == 'up':
        return set([(x, y+1) for (x, y) in piece])


def pattern(state, max_y):
    return frozenset([(x, max_y-y) for (x, y) in state if max_y-y <= 100]) #


def solve(jets, chamber, max_iters):
    known = {}
    max_y, jet_idx, itr_idx = 0, 0, 0
    skipped = 0
    while itr_idx < max_iters:
        piece = generate_piece(itr_idx % 5, max_y + 4)
        while True:
            if jets[jet_idx] == '>':
                piece = move(piece, 'right')
                if piece.intersection(chamber):
                    piece = move(piece, 'left')
            else:
                piece = move(piece, 'left')
                if piece.intersection(chamber):
                    piece = move(piece, 'right')
            jet_idx = (jet_idx+1) % len(jets)

            piece = move(piece, 'down')
            if piece.intersection(chamber):
                piece = move(piece, 'up')
                chamber = chamber.union(piece)
                max_y = max([y for (_, y) in chamber])

                state = (itr_idx % 5, jet_idx, pattern(chamber, max_y))
                if state in known:
                    (k_idx, k_y) = known[state]
                    d_y = max_y - k_y
                    d_idx = itr_idx - k_idx
                    rpts = (max_iters - itr_idx) // d_idx
                    itr_idx += rpts * d_idx
                    skipped += rpts * d_y
                known[state] = (itr_idx, max_y)
                break
        itr_idx += 1
    return max_y+skipped


jets = open('inputs/day17.txt').read().strip()
print('Part1:', solve(jets, set([(x, 0) for x in range(7)]), 2022))
print('Part2:', solve(jets, set([(x, 0) for x in range(7)]), 1000000000000))
