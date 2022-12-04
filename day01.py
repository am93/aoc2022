with open('inputs/day01.txt', 'r') as data:
    elf_cal = sorted([sum(map(int,cals_per_elf.split('\n'))) for cals_per_elf in data.read().split('\n\n')])
    print('Most calories: '+str(elf_cal[-1]))
    print('    Top three: '+str(sum(elf_cal[-3:])))