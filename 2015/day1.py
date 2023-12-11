f = open("day1.txt", "r")

lines = [line.replace("\n", "") for line in f if line != "\n"]
line = lines[0]

floor = 0
basement = 0
found_basement = False

for i in range(len(line)):
    if(line[i] =="("):
        floor+=1
    else:
        floor-=1
    if(not found_basement and floor == -1):
        basement = i+1
        found_basement = True
        

#print(line)
print(floor)
print(basement)