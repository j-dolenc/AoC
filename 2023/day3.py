f = open("day3.txt", encoding='utf8')

sum_of_parts = 0

#put lines into array without \n
lines = []
for line in f:
    lines.append(line.replace("\n", ""))
#print(lines)

for index in range(len(lines)):
    line = lines[index]
    char_index = 0
    while char_index < len(line):
        char = line[char_index]
        
        skip_index = 1
        if char.isdigit():
            # get rest of the number
            has_adjacent_symbol = False    
            num = ""
            i = char_index
            
            while i < len(line) and line[i].isdigit():
                if index > 0:
                    if lines[index - 1][i] != "." :
                        has_adjacent_symbol = True
                    if i > 0:
                        if lines[index - 1][i - 1] != ".":
                            has_adjacent_symbol = True
                    if i < len(line) - 1:
                        if lines[index - 1][i + 1] != ".":
                            has_adjacent_symbol = True
                if index < len(lines) - 1:
                    if lines[index + 1][i] != "." :
                        has_adjacent_symbol = True
                    if i > 0:
                        if lines[index + 1][i - 1] != ".":
                            has_adjacent_symbol = True
                    if i < len(line) - 1:
                        if lines[index + 1][i + 1] != ".":
                            has_adjacent_symbol = True
                if i > 0:
                    if line[i - 1] != "." and not line[i - 1].isdigit():
                        has_adjacent_symbol = True
                if i < len(line) - 1:
                    if line[i + 1] != "." and not line[i + 1].isdigit():
                        has_adjacent_symbol = True
                num += line[i]
                i += 1
            if has_adjacent_symbol:
                sum_of_parts += int(num)


            skip_index = len(num)
            #print(len(num))
            #print(num)
            
        char_index += skip_index

print(sum_of_parts)


f = open("day3.txt", encoding='utf8')

gear_sum = 0


for index in range(len(lines)):
    line = lines[index]

    char_index = 0
    while char_index < len(line):
        char = line[char_index]
        
        if(char == "*"):
            adjacent_numbers = []
            

            #right
            if char_index < len(line) - 1:
                if line[char_index + 1].isdigit():
                    
                    i = char_index + 1
                    full_number = ""
                    while i < len(line) and line[i].isdigit():
                        full_number += line[i]
                        i += 1
                    adjacent_numbers.append(int(full_number))   
            #left
            if char_index > 0:
                if line[char_index - 1].isdigit():
                    
                    i = char_index - 1
                    full_number = ""
                    while i >= 0 and line[i].isdigit():
                        full_number = line[i] + full_number
                        i -= 1
                    adjacent_numbers.append(int(full_number))
            #up
            if index > 0:
                number_start = char_index
                direct_up = False
                #up
                if lines[index - 1][char_index].isdigit():
                    direct_up = True
                    i = char_index
                    while i >= 0 and lines[index - 1][i].isdigit():
                        i -= 1
                    number_start = i + 1
                    #iterate to end of number to get full number and add to adjacent numbers
                    i = number_start
                    full_number = ""
                    while i < len(line) and lines[index - 1][i].isdigit():
                        full_number += lines[index - 1][i]
                        i += 1
                    adjacent_numbers.append(int(full_number))
                    
                if not direct_up:
                    #left
                    if char_index > 0:
                        if lines[index - 1][char_index - 1].isdigit():
                            #iterate to start of number to get full number and add to adjacent numbers
                            i = char_index - 1
                            full_number = ""
                            while i >= 0 and lines[index - 1][i].isdigit():
                                full_number = lines[index - 1][i] + full_number
                                i -= 1
                            adjacent_numbers.append(int(full_number))
                            
                    #right
                    if char_index < len(line) - 1:
                        if lines[index - 1][char_index + 1].isdigit():
                            #iterate to end of number to get full number and add to adjacent numbers
                            i = char_index + 1
                            full_number = ""
                            while i < len(line) and lines[index - 1][i].isdigit():
                                full_number += lines[index - 1][i]
                                i += 1
                            adjacent_numbers.append(int(full_number))
            #down
            if index < len(lines) - 1:
                number_start = char_index
                direct_down = False
                #down
                if lines[index + 1][char_index].isdigit():
                    direct_down = True
                    i = char_index
                    while i < len(line) and lines[index + 1][i].isdigit():
                        i += 1
                    number_start = i - 1
                    #iterate to end of number to get full number and add to adjacent numbers
                    i = number_start
                    full_number = ""
                    while i >= 0 and lines[index + 1][i].isdigit():
                        full_number = lines[index + 1][i] + full_number
                        i -= 1
                    adjacent_numbers.append(int(full_number))
                if not direct_down:
                    #left
                    if char_index > 0:
                        if lines[index + 1][char_index - 1].isdigit():
                            #iterate to start of number to get full number and add to adjacent numbers
                            i = char_index - 1
                            full_number = ""
                            while i >= 0 and lines[index + 1][i].isdigit():
                                full_number = lines[index + 1][i] + full_number
                                i -= 1
                            adjacent_numbers.append(int(full_number))
                            
                    #right
                    if char_index < len(line) - 1:
                        if lines[index + 1][char_index + 1].isdigit():
                            #iterate to end of number to get full number and add to adjacent numbers
                            i = char_index + 1
                            full_number = ""
                            while i < len(line) and lines[index + 1][i].isdigit():
                                full_number += lines[index + 1][i]
                                i += 1
                            adjacent_numbers.append(int(full_number))
            #print(adjacent_numbers)
            if len(adjacent_numbers) == 2:
                gear_sum += adjacent_numbers[0] * adjacent_numbers[1]

        char_index += 1
print(gear_sum)

        
            
        