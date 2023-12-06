f =open("day5.txt", encoding='utf8')

lines = []
for line in f:
    #out with empty lines
    if line != "\n":
        lines.append(line.replace("\n",""))

current = [int(x) for x in lines[0].split(": ")[1].split(" ")]


#print(current)
lines.pop(0)

changed_arr = [0 for _ in range(len(current))]
i = 0
while i < len(lines):
    line = lines[i]
    if(not line[0].isdigit()):
        
        changed_arr = [0 for _ in range(len(current))]
        i+=1
        #print(line)
        continue

    #print(line)
    numbers = [int(x) for x in line.split(" ")]
    #print(numbers)
    dest_range_start = numbers[0]
    src_range_start = numbers[1]
    range_length = numbers[2]
    dest_range_end = dest_range_start + range_length
    src_range_end = src_range_start + range_length
    
    for j in range(len(current)):
        if(current[j] >= src_range_start and current[j] < src_range_end and changed_arr[j] == 0):
            current[j] = dest_range_start + (current[j] - src_range_start)
            changed_arr[j] = 1
            #print("current: " + str(current[j]))
        
    i+=1

print("Part 1: ",min(current))


#Part 2

f =open("day5.txt", encoding='utf8')

lines = []
for line in f:
    #out with empty lines
    if line != "\n":
        lines.append(line.replace("\n",""))

seed_line = [int(x) for x in lines[0].split(": ")[1].split(" ")]

i = 0
current= []
while i < len(seed_line):
    #print(i)
    
    start = seed_line[i]
    range_length = seed_line[i+1]
    #print("start: " + str(start))
    #print("range_length: " + str(range_length))
    current.append((start,start+range_length-1))
    i+=2
#print(current)
lines.pop(0)

changed_arr = [0 for _ in range(len(current))]
i = 0
while i < len(lines):
    line = lines[i]
    if(not line[0].isdigit()):
        
        changed_arr = [0 for _ in range(len(current))]
        i+=1
        #print(line)
        continue

    #print(line)
    numbers = [int(x) for x in line.split(" ")]
    #print(numbers)
    dest_range_start = numbers[0]
    src_range_start = numbers[1]
    range_length = numbers[2]
    dest_range_end = dest_range_start + range_length-1
    src_range_end = src_range_start + range_length-1

    new_current = []
    new_changed = []
    
    for j in range(len(current)):
        # if(current[j] >= src_range_start and current[j] < src_range_end and changed_arr[j] == 0):
        #     current[j] = dest_range_start + (current[j] - src_range_start)
        #     changed_arr[j] = 1
            #print("current: " + str(current[j]))
        current_range_start = current[j][0]
        current_range_end = current[j][1]
        #check if src_range and current_range overlap
        #the part that doesnt overlap should be added separately to current
        #the part that does should be updated with dest
        if changed_arr[j] == 1:
            #already changed
            new_current.append(current[j])
            new_changed.append(1)
            continue
        #no overlap
        if src_range_end < current_range_start or src_range_start > current_range_end:
            new_current.append(current[j])
            new_changed.append(0)
            continue
        #src range contains current range
        if src_range_start <= current_range_start and src_range_end >= current_range_end:
            new_current.append((dest_range_start + (current[j][0] - src_range_start),dest_range_start + (current[j][1] - src_range_start)))
            new_changed.append(1)
            continue
        #partially overlap
        if current_range_start < src_range_start and current_range_end <= src_range_end:

            new_current.append((current_range_start,src_range_start-1))
            new_changed.append(0)

            new_current.append((dest_range_start,dest_range_start + (current[j][1] - src_range_start)))
            new_changed.append(1)
            continue
        #partially overlap
        if current_range_start >= src_range_start and current_range_end > src_range_end:
            new_current.append((src_range_end,current_range_end))
            new_changed.append(0)

            new_current.append((dest_range_start + (current[j][0] - src_range_start),dest_range_start + range_length))
            new_changed.append(1)
            continue
        #src contained in current
        if current_range_start < src_range_start and current_range_end > src_range_end:
            new_current.append((current_range_start,src_range_start-1))
            new_changed.append(0)

            new_current.append((dest_range_start,dest_range_start + range_length))
            new_changed.append(1)

            new_current.append((src_range_end,current_range_end))
            new_changed.append(0)
            continue

    current = new_current
    changed_arr = new_changed



            
            

    


        
    i+=1

starts = [x[0] for x in current]
print("Part 1: ",min(starts))










