f = open("day2.txt", "r")

lines = [line.replace("\n", "").split("x") for line in f if line != "\n"]

surface_sum = 0
total_ribbon = 0
for line in lines:
    line = [int(num) for num in line]
    #length, width, height
    #surface area = 2*l*w + 2*w*h + 2*h*l
    
    lw = line[0]*line[1]
    wh = line[1]*line[2]
    hl = line[2]*line[0]

    surface = 2*(lw+wh+hl)
    surface+= min(lw,wh,hl)
    surface_sum+=surface

    two_smallest = sorted(line)[:2]
    ribbon = 2*(two_smallest[0]+two_smallest[1])
    ribbon+= line[0]*line[1]*line[2]
    total_ribbon+=ribbon

    
print("Part 1: ",surface_sum)
print("Part 2: ",total_ribbon)

