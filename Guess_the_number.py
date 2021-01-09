from random import randint
name=input('Enter your name:')
print("Welcome {}, you have five chances to guess the number between 1-25.".format(name.upper()))
print('Let the game begin')
chances=0
number=randint(1,25)
guessed_numbers=[]
while chances<5:
    user=int(input("guess the number:"))
    guessed_numbers.append(user)
    if user==number:
        print('Yayy you guessed it right {}'.format(name))
        break
    elif user>number:
        print('The number you guesssed is high.')  
    elif user<number:
        print('The number you guessed is low.')      
    chances+=1  
    print("Guessed numbers:{}".format(guessed_numbers))  
if chances==5:
    print('Game over,the number is {}'.format(number))    
