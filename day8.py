
grid = []
with open('day8input.txt') as f:
    for line in f:
        line = line.strip()
        line = [int(i) for i in line]
        grid.append(line)

count = 0

def find_column(i,j,k):
    answer = []
    for z in range(i,k):
        answer.append(grid[z][j])
    return answer


for i in range(len(grid)):
    for j in range(len(grid[0])):
        test = grid[i][j]
        if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1:
            count+=1
        elif test > max(grid[i][0:j]):
            count+=1
        elif test > max(find_column(0,j,i)):
            count+=1
        elif test > max(grid[i][j+1:len(grid[0])]):
            count+=1
        elif test > max(find_column(i+1,j,len(grid))):
            count+=1

print(count)
answer = 0

def sienic(x,y):
    if len(x) == 0:
        return 0
    if y > max(x):
        return len(x)
    value = 1
    for i in x:
        if y > i:
            value+=1
        else:
            return value
    return value

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) == (3,2):
            print('Found')
        tree = grid[i][j]
        test1 = grid[i][0:j]
        test1.reverse()
        test1 = sienic(test1,tree)
        test2 = find_column(0,j,i)
        test2.reverse()
        test2 = sienic(test2, tree)
        test3 = grid[i][j+1:len(grid[0])]
        test3 = sienic(test3,tree)
        test4 = find_column(i+1,j,len(grid))
        test4 = sienic(test4,tree)
        score = test1*test2*test3*test4
        if score > answer:
            answer = score
            print((i,j))
print(answer)



