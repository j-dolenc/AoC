f = open("day4.txt", encoding='utf8')

points_sum = 0




for line in f:
    
    card = line.replace("\n","").split(": ")[1].split(" | ")
    #print(card)
    
    
    winning_numbers = [int(x) for x in card[0].split(" ") if x.isdigit()]
    #print("winning numbers: " + str(winning_numbers))
    
    
    my_numbers = [int(x) for x in card[1].split(" ") if x.isdigit()]
    
    #print("my numbers: " + str(my_numbers))

    my_wins = 0
    for number in my_numbers:
        if number in winning_numbers:
            my_wins += 1
    
    if(my_wins > 0):
        points_sum += 2 ** (my_wins - 1)
print(points_sum)

#Part 2

f=open("day4.txt", encoding='utf8')

lines = f.readlines()
#print(len(lines))

num_of_copies = [1 for _ in range(len(lines))]
#print(num_of_copies)

for i in range(len(lines)):
    
    card = lines[i].replace("\n","").split(": ")[1].split(" | ")
    #print(card)
    
    
    winning_numbers = [int(x) for x in card[0].split(" ") if x.isdigit()]
    #print("winning numbers: " + str(winning_numbers))
    
    
    my_numbers = [int(x) for x in card[1].split(" ") if x.isdigit()]

    #print("my numbers: " + str(my_numbers))

    my_wins = 0
    for number in my_numbers:
        if number in winning_numbers:
            my_wins += 1

    if(my_wins > 0):
        for j in range(i+1,i+my_wins+1):#maybe i+my_wins+1
            num_of_copies[j] += num_of_copies[i]
    #print(num_of_copies)

print(sum(num_of_copies))




    