count = 0

with open('day4input.txt') as f:
    for line in f:
        line = line.strip()
        p1,p2 = line.split(',')
        l1,l2 = p1.split('-')
        l3,l4 = p2.split('-')
        l1 = int(l1)
        l2 = int(l2)
        l3 = int(l3)
        l4 = int(l4)
        if l1 <= l3 and l2 >= l4:
            count+=1
        elif l3 <= l1 and l4 >= l2:
            count+=1
print(count)

count2 = 0
with open('day4input.txt') as f:
    for line in f:
        line = line.strip()
        p1,p2 = line.split(',')
        l1,l2 = p1.split('-')
        l3,l4 = p2.split('-')
        l1 = int(l1)
        l2 = int(l2)
        l3 = int(l3)
        l4 = int(l4)
        if l1 <= l3 <= l2 <= l4:
            count2+=1
        elif l3 <= l1 <= l4 <= l2:
            count2+=1
        elif l1 <= l3 and l2 >= l4:
            count2+=1
        elif l3 <= l1 and l4 >= l2:
            count2+=1



print(count2)

