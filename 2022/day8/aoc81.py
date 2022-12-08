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
            continue
        else:
            visibility = [1,1,1,1]
            #LEFT [i][k]
            for k in range(0,j):
                if forest[i][k] >= current:
                    visibility[0] = 0
                    break

            #RIGHT[i][k]
            for k in range(j+1,nColumns):
                if forest[i][k] >= current:
                    visibility[1] = 0
                    break

            #UP[k][j]
            for k in range(0,i):
                if forest[k][j] >= current:
                    visibility[2] = 0
                    break

            #DOWN[k][j]
            for k in range(i+1,nLines):
                if forest[k][j] >= current:
                    visibility[3] = 0
                    break
            
            if not all(i == 0 for i in visibility):
                isVisible[i][j] = 1

res = 0
for i in isVisible:
    res+= sum(i)
print(res)
