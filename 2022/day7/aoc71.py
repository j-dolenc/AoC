import re
import numpy as np
with open("input.txt", encoding='utf8') as f:
    grid = []
    
    res = 0
    for line in f:
        #print(line)
        for i in range(len(line)- 3):
            curr = ""
            for j in range(i,i+4):
                curr= curr + line[j]
            if len(set(curr)) == len(curr):
                res = i + 4
                print(res)
                break
            curr = ""

            
    
        
   


