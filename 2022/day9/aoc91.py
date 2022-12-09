lines = open("input.txt", encoding="utf8")

headPos = [0,0]
tailPos = [0,0]

print(tailPos)

visited = [[0,0]]


for line in lines:

    command = [i for i in line.strip().split()]
    direction = command[0]
    steps = int(command[1])

    
    #headPos[0] -= steps
    for i in range(0,steps):
        if(direction == 'L'):
            #print("LEFT")
            headPos[0] -= 1
        elif(direction == 'R'):
            #print("RIGHT")
            headPos[0] += 1
        elif(direction == 'U'):
            #print("UP")
            headPos[1] += 1
        elif(direction == 'D'):
            #print("DOWN")
            headPos[1] -= 1
        
        colDist = headPos[0] - tailPos[0]
        lineDist = headPos[1] - tailPos[1]
        
        #print(headPos)
        #check if head is one away:
        if(abs(colDist) == 1 and abs(lineDist) == 1) or \
            (abs(lineDist) == 1 and colDist == 0) or \
            (abs(colDist) == 1 and lineDist == 0) or \
            (colDist == 0 and lineDist == 0) :
            continue
        else:
            if(colDist > 0):
                tailPos[0]+=1
            elif(colDist < 0):
                tailPos[0]-=1
            if(lineDist > 0):
                tailPos[1]+=1
            elif(lineDist < 0):
                tailPos[1]-=1
            #print(tailPos)

        if not (tailPos in visited):
            visited.append([tailPos[0],tailPos[1]])
    #print(headPos)
    #print(tailPos)


    
    
print(len(visited))