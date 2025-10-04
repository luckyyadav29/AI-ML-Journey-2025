#Write a program to find out how often a streak of six heads or a streak
#of six tails comes up in a randomly generated list of 100 heads and tails.
# # Put all of this code in a loop that
#repeats the experiment 10,000 times so that you can find out what percentage of the coin flips contains a streak of six heads or six tails in a row 

import random
n=0
nosh,nost=0,0  #nos-number of streaks , head/tail
chance_of_streak_of_head,chance_of_streak_of_tail=0.0,0.0
streak_of_head,streak_of_tail=0.0,0.0

while n<10000:
    flip_list=[]
    nosh,nost=0.0,0.0
    for i in range(0,100):
        flip=random.randint(0,1)
        if flip==0:
            flip_list.append("H")
        else:
            flip_list.append("T") 

    for i in range(0,len(flip_list)):
        if flip_list[i:i+6]==(['H']*6):
            nosh+=1
            chance_of_streak_of_head=(nosh/100000)*100 
        elif flip_list[i:i+6]==(['T']*6):
            nost+=1
            chance_of_streak_of_tail=(nost/100000)*100
           
    streak_of_head+=chance_of_streak_of_head
    streak_of_tail+=chance_of_streak_of_tail
    n+=1        
   
print(f"6 Head Streak % :{streak_of_head:.2f}%")
print(f"6 Tail Streak % :{streak_of_tail:.2f}%")