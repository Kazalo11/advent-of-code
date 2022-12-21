monkeys = {}
message = ""
with open('day21input.txt') as f:
    for line in f:
        line = line.strip()
        line = line.split(":")
        monkeys[line[0]] = 0
        line[1] = line[1].strip()
        if line[1].isnumeric():
            monkeys[line[0]] = float(line[1])
        else:
            monkeys[line[0]] = line[1]
        if line[0] == 'root':
            message = line[1]


# i = -9.36390562e11
count = 0
i = 3.876027196e12
found = True
monkeys2 = monkeys.copy()
while found:
    monkeys['humn'] = i
    count = 0
    for index,value in monkeys.items():
        if index == 'root':
            m1,op,m2 = value.split(' ')
            if monkeys[m1] == monkeys[m2]:
                found = False
                continue
            else:
                continue
        if isinstance(value,float):
            count+=1
        else:
            m1,op,m2 = value.split(" ")
            if isinstance(monkeys[m1],float) and isinstance(monkeys[m2],float):
                monkeys[index] = eval(f'{monkeys[m1]} {op} {monkeys[m2]}')
    if count == len(monkeys.keys())-1:
        m1,op,m2 = monkeys['root'].split(" ")
        if monkeys[m1] == monkeys[m2]:
            break
        else:
            print(f'pgnv: {monkeys["pgnv"]}, wcnp: {monkeys["wcnp"]}')
            i+=1
            count =0
            temp = monkeys2.copy()
            monkeys = monkeys2
            monkeys2 = temp

print(i)





