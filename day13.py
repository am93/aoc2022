from functools import cmp_to_key


def check_signal(pack1, pack2):
    if isinstance(pack1, int) and isinstance(pack2, int):
        if pack1 < pack2:
            return -1
        elif pack1 == pack2:
            return 0
        else:
            return 1
    elif isinstance(pack1, list) and isinstance(pack2, list):
        idx = 0
        while idx < len(pack1) and idx < len(pack2):
            res = check_signal(pack1[idx], pack2[idx])
            if res != 0:
                return res
            idx += 1
        return len(pack1) - len(pack2)
    elif isinstance(pack1, int) and isinstance(pack2, list):
        return check_signal([pack1], pack2)
    else:
        return check_signal(pack1, [pack2])


with open('inputs/day13.txt') as data:
    data = data.read().strip()
    packets = []
    part1 = 0
    for idx, pair in enumerate(data.split('\n\n'), start=1):
        pack1, pack2 = pair.split('\n')
        packets.append(eval(pack1))
        packets.append(eval(pack2))
        if check_signal(packets[-2], packets[-1]) < 0:
            part1 += idx
    print('Part1:', part1)

    packets.append([[2]])
    packets.append([[6]])

    packets = sorted(packets, key=cmp_to_key(lambda x, y: check_signal(x, y)))
    print('Part2:', (packets.index([[2]])+1)*(packets.index([[6]])+1))
