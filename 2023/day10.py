f = open("day10.txt", "r")

lines = [line.replace("\n", "") for line in f if line != "\n"]
lines = [[char for char in line] for line in lines]
#print(lines)

starting_pos = [0,0]
i = 0
for i in range(len(lines)):
    line = lines[i]
    found = False
    for j in range(len(line)):
        if(line[j] == "S"):
            starting_pos = [i,j]
            found = True
            break
    if(found):
        break
# print(starting_pos)
# print("desno",lines[starting_pos[0]][starting_pos[1]+1])
# print("levo",lines[starting_pos[0]][starting_pos[1]-1])
# print("gor",lines[starting_pos[0]-1][starting_pos[1]])
# print("dol",lines[starting_pos[0]+1][starting_pos[1]])

current_pos = starting_pos.copy()
            
prev_position = starting_pos.copy()
current_position = [starting_pos[0],starting_pos[1]+1]
path = []
path.append(starting_pos)

path_2d = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
path_2d[starting_pos[0]][starting_pos[1]] = 1
while(lines[current_position[0]][current_position[1]] != "S"):
    current_pipe = lines[current_position[0]][current_position[1]]
    path.append(current_position)
    path_2d[current_position[0]][current_position[1]] = 1
    if(current_pipe == "|"):
        if(current_position[0] < prev_position[0]):
            #going up
            prev_position = current_position.copy()
            current_position = [current_position[0]-1,current_position[1]]
            #current_position[0]-=1
        else:
            #going down
            prev_position = current_position.copy()
            #current_position[0]+=1
            current_position = [current_position[0]+1,current_position[1]]
    if(current_pipe == "-"):
        if(current_position[1] < prev_position[1]):
            #going left
            prev_position = current_position.copy()
            #current_position[1]-=1
            current_position = [current_position[0],current_position[1]-1]
        else:
            #going right
            prev_position = current_position.copy()
            #current_position[1]+=1
            current_position = [current_position[0],current_position[1]+1]
    if(current_pipe == "L"):
        if(current_position[1] == prev_position[1]):
            #go right
            prev_position = current_position.copy()
            #current_position[1]+=1
            current_position = [current_position[0],current_position[1]+1]
        else:
            #go up
            prev_position = current_position.copy()
            #current_position[0]-=1
            current_position = [current_position[0]-1,current_position[1]]
    if(current_pipe == "J"):
        if(current_position[1] == prev_position[1]):
            #go left
            prev_position = current_position.copy()
            #current_position[1]-=1
            current_position = [current_position[0],current_position[1]-1]
        else:
            #go up
            prev_position = current_position.copy()
            #current_position[0]-=1
            current_position = [current_position[0]-1,current_position[1]]
    if(current_pipe == "7"):
        if(current_position[1] == prev_position[1]):
            #go left
            prev_position = current_position.copy()
            #current_position[1]-=1
            current_position = [current_position[0],current_position[1]-1]
        else:
            #go down
            prev_position = current_position.copy()
            #current_position[0]+=1
            current_position = [current_position[0]+1,current_position[1]]
    if(current_pipe == "F"):
        if(current_position[1] == prev_position[1]):
            #go right
            prev_position = current_position.copy()
            #current_position[1]+=1
            current_position = [current_position[0],current_position[1]+1]
        else:
            #go down
            prev_position = current_position.copy()
            #current_position[0]+=1
            current_position = [current_position[0]+1,current_position[1]]
    if(current_pipe == "."):
        print("error")
        break
    #print(current_position)
#print(path_2d)
print("Part 1: ",int(len(path)/2))

enclosed_area = 0
#find all positions that are enclosed



