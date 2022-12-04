import re

with open("input.txt", encoding='utf8') as f:
    grid = []
    reg = ",|-"
    sum=0
    for line in f:
        curr = [int(i) for i in re.split(reg, line.strip())]
        grid.append([int(i) for i in re.split(reg, line.strip())])
        part1 = range(curr[0],curr[1]+1)
        part2 = range(curr[2],curr[3]+1)
        
        if(set(part1).intersection(set(part2))):
            sum+=1

    print(sum)

