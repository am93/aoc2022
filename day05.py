stacks_p1 = {
	1: "PZMTRCN"[::-1],
	2: "ZBSTND"[::-1],
	3: "GTCFRQHM"[::-1],
	4: "ZRG"[::-1],
	5: "HRNZ"[::-1],
	6: "DLZPWSHF"[::-1],
	7: "MGCRZDW"[::-1],
	8: "QZWHLFJS"[::-1],
	9: "NWPQS"[::-1]
}

stacks_p2 = {
	1: "PZMTRCN"[::-1],
	2: "ZBSTND"[::-1],
	3: "GTCFRQHM"[::-1],
	4: "ZRG"[::-1],
	5: "HRNZ"[::-1],
	6: "DLZPWSHF"[::-1],
	7: "MGCRZDW"[::-1],
	8: "QZWHLFJS"[::-1],
	9: "NWPQS"[::-1]
}

with open("inputs/day05.txt", "r") as data:
    for movement in data.read().splitlines():
        command = movement.split(" ")
        q,s,d = int(command[1]),int(command[3]),int(command[5])
        # part 1
        source_stack = stacks_p1[s]
        stacks_p1[d] = stacks_p1[d] + source_stack[-q:][::-1]
        stacks_p1[s] = source_stack[0: -q]
        # part 2 
        source_stack = stacks_p2[s]
        stacks_p2[d] = stacks_p2[d] + source_stack[-q:]
        stacks_p2[s] = source_stack[0: -q]
    print('Part1:',''.join(map(lambda k : stacks_p1[k][-1], sorted(stacks_p1.keys()))))
    print('Part2:',''.join(map(lambda k : stacks_p2[k][-1], sorted(stacks_p2.keys()))))