f= open("day6.txt", encoding='utf8')

lines = []
for line in f:
    #out with empty lines
    if line != "\n":
        lines.append(line.replace("\n","").split(": ")[1])

print(lines)

times = [int(x) for x in lines[0].split(" ") if x.isdigit()]
distances = [int(x) for x in lines[1].split(" ") if x.isdigit()]

print(times)
print(distances)

ways_to_beat = []
for i in range(len(times)):
    sum_of_ways = 0
    for j in range(times[i]):
        speed = j
        time_left = times[i] - j
        distance = speed * time_left
        if distance > distances[i]:
            sum_of_ways += 1
    ways_to_beat.append(sum_of_ways)
#print(ways_to_beat)

#multiply all elements in ways_to_beat
margin = 1
for i in ways_to_beat:
    margin *= i
print("Part 1: ",margin)

#Part 2
f= open("day6.txt", encoding='utf8')

f= open("day6.txt", encoding='utf8')

lines = []
for line in f:
    #out with empty lines
    if line != "\n":
        lines.append(line.replace("\n","").split(": ")[1])

print(lines)

times2 = int(lines[0].replace(" ",""))
distances2 = int(lines[1].replace(" ",""))
sum_of_ways = 0
for j in range(times2):
    speed = j
    time_left = times2 - j
    distance = speed * time_left
    if distance > distances2:
        
        sum_of_ways += 1
print("Part 2: ",sum_of_ways)