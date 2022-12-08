

#poisci curr in vrni starsev string
def isDescendant(grid, child, parent):
    indeks = findCurr(grid,child)
    now = grid[indeks][1]
    while True:
        if(now == parent):
            return True
        if(now == "/"):
            break
        indeks = findCurr(grid,grid[indeks][1])
        now = grid[indeks][1]
    return False

def findParent(grid, currentDir):
    for i in grid:
        if i[0] == currentDir:
            return i[1]

    return ""    

def findCurr(grid, currentDir):
    ind = 0
    for i in grid:
        if i[0] == currentDir:
            return ind
        ind+=1

    

def exist(grid, name):
    for i in grid:
            if i[0] == name:
                return 1
    return 0
                
def result(grid):
    sums =0
    for i in grid:
        if i[3] and i[2] < 100000 :
            print(i)
            sums+=i[2]
    return sums

#./2022/day7/
lines = open("input.txt", encoding='utf8')
dirs = [["/", "", 0, True]]
#dirs = [["imedira", "fotr", "size", isDir], ["imedira2","fotr","size", isDir]]
cmnds = []
curr = "/"
currIndex = 0
ls = False

for line in lines:
    currCmnd = line.strip().split(" ")
    if currCmnd[0] == "$":
        if currCmnd[1] == "cd":
            if(currCmnd[2] == "/"):
                curr = "/"
            elif currCmnd[2] == "..":
                curr = findParent(dirs,curr)
            else:
                if not exist(dirs, currCmnd[2]):
                    dirs.append([currCmnd[2],curr,0, True])
                curr = currCmnd[2]
        elif currCmnd[1] == "ls":
            continue
        
    elif currCmnd[0] == "dir":
        if not exist(dirs, currCmnd[1]):
            dirs.append([currCmnd[1],curr,0, True])
    elif currCmnd[0].isdigit():
        if not exist(dirs, currCmnd[1]):
            dirs.append([currCmnd[1],curr,int(currCmnd[0]), False])            


sestevek = 0 
for i in dirs:
    
    if i[3]:
        isum = 0
        for k in dirs:
            #check if k is descendant of i
            if not k[3]:
                #print(k[0] + " je potomec od " + i[0] + "? ")
                #print(isDescendant(dirs,k[0],i[0]))
                if isDescendant(dirs,k[0],i[0]):
                    isum+= int(k[2])
        print(isum)
        if(isum <= 100000):
            sestevek+=isum
        isum = 0

print(sestevek)    
#print(result(dirs))


#for line in f:
#    print(line.strip())


