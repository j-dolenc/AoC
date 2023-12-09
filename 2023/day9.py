f = open("day9.txt", "r")

lines = [line.replace("\n", "").split(" ") for line in f if line != "\n"]



sum_of_last_nums = 0
sum_of_first_nums = 0

for line in lines:
    numbers = [int(num) for num in line]
    
    new_array = []
    for i in range(len(numbers)-1):
        new_array.append(numbers[i+1]-numbers[i])
    
    all_numbers = []
    all_numbers.append(new_array)
    
    while(new_array != [0]*len(new_array)):
        
        last_array = new_array.copy()
        new_array = []

        for i in range(len(last_array)-1):
            new_array.append(last_array[i+1]-last_array[i])
    
        all_numbers.append(new_array)
    

    i =  len(all_numbers)-1
    part_sum = 0
    while(i>0):
        all_numbers[i-1].append(all_numbers[i][-1]+ all_numbers[i-1][-1])
        all_numbers[i-1].insert(0,all_numbers[i-1][0]-all_numbers[i][0])
        i-=1
    
    numbers.append(all_numbers[0][-1] + numbers[-1])
    numbers.insert(0,numbers[0]-all_numbers[0][0])
    
    sum_of_last_nums+=numbers[-1]
    sum_of_first_nums+=numbers[0]
    
print("Part 1: ",sum_of_last_nums)
print("Part 2: ",sum_of_first_nums)
