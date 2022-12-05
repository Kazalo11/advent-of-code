stack_1 = ['W', 'B', 'D', 'N', 'C', 'F', 'J']
stack_2 = ['P', 'Z', 'V', 'Q', 'L', 'S', 'T']
stack_3 = ['P', 'Z', 'B', 'G', 'J', 'T']
stack_4 = ['D', 'T', 'L', 'J', 'Z', 'B', 'H', 'C']
stack_5 = ['G', 'V', 'B', 'J', 'S']
stack_6 = ['P', 'S', 'Q']
stack_7 = ['B', 'V', 'D', 'F', 'L', 'M', 'P', 'N']
stack_8 = ['P', 'S', 'M', 'F', 'B', 'D', 'L', 'R']
stack_9 = ['V', 'D', 'T', 'R']

# crates = eval(f'stack_{start}[-{amount_moved}:]')
#         crates.reverse()

stacks = [stack_1,stack_2,stack_3,stack_4,stack_5,stack_6,stack_7,stack_8,stack_9]

with open('day5input.txt') as f:
    for line in f:
        line = line.strip()
        line = line.split(" ")
        amount_moved = int(line[1])
        start = int(line[3])
        end = int(line[-1])
        crates = stacks[start-1][-amount_moved:]
        # crates.reverse() remove for part 2
        del stacks[start-1][-amount_moved:]
        stacks[end-1] = stacks[end-1] + crates

answer = ""
for i in stacks:
    answer+=i[-1]
print(answer)








