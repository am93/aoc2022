from collections import deque


def mix(numbers, idxs):
    for index in range(len(numbers)):
        location = idxs.index(index)

        numbers.rotate(-location)
        idxs.rotate(-location)

        number = numbers.popleft()
        index = idxs.popleft()

        numbers.rotate(-number)
        idxs.rotate(-number)

        numbers.appendleft(number)
        idxs.appendleft(index)
    return numbers, idxs


def grove_coordinates(numbers):
    location = numbers.index(0)
    return numbers[(location + 1000) % len(numbers)] + numbers[(location + 2000) % len(numbers)] + numbers[(location + 3000) % len(numbers)]


with open('inputs/day20.txt', 'r') as data:
    nums_p1 = deque(int(line) for line in data.readlines())
    nums_p2 = deque(811589153 * number for number in nums_p1)

    idxs = deque(range(len(nums_p1)))
    nums_p1, _ = mix(nums_p1, idxs)
    print('Part1:', grove_coordinates(nums_p1))

    idxs = deque(range(len(nums_p1)))
    for _ in range(10):
        nums_p2, idxs = mix(nums_p2, idxs)
    print('Part2:', grove_coordinates(nums_p2))
