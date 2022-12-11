monkeys = []
inspections = dict()
items = dict()
memoisation = dict()
with open('inputs/day11.txt') as data:
    monkeys_descr = data.read().split('\n\n')


def setup():
    lcm_tmp = 1
    for m in monkeys_descr:
        m = m.split('\n')
        monkey_id = int(m[0].split(" ")[-1].strip(":"))
        items[monkey_id] = [int(x) for x in m[1].split(':')[1].split(', ')]
        inspections[monkey_id] = 0
        operation = m[2].split(' = ')
        modulo = int(m[3].split(' ')[-1])
        lcm_tmp *= modulo
        t_true = int(m[4].split(' ')[-1])
        t_false = int(m[5].split(' ')[-1])
        monkeys.append([operation[-1],modulo,(t_false, t_true)])
    return lcm_tmp


def worry_lvl(item, oper):
    new_oper = oper.replace('old', str(item))
    if new_oper not in memoisation.keys():
        memoisation[new_oper] = eval(new_oper)
    return memoisation[new_oper]


def solve(part1, lcm=0):
    for m_id in items.keys():
        while items[m_id]:
            inspections[m_id] += 1
            itm = items[m_id].pop(0)
            if part1:
                itm = worry_lvl(itm, monkeys[m_id][0]) // 3
            else:
                itm = worry_lvl(itm, monkeys[m_id][0]) % lcm
            items[monkeys[m_id][2][int(itm % monkeys[m_id][1] == 0)]].append(itm)


setup()
for i in range(20):
    solve(True)
monkey_business = sorted(inspections.values())
print('Part1:', monkey_business[-1] * monkey_business[-2])

lcm = setup()
for i in range(10000):
    solve(False, lcm)
monkey_business = sorted(inspections.values())
print('Part2:', monkey_business[-1] * monkey_business[-2])
