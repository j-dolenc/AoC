f = open("day11.txt", "r")

lines = [line.replace("\n", "") for line in f if line != "\n"]
lines = [[char for char in line] for line in lines]
print(lines)

uid = 0
galaxies = []
for i in range(len(lines)):

    
    for j in range(len(lines[i])):
        if(lines[i][j] == "#"):
            galaxies.append([i,j])
            lines[i][j] = str(uid)
            uid+=1
            
print(lines)
only_dots_i = []
only_dots_j = []
for i in range(len(lines)):
    if(lines[i].count(".")) == len(lines[i]):
        only_dots_i.append(i)
for i in range(len(lines[0])):
    if([line[i] for line in lines].count(".")) == len(lines):
        only_dots_j.append(i)
print(only_dots_i)
print(only_dots_j)
only_dots_i.reverse()
only_dots_j.reverse()

#next to index in only_dots_i add additonal row
#next to index in only_dots_j add additonal column
for i in only_dots_i:
    lines.insert(i,["." for j in range(len(lines[0]))])
for i in range(len(lines)):
    for j in only_dots_j:
        lines[i].insert(j,".")
for line in lines:
    print(line)

#uid+=1
#grid of zeros for uid*uid
grid = [[0 for i in range(uid)] for j in range(uid)]
print(grid)
#fill grid with distances between galaxies
for i in range(len(galaxies)):
    for j in range(len(galaxies)):
        grid[i][j] = abs(galaxies[i][0]-galaxies[j][0])+abs(galaxies[i][1]-galaxies[j][1])
for line in grid:
    print(line)

all_sum = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        all_sum+=grid[i][j]

all_sum = all_sum/2
print(all_sum)