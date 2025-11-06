
def part2(nums, changedOnce):
    direction = 0
    
    for i in range(len(line_nums)):
        if(i == 0):
            continue
        if(i ==1):
            if(line_nums[i] > line_nums[i-1]):
                direction = 1
            else:
                direction = -1
        if(direction == 1):
            if(line_nums[i] < line_nums[i-1]):
                #remove this element and call part2 again
                if(changedOnce):
                    return 0
                else:
                    return part2(nums[:i]+nums[i+1:], True)
                
        if(direction == -1):
            if(line_nums[i] > line_nums[i-1]):
                #remove this element and call part2 again
                if(changedOnce):
                    return 0
                else:
                    return part2(nums[:i]+nums[i+1:], True)
        if(abs(line_nums[i] - line_nums[i-1]) > 3 or line_nums[i] == line_nums[i-1]):
            if(changedOnce):
                return 0
            else:
                return part2(nums[:i]+nums[i+1:], True)
    return direction


f = open("day2.txt", encoding="utf8")
sum = 0
for line in f:
    line_nums = list(map(int, line.split()))
    #if gradually increasing or gradually decreasing and max difference between adjacent is 3 then ad 1 to sum
    direction = 0
    for i in range(len(line_nums)):
        if(i == 0):
            continue
        if(i ==1):
            if(line_nums[i] > line_nums[i-1]):
                direction = 1
            else:
                direction = -1
        if(direction == 1):
            if(line_nums[i] < line_nums[i-1]):
                direction = 0
                break
        if(direction == -1):
            if(line_nums[i] > line_nums[i-1]):
                direction = 0
                break
        if(abs(line_nums[i] - line_nums[i-1]) > 3 or line_nums[i] == line_nums[i-1]):
            direction = 0
            break
    if(direction != 0):
        sum+=1
    print(direction)
print(sum)



f = open("day2.txt", encoding="utf8")
sum = 0
for line in f:
    line_nums = list(map(int, line.split()))
    #if gradually increasing or gradually decreasing and max difference between adjacent is 3 then ad 1 to sum
    part2(line_nums,False)
    if(part2(line_nums,False) != 0):
        sum+=1

print(sum)


