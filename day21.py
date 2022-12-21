def shout(name, val, mb):
    if name == 'humn' and val >= 0:
        return val
    ops = mb[name]
    if len(ops) == 1:
        return int(ops[0])
    else:
        return eval(''.join(ops).replace(ops[0], str(shout(ops[0], val, mb)))
                                .replace(ops[2], str(shout(ops[2], val, mb))))


mnky_bussiness = {}

for line in open('inputs/day21.txt').readlines():
    words = line.split()
    name = words[0].strip(':')
    mnky_bussiness[name] = line.split(':')[1].split()

print('Part1:', shout('root', -1, mnky_bussiness))

mnky1 = mnky_bussiness['root'][0]
mnky2 = mnky_bussiness['root'][2]

mnky1_score = shout(mnky1, -1, mnky_bussiness)
mnky2_score = shout(mnky2, -1, mnky_bussiness)

target = 0
if mnky1_score < mnky2_score:
    target = mnky1_score
    othr_mnky = mnky2
else:
    target = mnky2_score
    othr_mnky = mnky1

bottom = 0
top = 124765768589550    # my part1 solution -
while bottom < top:
    mid = (bottom + top)//2
    score = target - shout(othr_mnky, mid, mnky_bussiness)
    if score < 0:
        bottom = mid
    elif score == 0:
        print('Part2:', mid)
        break
    else:
        top = mid
