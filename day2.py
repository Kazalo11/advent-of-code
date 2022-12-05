score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}
lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}
total = 0
with open('day2input.txt') as f:
    for line in f:
        line = line.strip()
        line = line.split(' ')
        if win[line[0]] == line[1]:
            total+=6
            total+=score[line[1]]
        elif draw[line[0]] == line[1]:
            total+=3
            total+=score[line[1]]
        else:
            total+=0
            total+=score[line[1]]

total2 = 0

with open('day2input.txt') as f:
    for line in f:
        line = line.strip()
        line = line.split(' ')
        if line[1] == 'X':
            total2+=score[lose[line[0]]]
        elif line[1] == 'Y':
            total2+=3
            total2+=score[draw[line[0]]]
        else:
            total2+=6
            total2+=score[win[line[0]]]


print(total2)


