
system = [["/", "", 0, True,0]]
currentDir = "/"
currentDirIndex = 0
lines = open("input.txt", encoding='utf8')


def indexOfCurrentDir(dirName):
    index = 0
    for dir in system:
        if dir[0] == dirName:
            return index
        index+=1
    return -1


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
        system.append([currentCommand[1], currentDir, 0, True,currentDirIndex])
    else:
        system.append([currentCommand[1], currentDir,int(currentCommand[0]), False,currentDirIndex])
        changesizeOf = currentDir
        indeks = currentDirIndex

        while True:
            system[indeks][2] = system[indeks][2]+int(currentCommand[0])
            if system[indeks][0] == "/":
                break
            indeks = system[indeks][4]
            
unusedSpace = 70000000-system[0][2] #needs to be at least 300000

delete = "/"
sizeofDel = system[0][2]
ind = 0
for i in system:
    if ((unusedSpace+ i[2]) >= 30000000):
        if(i[2] < sizeofDel):
            sizeofDel = i[2]
            delete = i[0]
print(sizeofDel)
