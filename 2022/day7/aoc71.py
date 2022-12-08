system = [["/", "", 0, True,0]]
currentDir = "/"
currentDirIndex = 0
lines = open("input.txt", encoding='utf8')

for line in lines:
    
    currentCommand = line.strip().split(" ")
    
    if currentCommand[0] == "$":
        if currentCommand[1] == "cd":
            
            if currentCommand[2] == "/":
                currentDir = "/"
                currentDirIndex = 0

            elif currentCommand[2] == "..":  
                currentDir = system[currentDirIndex][1]
                currentDirIndex =  system[currentDirIndex][4]
            
            else:
                currentDir = currentCommand[2]
                ind = 0
                
                for i in system:
                    if i[4] == currentDirIndex and currentDir == i[0]:
                        break
                    ind+=1
                currentDirIndex = ind
                
        else:
            continue
    elif currentCommand[0] == "dir":
        #print("Found dir: " + currentCommand[1])
        system.append([currentCommand[1], currentDir, 0, True,currentDirIndex])
    else:
        #print("Found file: " + currentCommand[1] + " of size " + currentCommand[0])
        system.append([currentCommand[1], currentDir,int(currentCommand[0]), False,currentDirIndex])
        changesizeOf = currentDir
        indeks = currentDirIndex

        while True:
            system[indeks][2] = system[indeks][2]+int(currentCommand[0])
            if system[indeks][0] == "/":
                break
            indeks = system[indeks][4]
         
sums =0

for i in system:
    if i[3] and i[2] < 100000 :
        sums+=i[2]
        
print(sums)