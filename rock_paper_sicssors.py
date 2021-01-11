import random
name=input("Enter your name:")
print("welcome {}".format(name))  
print("Let the fun begins")   
s=("rock","paper","scissors")
while True:
    comp=random.choice(s) 
    player=input("let's play (rock,paper,scissors):")
    player=player.lower()
    if comp=='rock' and player=='scissors':
        print("computer: {}".format(comp))
        print("You loose!")
    elif comp=='paper' and player=='rock':
        print("computer: {}".format(comp))
        print("You loose!")
    elif comp=='scissors' and player=='paper':
        print("computer: {}".format(comp))
        print("You loose!")
    elif comp==player:
        print("computer: {}".format(comp))
        print("It's a draw")    
    else:
        print("computer: {}".format(comp))
        print("You won!")        





    