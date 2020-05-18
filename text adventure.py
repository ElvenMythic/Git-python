#init
import random
import time

#instructions

print("Are you a newcomer? (Y/N)")
choice=input()
if choice.upper()=="Y":
    print("Welcome to a text adventure.")
    time.sleep(2)
    print()
    print("During the adventure, when given choices type the NUMBER of the option you choose to proceed.")
    time.sleep(2)
    print()
    print("Enjoy your time!")
    time.sleep(3)
elif choice.upper()=="N":
    print("Got it.")
    time.sleep(0.5)

print("-----------")

print("You find yourself on top of a tree.")
print("1. Jump down")
print("2. Breakdance")

choice=input()

if choice=="1":
    print("You jump off without realizing how high up you are. You promptly die.")
    time.sleep(3)
    quit()
elif choice=="2":
    print("You breakdance, raising a huge ruckus and causing a large bird to attack you violently. You are mauled to death.")
    time.sleep(3)
    quit()
else:
    print("You do absolutely nothing.")
    time.sleep(2)
    
    print()
    print("A helicopter passes overhead.")
    print("1. Breakdance")
    print("2. Shoot a flare")
    print("3. Jump down")
    
    choice=input()
    if choice=="1":
        print("Your epic dance moves attract a large bird that attacks you violently. You are mauled to death.")
        time.sleep(3)
        quit()
    elif choice=="2":
        outcome=random.randint(0,1)
        if outcome==0:
            print("You shot the flare at the wrong time, causing the flare the fly into the helicopter window and blinding the pilot. The helicopter crashes somewhere near the floor.")
            time.sleep(3)

            print()
            print("Look's like you're in a real pickle. What are you gonna do next?")
            print("1. Cry")
            print("2. Cry")
            print("3. Jump down")
            
            choice=input()
            if choice=="1":
                print("You cry.")
                time.sleep(3)
                quit()
            elif choice=="2":
                print("You cry.")
                time.sleep(3)
                quit()
            elif choice=="3":
                print("You jump down.")
                time.sleep(2)
                print("You land on something soft. When you look down, you see that the helicopter was secretly made of foam all along.")
        elif outcome==1:
            print("The flare goes up, annoying the pilot who proceeds to gun you down.")
            time.sleep(1)
            print("Maybe you could aim better next time.")
            time.sleep(3)
            quit()
    elif choice=="3":
        print("You jump off without realizing how high up you are. You promptly die.")
        time.sleep(2)
        quit()
    
