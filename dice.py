from random import randint
 
maximum=int(input("Enter the max value of dice:"))
print('The person who reaches {} wins.And if any player exits before the game ends ,a random number from (10-30) will be subtraced from thier score. '.format(str(10*maximum)))
player1=0
player2=0
while player1 < 10*maximum and player2 < 10*maximum:
     p1=input('player1 its your turn do you want to play(y/n):')
     if p1=='y':
         player1+=randint(1,maximum)
         print("your score is {}".format(player1))
     else:
         player1-=randint(10,30)
         break
     p2=input('player2 its your turn do you want to play(y/n):') 
     if p2=='y':
         player2+=randint(1,maximum)  
         print("your score is {}".format(player2))
     else:
         player2-=randint(10,30)
         break 
if player1>player2:
    print("yayy player1 won the game")  
elif player2>player1:
    print('yayy player2 won the game') 
else:
    print('Its a Draw')                    