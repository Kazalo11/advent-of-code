answer = []
nodes = []
count = []
with open('day20input.txt') as f:
    for line in f:
        line = int(line.strip())
        nodes.append(line)
        answer.append(line)
        count.append(nodes.count(line))

start = 0
for i in range(len(nodes)):
    j = 1
    for k in range(len(answer)):
        if answer[k] == nodes[i]:
            if j == count[i]:
                start = k
                break
            else:
                j+=1
    if nodes[i] < 0:
        val = len(nodes)+nodes[i]-1
    else:
        val = nodes[i]
    for _ in range(val):
        if start == len(nodes)-1:
            temp = answer[start]
            del answer[start]
            answer.insert(1,temp)
            start = 1
            continue
        else:
            z = start+1
        answer[start],answer[z] = answer[z],answer[start]
        start+=1


inital = answer.index(0)

while len(answer) < (answer.index(0)+3001):
    answer = answer+answer

answer = answer[inital+1:]
print(answer[999]+answer[1999]+answer[2999])









