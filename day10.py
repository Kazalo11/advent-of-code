count = 0
X = 1
total = 0
check=[20,60,100,140,180,220]
instructions = []
row = ['.']*40
picture = []
for i in range(6):
    picture.append(row)

with open('day10input.txt') as f:
    for line in f:
        line = line.strip()
        line = line.split(" ")
        if line[0] == "noop":
            instructions.append(X)
        else:
            instructions.append(X)
            X+=int(line[1])
            instructions.append(X)

for i in check:
    total+= i*instructions[i-2]




