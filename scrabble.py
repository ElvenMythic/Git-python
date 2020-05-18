#double word chance=1/13 (8%)
#triple word chance=1/28 (4%)

#init

import random
import time

letters={
         "A":1,
         "B":3,
         "C":3,
         "D":2,
         "E":1,
         "F":4,
         "G":2,
         "H":4,
         "I":1,
         "J":8,
         "K":5,
         "L":1,
         "M":3,
         "N":1,
         "O":1,
         "P":2,
         "Q":10,
         "R":1,
         "S":1,
         "T":1,
         "U":1,
         "V":4,
         "W":4,
         "X":8,
         "Y":4,
         "Z":10
         }
specialCharacters=["`","~","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","<","*","(",")","-","_","=","+","[","]","{","}",":",";",",",".","<",">","?","/","|"]

while 1==1:
    #var reset
    wordchoice=0
    splitword=()
    length=0
    points=0
    
    print("Type a word")
    wordchoice=input().upper()
    print()
    wordchoice=wordchoice.replace(" ","")

    if ":DEBUG:" in wordchoice:
        print("Enter DEBUG ---")
        wordchoice=wordchoice.replace(":DEBUG:","")
        print(wordchoice)
        splitword=list(wordchoice)
        print(splitword)
        length=len(splitword)-1
        print("--- Exit DEBUG")
    else:
        splitword=list(wordchoice)
        length=len(splitword)

    print()

    for i in range (0,length):
        chosenletter=splitword[i]
        
        if chosenletter in specialCharacters:
            print("ERROR! Invalid character!")
            time.sleep(1)
            quit()
        
        print("Letter:",chosenletter,"-","Point value:",letters.get(chosenletter))
        print()
        points=points+(letters.get(chosenletter))
        
    print("---")
    print()
    
    percentage=random.randint(0,100)
    if percentage<=8:
        points=points*2
        print("It's you're lucky day! Your point value was doubled!")
    if percentage>=8 and percentage<=12:
        points=points*3
        print("It's you're lucky day! Your point value was tripled!")

    print("Total Word Value:",points)