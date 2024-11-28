f = open("day1.txt", encoding='utf8')

# numbers= []
# for line in f:
#     allnums = ''.join(filter(str.isdigit, line))
#     first = allnums[0]
#     if(len(allnums) == 1):
#         last = allnums[0]
#     else:
#         last = allnums[-1]
#     numbers.append(int(first+last))
# print(sum(numbers))

# f = open("day1.txt", encoding='utf8')

#part 2
#create dictionary of number 1-9 "one":1
worded_numbers =  ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]




# test ="oneftwoasthree3four5five six seven eight nine"
# for key in dict:
#     test = test.replace(dict[key], str(key))
# print(test)
numbers= []

for line in f:
    #print("Line: ", line)
    num_array = []
    ind = 0
    for letter in line:
        #print("Letter: ", letter)
        if letter.isdigit():
            num_array.append(letter)
            #print(letter)
        else:
            for i in range(len(worded_numbers)):
                word = worded_numbers[i]
                test_word = line[ind:ind+len(word)]
                #print("Test word: ", test_word)
                if(test_word == word):
                    #print("Word: ", word)
                    num_array.append(str(i+1))
                    break
            # for word in array:
            #     if(ind+len(word) > len(line)):
            #         continue
            #     test = line[ind:ind+len(word)]
            #     if(test == word):
            #         num_array.append(str(array.index(word)+1))
        ind+=1 
    numbers.append(int(num_array[0]+num_array[-1])) 
                    
            
    
    
    
    # print(line)
    
    # allnums = ''.join(filter(str.isdigit, line))

    # first = allnums[0]
    # if(len(allnums) == 1):
    #     last = allnums[0]
    # else:
    #     last = allnums[-1]
    # numbers.append(int(first+last))
    # ind+=1
    
print(sum(numbers))





