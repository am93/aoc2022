from collections import deque


def solve(ore_cost, clay_cost, obsidian_robot_ore, obsidian_robot_clay, geode_robot_ore, geode_robot_obs, time):
    best = 0
    to_check = deque([(0, 0, 0, 0, 1, 0, 0, 0, time)])
    have_checked = set()
    max_ore_cost = max([ore_cost, clay_cost, obsidian_robot_ore, geode_robot_ore])

    while len(to_check) > 0:
        ore, clay, obsid, geod, ro, rc, robs, rg, t = to_check.popleft()
        best = geod if geod > best else best
        if t == 0:
            continue

        ro = ro if ro < max_ore_cost else max_ore_cost
        if ore > t * max_ore_cost - ro * (t - 1):
            ore = t * max_ore_cost - ro * (t - 1)

        rc = rc if rc < obsidian_robot_clay else obsidian_robot_clay
        if clay > t * obsidian_robot_clay - rc * (t - 1):
            clay = t * obsidian_robot_clay - rc * (t - 1)

        robs = robs if robs < geode_robot_obs else geode_robot_obs
        if obsid > t * geode_robot_obs - robs * (t - 1):
            obsid = t * geode_robot_obs - robs * (t - 1)

        state = (ore, clay, obsid, geod, ro, rc, robs, rg, t)

        if state in have_checked:
            continue
        have_checked.add(state)

        to_check.append((ore + ro, clay + rc, obsid + robs, geod + rg, ro, rc, robs, rg, t - 1))
        if ore >= ore_cost:
            to_check.append((ore - ore_cost + ro, clay + rc, obsid + robs, geod + rg, ro + 1, rc, robs, rg, t - 1))
        if ore >= clay_cost:
            to_check.append((ore - clay_cost + ro, clay + rc, obsid + robs, geod + rg, ro, rc + 1, robs, rg, t - 1))
        if ore >= obsidian_robot_ore and clay >= obsidian_robot_clay:
            to_check.append((ore - obsidian_robot_ore + ro, clay - obsidian_robot_clay + rc, obsid + robs, geod + rg, ro, rc, robs + 1, rg, t - 1))
        if ore >= geode_robot_ore and obsid >= geode_robot_obs:
            to_check.append((ore - geode_robot_ore + ro, clay + rc, obsid - geode_robot_obs + robs, geod + rg, ro, rc, robs, rg + 1, t - 1))
    return best


p1, p2 = 0, 1
for line in open('inputs/day19.txt').readlines():
    words = line.split(' ')
    idx = int(words[1].replace(':', ''))
    print('Processing blueprint ', idx)
    ore_cost, clay_cost = int(words[6]), int(words[12])
    obsidian_robot_ore, obsidian_robot_clay = int(words[18]), int(words[21])
    geode_robot_ore, geode_robot_obs = int(words[27]), int(words[30])
    p1 += idx * solve(ore_cost, clay_cost, obsidian_robot_ore, obsidian_robot_clay, geode_robot_ore, geode_robot_obs, 24)
    if idx <= 3:
        p2 *= solve(ore_cost, clay_cost, obsidian_robot_ore, obsidian_robot_clay, geode_robot_ore, geode_robot_obs, 32)
print('Part1:', p1)
print('Part2:', p2)
