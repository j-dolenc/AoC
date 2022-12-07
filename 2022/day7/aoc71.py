import re
import numpy as np

#poisci curr in vrni starsev string
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
            sums+=i[2]
    return sums

#./2022/day7/
lines = open("input.txt", encoding='utf8')
dirs = [["/", "", 0, True]]
#dirs = [["imedira", "fotr", "size", isDir], ["imedira2","fotr","size", isDir]]
cmnds = []
curr = "/"
last = "/"
currIndex = 0
ls = False

for line in lines:
    currCmnd = line.strip().split(" ")
    #cmnds.append(line.strip().split(" "))

    #listamo direktorij
    if ls and currCmnd[0] != "$":
        

        #ce je dir
        if currCmnd[0] == "dir":

            print("ls dir: " + currCmnd[1])

            #preverimo ce imamo direktorij ze v gridu
            exists= exist(dirs,currCmnd[1])
            
            #ce ga nimamo ga dodamo
            if not exists:    
                dirs.append([currCmnd[1],curr,0,True])
                #print(dirs)

    	#ce je file
        else: 
            #dodamo ga v grid kot file isDir = False, dodamo size, dodamo size vsem njegovim starsem...
            exists = exist(dirs,currCmnd[1])
            if not exists:
                dirs.append([currCmnd[1],curr,0,True])
                koren = curr
                #do korena dodajas size fila
                while True :
                    #poisces trenutnega in mu didas size
                    index = findCurr(dirs, koren)
                    
                    dirs[index][2] += int(currCmnd[0])
                    if(koren == "/"):
                        break
                    koren = dirs[index][1]
                    

            print("ls file: " + currCmnd[1])


    #command is cd or ls

    if currCmnd[0] == "$":

        # ce je komanda cd
        if currCmnd[1] == "cd":
            ls = False
            

            # ce je komanda za nazaj, current nastavimo na starsa
            if currCmnd[2] == "..":
                # poisci curr v dirs in nastavi curr na starsa dirs[curr][1]
                print("go back")
                curr =findParent(dirs, curr)
            
            # komanda gre naprej na nekega sina
            else:

                print("move to: " + currCmnd[2])
                #preverimo ce sin ze obstaja v gridu
                exists = exist(dirs,currCmnd[2])

                # ce ne obstaja ga ustvarimo
                if not exists:    
                    dirs.append([currCmnd[2],curr,0,True])
                    #print(dirs)

                #spremenimo trenutni direktorij
                curr = currCmnd[2]

        #ce je komanda ls damo flag ls
        elif currCmnd[1] == "ls":
            ls = True
            print("start ls:")
    

print(result(dirs))



#for line in f:
#    print(line.strip())


