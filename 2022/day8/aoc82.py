import numpy as np
lines = open("input.txt", encoding='utf8')

forest = [[int(i) for i in line.strip()] for line in lines]
isVisible = [[0 for i in line] for line in forest]
nLines = len(forest)
nColumns = len(forest[0])


isVisible[0] = [1 for i in forest[0]]
isVisible[nLines-1] = [1 for i in forest[0]]
for i in range(0,nLines):
    isVisible[i][0] = 1
    isVisible[i][nColumns-1] = 1

for i in range(0,nLines):
    
    for j in range(0,nColumns):
        current = forest[i][j]
        visibility = isVisible[i][j]
        if visibility:
            #print("EDGE")
            isVisible[i][j] = 0
            continue
        else:
        
            visibility = [0,0,0,0]
            
            for k in range(j-1,-1,-1): 
                visibility[0]+=1
                if(forest[i][k] >= current):
                    break

            #RIGHT[i][k]
            for k in range(j+1,nColumns): 
                visibility[1]+=1
                if(forest[i][k] >= current):
                    break

            #UP[k][j]
            for k in range(i-1,-1,-1): 
                visibility[2]+=1
                if(forest[k][j] >= current):
                    break

            #DOWN[k][j]
            for k in range(i+1,nLines): 
                visibility[3]+=1
                if(forest[k][j] >= current):
                    break
            
            isVisible[i][j] = int(np.prod(visibility))
        
res = 0
for i in isVisible:
    for j in i:
        if(j > res):
            res = j
print(res)
