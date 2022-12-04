with open("inputs/day03.txt") as f:
    data = f.read().splitlines()

score = lambda x : ord(x) - ord('a') + 1 if x >= 'a' and x <= 'z' else ord(x) - ord('A') + 27

part1 = sum(score(set(x[:len(x)//2]).intersection(set(x[len(x)//2:])).pop()) for x in data)
print ('Part1: ',part1)

iter_data = iter(data)
part2 = sum(score(set(x[0]).intersection(set(x[1])).intersection(set(x[2])).pop()) for x in zip(iter_data,iter_data,iter_data))
print ('Part2: ',part2)