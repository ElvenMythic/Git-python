#init
import random
import time

choices=["rock","paper","scissors"]
messageWin=["I win!","Haha, you lost.","Don't mess with the bot","Get toasted!"]
messageLoss=["Boohooo...","Looks like I lost. For once.","Ugh, I lost.","You beat me?? Pee poo."]
messageDraw=["Looks like we've tied.","It's a draw!","We got the same thing.","Neither of us wins."]

print("Welcome to Rock, Paper, Scissors.")
time.sleep(1)
print("In this game, you will be utterly destroyed by a bot in a game of rock, paper, scissors.")
time.sleep(1.5)
print()
print("Continue? (Y/N)")

while 1==1:
    inp=input()
    print()
    if inp=="Y":
        print("Prepare for ultimate disappointment and failure.")
        print("-------------------")
        print("Choose rock, paper, or scissors.")
        inp=input()
        print()
        print("Processing...")
        time.sleep(random.randint(1,3))
        botDecis=random.randint(0,2)

        if inp!="rock" and inp!="paper" and inp!="scissors":
            print("Hm? That's an invalid answer...")
            time.sleep(1)
            quit()
        else:
            print("I chose",choices[botDecis]+".")
        
        if inp=="rock" and choices[botDecis]=="paper":
            
            part1="Paper beats rock!"

            outcome="BotWin"
            
        elif inp=="rock" and choices[botDecis]=="scissors":
            
            part1="Rock beats scissors."

            outcome="BotLoss"
            
        elif inp=="paper" and choices[botDecis]=="scissors":
            
            part1="Scissors beats paper!"

            outcome="BotWin"
            
        elif inp=="paper" and choices[botDecis]=="rock":
            
            part1="Paper beats rock."

            outcome="BotLoss"

        elif inp=="scissors" and choices[botDecis]=="rock":

            part1="Rock beats scissors!"

            outcome="BotWin"

        elif inp=="scissors" and choices[botDecis]=="paper":

            part1="Scissors beats paper."

            outcome="BotLoss"

        elif inp==choices[botDecis]:

            part1="We chose the same object."

            outcome="Draw"

        time.sleep(1)

        if outcome=="BotWin":
            print(part1,messageWin[random.randint(0,3)])
        elif outcome=="BotLoss":
            print(part1,messageLoss[random.randint(0,3)])
        elif outcome=="Draw":
            print(part1,messageDraw[random.randint(0,3)])
            
    elif inp=="N":
        print("Pathetic mortal. Can't even take a challenge.")
        time.sleep(1)
        print("Quitting...")
        quit()
    else:
        print("Unknown answer.")
