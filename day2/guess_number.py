#A Short Program: Guess the Number between 0 and 10 within 3 attempts

import random
print("Guess the number between 0 and 10. You only have 3 attempts")
number=random.randint(1,9)
i=1
while (i<4):
    guess_no=int(input('>'))
    if(number<guess_no):
         print("Your guess is too high")
    elif(number>guess_no):
         print("Your guess is too low")  
    elif(number==guess_no):
        print(f"Hurray! You guessed correctly in {i} attempt/s") 
        break
    if(i<3): 
        print("Take another guess")
    i+=1    
else:
     print("Your attempts are over")
     