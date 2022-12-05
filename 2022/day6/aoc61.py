import re
import numpy as np
with open("input.txt", encoding='utf8') as f:
    grid = []
    arr= []
    n=0
    res = ""
    for line in f:
        
        if("[" in line):
            grid.append([line[i:i+4].strip().replace(']','').replace('[','') for i in range(0,len(line),4)])
        elif n == 0 :
            arr = np.array(grid).T 
            arr = np.flip(arr,axis=1).tolist()
            arr = [[i for i in item if i != ''] for item in arr]
            n+=1
        elif line.strip() =="":
            continue
        else:
            a,quant,b,frm,c,to = [i for i in re.split(" ", line.strip())]
            quant = int(quant)
            frm = int(frm)
            to = int(to)
            for i in range(0,quant):    
                arr[to-1].append(arr[frm-1].pop())
    for i in arr:
        res= res + i[len(i)-1]       

    print(res)    


