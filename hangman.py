from PyDictionary import PyDictionary
import random 
words=open('C:/Users/R.R.6.12.20/Desktop/wordlist.10000.txt','r')
list_of_words=words.read().split('\n')
game_word=random.choice(list_of_words)
game_word=game_word.lower()
l=len(game_word)
string= ['_']*l
chances=0
guessed_alphabets=[]
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
while chances<6:
    print(string)
    guess=input("Enter the alphabet:")
    guess=guess.lower()
    
    if guess in game_word:
        alpha_index=find(game_word,guess)
        for i in alpha_index:
            string[int(i)]=guess
    else:
        chances+=1  
        guessed_alphabets.append(guess)
    print("Guessed alphabets:{}".format(guessed_alphabets)) 
    num= 6-chances
    print("remaining guesses {}".format(num))    
    if ''.join(string)==game_word:
        print("Yayy you guessed it right")
        break 
if chances==6:
    print('GAME OVER') 
  
print("The word is '{}' and its meaninig {}".format(game_word,PyDictionary.meaning(game_word)))       










