#design a rock , paper, scissor game
import random

print("Game Instructions: \nYou have total 5 rounds \nEnter R for Rock, P for Paper and S for scissor ")
machine_points,user_points=0,0
i=0
while(i<5):
    machine_input=random.randint(1,3)
    if machine_input==1:
        machine_input="R"
    elif machine_input==2:
        machine_input="P"
    else:
        machine_input="S"    
    # print(machine_input)

    user_input=input("Enter your choice\n").upper()
    if machine_input==user_input:
        print("A tie")
        i+=1
    elif machine_input=="R" and user_input=="S" or machine_input=="P" and user_input=="R" or machine_input=="S" and user_input=="P":
        machine_points+=1
        print(f"You lose this round\nMachine's points:{machine_points} , Your points:{user_points}")
        i+=1
    elif machine_input=="S" and user_input=="R" or machine_input=="R" and user_input=="P" or machine_input=="P" and user_input=="S":
        user_points+=1    
        print(f"You won this round\nYour points:{user_points} , Machine's points:{machine_points}")
        i+=1
    else:
        print("Wrong Input \nEnter R for Rock, P for Paper and S for scissor")

if user_points==machine_points:
    print("Match Tie")
if user_points>machine_points:
    print(f"\nCongratulations! You won this game\nYour points:{user_points} , Machine's points:{machine_points}") 
else:
     print(f"\nOh no!, Better Luck Next Time.\nMachine won this game\nMachine's points:{machine_points} , Your points:{user_points} ")          
        