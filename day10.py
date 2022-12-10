with open("inputs/day10.txt", "r") as data:
    signals = [0]
    x = 1
    last_idx = 1
    idx = 1
    buff = ""
    result = 0
    for instr in data.read().splitlines():
        if instr.startswith("noop"):
            signals.extend([x])
        else:
            signals.extend([x,x])
            x += int(instr.split(" ")[1])
        idx = len(signals)
        for i in range(last_idx, idx):
            if abs(signals[i] - (i - 1) % 40) < 2:
                buff += "#"
            else:
                buff += "."
            if i % 40 == 0:
                print(buff)
                buff = ""
            if i % 40 == 20 and i < 221:
                result += signals[i] * i
        last_idx = idx
    print('Part1: ', result)
