import random
while True:
    #["Rock", "Paper", "Scissors"]
    options = ["R", "P", "S"]
    CPU = random.choice(options)
    Player = input("Pick an option from R, P, S: ").upper()
    if Player == CPU:
        print("Player(" + Player + ")" + ":" + "CPU(" + CPU + ")")
        print("Its a tie")
    elif Player == "R":
        if CPU == "P":
           print("Player(" + Player + ")" + ":" + "CPU(" + CPU + ")")
           print("CPU WINS!")
           break
        else:
            print("Player(" + Player + ")" + ":" + "CPU(" + CPU + ")")
            print("You Win!")
            break
    elif Player == "P":
        if CPU == "R":
            print("Player(" + Player + ")" + ":" + "CPU(" + CPU + ")")
            print("You Win!")
            break
        else:
            print("Player(" + Player + ")" + ":" + "CPU(" + CPU + ")")
            print("CPU WINS!")
            break
    elif Player == "S":
        if CPU == "R":
            print("Player(" + Player + ")" + ":" + "CPU(" + CPU + ")")
            print("CPU WINS!")
            break
        else:
            print("Player(" + Player + ")" + ":" + "CPU(" + CPU + ")")
            print("You Win!")
            break
    else:
        print("Error...Pick from R, S, P")