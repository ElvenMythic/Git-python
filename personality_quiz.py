import time

print("Welcome to the Sree Sanka personality quiz!")
time.sleep(1)
print("We will give you four choices. Pick one and enter the number. After you have answered all of the questions, you will get the character from the famous Sree Sanka series that is closest to your personality.")
time.sleep(3)

sreesanka=0
kapoodi=0
bashwinius=0
bankyrank=0
mrbuke=0

question=0

questions=["If somebody threw a basketball at you, what would you do?"]

answers1=["1. Dribble it with your belly"]
answers2=["2. Consume it"]
answers3=["3. Chop it in half with your bare hands in the blink of an eye"]
answers4=["4. Scold the thrower with a sassy remark"]
answers5=["5. Catch it, dribble it between your legs, and yoink it into the basket"]

while question<=5:
    print(questions[question])
    print()
    print(answers1[question])
    print(answers2[question])
    print(answers3[question])
    print(answers4[question])
    print(answers5[question])
    print()
    answer=input()
    if answer==1:
        sreesanka=sreesanka+1
    elif answer==2:
        kapoodi=kapoodi+1
    elif answer==3:
        bashwinius=bashwinius+1
    elif answer==4:
        bankyranky=bankyranky+1
    elif answer==5:
        mrbuk=mrbuke+1
    question=question+1
