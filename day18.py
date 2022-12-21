cubes = []
open_sides = []
with open('day18input.txt') as f:
    for line in f:
        line = line.strip()
        line = [int(i) for i in line.split(',')]
        cubes.append(line)
        open_sides.append(6)

subtract = 0
for i in range(len(cubes)):
    current = cubes[i]
    for j in range(len(cubes)):
        if i != j:
            test = cubes[j]
            diff = [x-y for x,y in zip(current,test)]
            diff2 = sorted(abs(i) for i in diff)
            if diff2 == [0,0,1]:
                open_sides[i]-=1
            if diff2 == [0,0,2]:
                find = [m - n/2 for m,n in zip(current,diff)]
                if find not in cubes:
                    subtract+=6

print(sum(open_sides)-subtract)








