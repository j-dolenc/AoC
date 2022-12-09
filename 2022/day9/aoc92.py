lines = open("input.txt", encoding="utf8")

headPos = [0,0]

tailPos2 = [[0,0] for i in range(0,10)]
visited = [[0,0]]

for line in lines:

    command = [i for i in line.strip().split()]
    direction = command[0]
    steps = int(command[1])

    for i in range(0,steps):
        
        if(direction == 'L'):
            headPos[0] -= 1
        elif(direction == 'R'):
            headPos[0] += 1
        elif(direction == 'U'):
            headPos[1] += 1
        elif(direction == 'D'):
            headPos[1] -= 1

        tempPos= [headPos[0],headPos[1]]

        for i in range(0,10):
            knot= [tailPos2[i][0],tailPos2[i][1]]
            
            colDist = tempPos[0] - knot[0] #levo desno
            lineDist = tempPos[1] - knot[1] #gor dol

            if not ((abs(colDist) == 1 and abs(lineDist) == 1) or \
                (abs(lineDist) == 1 and colDist == 0) or \
                (abs(colDist) == 1 and lineDist == 0) or \
                (colDist == 0 and lineDist == 0)) :
                if(colDist > 0):
                    knot[0]+=1
                elif(colDist < 0):
                    knot[0]-=1
                if(lineDist > 0):
                    knot[1]+=1
                elif(lineDist < 0):
                    knot[1]-=1  

            tailPos2[i] =[knot[0],knot[1]]

            tempPos = knot
        
        if not (tailPos2[8] in visited):
            visited.append([tailPos2[8][0],tailPos2[8][1]])
    
print(len(visited))