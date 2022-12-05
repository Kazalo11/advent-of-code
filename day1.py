biggest = []

with open('day1input.csv') as f:
    current = 0
    for line in f:
        line= line.strip()
        if len(line) > 0:
            current+=int(line)
        else:
            biggest.append(current)
            current = 0

biggest.sort()
print(sum(biggest[-3:]))

