#init
import time
import random

directory=["Kapoodle","Chaden","Cryan","BankyRanky","Noodle"]
extradirectory=["Face Picado","ChingChong","null","AAAAAAA","Tonald Drump"]

files=["Caught 24 times committing arson. Has a detention-free record.","Defiled several holy sites and was a major pawn in WWII.","Robbed two banks using a shovel. Skipped 3 grades at once.","In a violent temper tantrum, accidentally created the universe.","Started a terrorist organization and is currently operating in a terrorist cell in the USA. Abysmal grades."]
extrafiles=["Thrown 54 lemons total at passersby in Paris.","Assaulted innocent members of the UN with a single banana.","Died","Achieved a new level of reality over the course of 3 seconds.","Arrested for using offensive language, allegedly saying nothing."]

chosenfiles=[]

#processing
while 1==1:
    print("Choose a student's file.")
    print(directory)

    chosenfile=input()
    print("Subject:",directory[directory.index(chosenfile)])
    print(files[random.randint(0,len(directory))])
    print("You've unlocked a new file.")

    newdir=random.randint(0,len(extradirectory))
    directory.append(extradirectory[newdir])
    extradirectory.pop(newdir)

    newfile=random.randint(0,len(extrafiles))
    files.append(extrafiles[newfile])
    extrafiles.pop(newfile)
    

