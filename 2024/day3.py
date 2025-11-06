import re

f = open("day3.txt", encoding="utf8")

lines = f.readlines()
#fuse all the lines into one string in lines variable
lines = "".join(lines)


# reg for "mul(x1,x2)" and then save them as tuples in a list
reg = re.compile(r"mul\((\d+),(\d+)\)")
matches = reg.findall(lines)
print(matches)
sum = 0
for match in matches:
    sum += int(match[0]) * int(match[1])
print(sum)


#part 2
#in the string there are do() and don't() operations 
#remove all parts of the string that are between "don't()"'s and "do()"s
result = re.sub(r"don't\(\).*?do\(\)", "", lines)

print(result) 
#then do the same as in part 1


