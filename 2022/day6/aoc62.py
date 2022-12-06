import re
import numpy as np
with open("input.txt", encoding='utf8') as f:
    grid = []
    
    res = 0
    for line in f:
        #print(line)
        for i in range(len(line)- 13):
            curr = ""
            for j in range(i,i+14):
                curr= curr + line[j]
            if len(set(curr)) == len(curr):
                res = i + 14
                print(res)
                break
            