import random
from bs4 import BeautifulSoup
import urllib.request
import requests

def display_hangman(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
          
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
         
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
          
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
           
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
             
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def hangman(tally):

    words=['malayalam','tomato','pumpkin','moon','goat']
    x=random.randint(0,len(words)-1)
    a=random.choice(words)
    #a=a.decode('utf-8')
    a=a.lower()
    b=str()
    print('Your word is: ', end= ' ')
    for i in range (0, len(a)):
        b= b+'_'
        print(b[i] ,end= ' ')
    
    guess=[]
    wrong=[]
    points=tally[1]
    tries=tally[0]
    while(tries>0):
        
        print("\nYour guesses so far:",guess)
        print('\n\nYou have ' +str(tries)+' chances to guess the word')
        x=input("Enter 0 to stop this game or Enter an alphabet: ")
        if(x=='0'):
            break
        if(len(x)!=1):
            print("Enter only a single alphabet")
            continue
        if(x.isalpha()==False):
            print("Enter a valid alphabet")
            continue
        
        x= x.lower()
        guess.append(x)
        buffer=0
        buffer1=0
        found=0
        for i in range (0,len(a)):
            if(a[i]==x):
                found=1
                buffer=1
                b=list(b)
                b[i]=x
                b="".join(b)
                points=points+1
        if(buffer==1):
            print("Correct guess :)")
            for j in range (0, len(b)):
                print(b[j] ,end= ' ')
        if(found==0):
            print("Incorrect guess, try harder!!")
            for j in range (0, len(b)):
                print(b[j] ,end= ' ')
        if(buffer==0):
            if x in wrong:
                    buffer1=1
            if(buffer1==0):
                print(display_hangman(tries-1))
                tries=tries-1
                wrong.append(x)
                
        buf=0
        for i in range(0, len(b)):
            if(b[i]=='_'):
                buf=1
        if(buf==0):
            print('\nYou have guessed the word with ' + str(tries) +' chances left \n'+ str(points)+' points\n\n')
            tally[0]=tries
            tally[1]=points
            return tally
    if(tries==0):
        print('You lost. Better luck next time! \n Your word was: '+a+'\nYour points are: '+str(points))
        print(a)
        tally[0]=0
        tally[1]=points
        return tally

print('HANGMAN')
tally=[0,0]
while True:
    x=input('Press:\n 1.To play a new game \n 2. Continue existing game \n 3. Exit\n')
    if(x=='1'):
        tally=[7,0]
        tally= hangman(tally)
    elif(x=='2'):
        if(tally[0]==0):
            print('There is no saved game, here is a new one\n')
            tally[0]=7
            tally[1]=0
        tally=hangman(tally)
        
    elif(x=='3'):
        exit()
    else:
        print("Enter a valid response ")

import time
import threading


t = threading.Thread(target=hangman)
t.daemon = True
t.start()

time.sleep(6)
