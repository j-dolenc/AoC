lines = open("input.txt", encoding="utf8")


cycle = 1
signalPower = 0
register = 1
pixel = 0
for line in lines:

    command = [i for i in line.strip().split()]
    
    goFor = 0

    if(command[0] == "noop"):
        goFor = 1
    else:
        goFor = 2
    for i in range(0,goFor):
        if(pixel == 40):
            pixel = 0
        if(abs(register-pixel) <= 1):
            print("##", end = '')
        else:
            print("..", end='')
        if(cycle%40 == 0):
            print("")
        pixel+=1
        if(cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
            signalPower += (cycle* register)
        cycle+=1
    if(command[0] != "noop"):
        register+=int(command[1])
    