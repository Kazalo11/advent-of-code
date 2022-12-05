total = 0
matching = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open('day3input.txt') as f:
    for line in f:
        line = line.strip()
        r1,r2 = line[:len(line )//2],line[len(line )//2:]
        similar = list((set(r1) & set(r2)))[0]
        total = total+ matching.index(similar)+1

total2 = 0
complete = []
with open('day3input.txt') as f:
    for line in f:
        line=line.strip()
        complete.append(line)

for i in range(0,len(complete),3):
    c1 = list(set(complete[i]) & set(complete[i+1]) & set(complete[i+2]))[0]
    total2 = total2 + matching.index(c1)+1

print(total2)



