import random

print("Rock, Paper, Scissors")
print("=====================")

player = int(input("1) ✊\n2) ✋\n3) ✌\nPick a number: "))

computer = random.randint(1,3)

choice = ["✊", "✋", "✌"] #0-2

if player > computer:
    if player == 3 and computer == 1:
        print("You chose: " + choice[player - 1])
        print("Cpu chose: " + choice[computer - 1])
        print("Cpu won!")
    else:
        print("You chose: " + choice[player - 1])
        print("Cpu chose: " + choice[computer - 1])
        print("Player won!")
elif player < computer:
    if player == 1 and computer ==3:
        print("You chose: " + choice[player - 1])
        print("Cpu chose: " + choice[computer - 1])
        print("Player won!")
    else:
        print("You chose: " + choice[player - 1])
        print("Cpu chose: " + choice[computer - 1])
        print("Cpu won!")
else:
    print("You chose: " + choice[player - 1])
    print("Cpu chose: " + choice[computer - 1])
    print("It's a tie!")
