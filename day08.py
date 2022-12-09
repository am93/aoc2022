with open("inputs/day08.txt", "r") as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

vis_count = 4 * len(grid) - 4
max_score = 0

for x in range(1, len(grid) - 1):
    for y in range(1, len(grid) - 1):
        scenic = 1
        vis = 0

        for i in range(x + 1, len(grid)):
            if grid[i][y] >= grid[x][y]:
                break
        else:
            vis = 1
        scenic *= i - x

        for i in range(y + 1, len(grid)):
            if grid[x][i] >= grid[x][y]:
                break
        else:
            vis = 1
        scenic *= i - y

        for i in range(x - 1, -1, -1):
            if grid[i][y] >= grid[x][y]:
                break
        else:
            vis = 1
        scenic *= x - i

        for i in range(y - 1, -1, -1):
            if grid[x][i] >= grid[x][y]:
                break
        else:
            vis = 1
        scenic *= y - i

        if vis:
            vis_count += 1
        max_score = max(max_score, scenic)

print('Part1: ', vis_count)
print('Part2: ', max_score)
