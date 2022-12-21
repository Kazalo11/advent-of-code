xmin,xmax,ymax = float('inf'),0,0
coordinates = []
with open('day14input.txt') as f:
    for line in f:
        initial = []
        line = line.strip()
        line = line.replace(" ","")
        line = line.split('->')
        for item in line:
            item = [int(i) for i in item.split(',')]
            x,y = item[0],item[1]
            xmin,xmax,ymax = min(xmin,x),max(xmax,x),max(ymax,y)
            initial.append((x,y))
        coordinates.append(initial)

grid = [['.' for _ in range(xmax-xmin+1)] for _ in range(ymax)]
for item in coordinates:
    for i in range(len(item)-1):
        if item[i][0] == item[i+1][0]:
            for y in range(item[i][1],item[i+1][1]+1):
                grid[item[i][0]][y] = "#"






