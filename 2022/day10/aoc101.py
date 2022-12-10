lines = open("input.txt", encoding="utf8")


cycle = 1
signalPower = 0
register = 1
for line in lines:
    command = [i for i in line.strip().split()]
    
    goFor = 0
    if(command[0] == "noop"):
        goFor = 1
        print("noop")
    else:
        print("addx: " + command[1])
        goFor = 2
    for i in range(0,goFor):
        print("Cycle: " + str(cycle))
        print(register)
        if(cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
            print((cycle* register))
            signalPower += (cycle* register)
        cycle+=1
    if(command[0] != "noop"):
        register+=int(command[1])
print(signalPower)