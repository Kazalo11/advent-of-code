import ast
import itertools

count = 0
test1 = []
test2 = []
indices = []
order = True




with open('day13input.txt') as f:
    for line in f:
        order = True
        line = line.strip()
        if len(line) != 0:
            line = ast.literal_eval(line)
            if count % 2 == 0:
                test1 = list(itertools.chain(*line))
            else:
                test2 = list(itertools.chain(*line))
            count+=1
        else:
            if len(test1) > len(test2):
                continue
            for i in range(len(min(test1,test2))):
                if test1[i] > test2[i]:
                    order = False
                    break
            if order:
                indices.append(count//2)









