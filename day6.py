count = 0

with open('day6input.txt') as f:
    for line in f:
        line = line.strip()
        unique = list(line)

for i in range(len(unique)-3):
    if len(set(unique[i:i+4])) == 4:
        print(i+4)
        break

for i in range(len(unique)-14):
    if len(set(unique[i:i+14])) == 14:
        print(i+14)
        break
