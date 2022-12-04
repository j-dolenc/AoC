
import re

with open("input.txt", encoding='utf8') as f:
    grid = []
    reg = ",|-"
    sum=0

    for line in f:
        curr = [int(i) for i in re.split(reg, line.strip())]
        if (curr[0] >= curr[2] and curr[1]<=curr[3]) or (curr[0] <= curr[2] and curr[1]>=curr[3]):
            sum+=1

    print(sum)
