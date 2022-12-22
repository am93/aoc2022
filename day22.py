# Please don't judge the code - I was trying to get to leaderboard,but failed due to stupid off by one error
# Part2 is therefore input specific and not general

start = None
board = {}
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

with open('inputs/day22.txt') as data:
    # ------------------------------------- INPUT PARSING
    parts = data.read().split('\n\n')
    for y, line in enumerate(parts[0].split('\n'), start=1):
        for x, state in enumerate(line, start=1):
            if not state.isspace():
                board[(x, y)] = state
                if start is None:
                    start = (x, y)

    path = []
    last = ''
    for c in parts[1]:
        if c in 'LR':
            if last != '':
                path.append(int(last))
                last = ''
            path.append(c)
        else:
            last += c
    if last != '':
        path.append(int(last))

    # ------------------------------------- PART 1
    dx = 1
    dy = 0
    crr = ''
    (x, y) = start

    for step in path:
        if isinstance(step, int):
            for _ in range(step):
                nx, ny = x+dx, y+dy
                cell = board.get((nx, ny))
                if cell is None:
                    nnx, nny = x, y
                    while (nnx, nny) in board:
                        nx, ny = nnx, nny
                        nnx -= dx
                        nny -= dy
                    cell = board[(nx, ny)]
                if cell == '#':
                    break # Hit a wall
                x, y = nx, ny
        elif step == 'R':
            dy, dx = dx, -dy
        elif step == 'L':
            dx, dy = dy, -dx

    print('Part1:', 1000 * y + 4 * x + dirs.index((dx,dy)))

    # ------------------------------------- PART 2
    dx = 1
    dy = 0
    crr = ''
    (x, y) = start

    sequence = []

    for step in path:
        if isinstance(step, int):
            for _ in range(step):
                bx, by = x, y
                bdx, bdy = dx, dy
                nx, ny = x+dx, y+dy
                cell = board.get((nx, ny))
                wrap = False
                if cell is None:
                    wrap = True
                    if dy == -1 and 51 <= x <= 100 and y == 1: # 1-UP
                        y = 151 + x - 51
                        x = 1
                        dx, dy = 1, 0
                    elif dx == -1 and x == 1 and 151 <= y <= 200: #1-LEFT
                        x = y - 100
                        y = 1
                        dx, dy = 0, 1
                    elif dx == -1 and x == 51 and 1 <= y <= 50: #2-left
                        x = 1
                        y = 150 - y + 1
                        dx, dy = 1, 0
                    elif dx == -1 and x == 1 and 101 <= y <= 150: #2-left
                        x = 51
                        y = abs(y - 150) + 1
                        dx, dy = 1,0
                    elif dy == -1 and y == 1 and 101 <= x <= 150: #3-up
                        y = 200
                        x = x - 100
                    elif dy == 1 and y == 200 and 1 <= x <= 50: #3-down
                        y = 1
                        x = x + 100
                    elif dx == 1 and x == 150 and 1 <= y <= 50: #4-right
                        x = 100
                        y = 150 - y + 1
                        dx, dy = -1, 0
                    elif dx == 1 and x == 100 and 101 <= y <= 150: #4-right
                        x = 150
                        y = abs(y - 150) + 1
                        dx, dy = -1, 0
                    elif dy == 1 and y == 50 and 101 <= x <= 150: #5-down
                        y = x - 50
                        x = 100
                        dx, dy = -1, 0
                    elif dx == 1 and x == 100 and 51 <= y <= 100: #5-right
                        x = y + 50
                        y = 50
                        dx, dy = 0, -1
                    elif dx == -1 and x == 51 and 51 <= y <= 100: #6-left
                        x = y - 50
                        y = 101
                        dx, dy = 0, 1
                    elif dy == -1 and y == 101 and 1 <= x <= 50: #6-up
                        y = x + 50
                        x = 51
                        dx, dy = 1, 0
                    elif dy == 1 and y == 150 and 51 <= x <= 100: #7-down
                        y = x + 100
                        x = 50
                        dx, dy = -1, 0
                    elif dx == 1 and x == 50 and 151 <= y <= 200: #7-right
                        x = y - 100
                        y = 150
                        dx, dy = 0, -1

                if cell == '#':
                    break # Hit a wall
                if wrap and board.get((x, y)) == '#': # revert
                    x, y = bx, by
                    dx, dy = bdx, bdy
                    break
                if not wrap:
                    x, y = nx, ny
                sequence.append((x,y))
        elif step == 'R':
            dy, dx = dx, -dy
        elif step == 'L':
            dx, dy = dy, -dx

    print('Part2:', 1000 * y + 4 * x + dirs.index((dx,dy)))
    