#open file day2.txt which is in the same folder as this file
f = open("day2.txt", encoding='utf8')


red_threshold = 12
green_threshold = 13
blue_threshold = 14

#one line in day2.txt looks like: "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
succ_games = []
for line in f:
    #remove \n from line
    line = line.replace("\n", "")
    #split line by :
    line = line.split(": ")
    #print(line)
    game_id = line[0].split(" ")[1]
    #print("Game ID: ", game_id)

    line = line[1].split("; ")
    succesful = True
    for sub in line:
        #print(sub)
        colors = sub.split(", ")
        #print(colors)
        for color in colors:
            color = color.split(" ")
            #print(color)
            if(color[1] == "red"):
                if(int(color[0]) > red_threshold):
                    succesful = False
                    #print("Failed red")
                    break
            elif(color[1] == "green"):
                if(int(color[0]) > green_threshold):
                    succesful = False
                    #print("Failed green")
                    break
            elif(color[1] == "blue"):
                if(int(color[0]) > blue_threshold):
                    succesful = False
                    #print("Failed blue")
                    break
        if(not succesful):
            break
    if(succesful):
        succ_games.append(game_id)
#print("Successful games: ", succ_games)
print(sum(map(int, succ_games)))


#Part 2

f = open("day2.txt", encoding='utf8')

red_max = 0
blue_max = 0
green_max = 0

pow_arr= []
for line in f:
    #remove \n from line
    line = line.replace("\n", "")
    #split line by :
    line = line.split(": ")
    #print(line)
    game_id = line[0].split(" ")[1]
    # print("Game ID: ", game_id)

    line = line[1].split("; ")
    for sub in line:
        #print(sub)
        colors = sub.split(", ")
        #print(colors)
        for color in colors:
            color = color.split(" ")
            #print(color)
            if(color[1] == "red"):
                if(int(color[0]) > red_max):
                    red_max = int(color[0])
            elif(color[1] == "green"):
                if(int(color[0]) > green_max):
                    green_max = int(color[0])
            elif(color[1] == "blue"):
                if(int(color[0]) > blue_max):
                    blue_max = int(color[0])
    #print("Red: ", red_max)
    #print("Green: ", green_max)
    #print("Blue: ", blue_max)

    pow_arr.append(red_max*blue_max*green_max)
    red_max = 0
    blue_max = 0
    green_max = 0
print(sum(pow_arr))