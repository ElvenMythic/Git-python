import time

import random

#generate list of books

books=[1,2,3,4,5,6,7,8,9,10]

lostbooks=[]

#The entire program lol

while 0==0:
    print("This is the total list of books in the library.",books)

    time.sleep(1)

    print("Would you like to check out or return a book?")

    answer=str(input())

    if answer=="check out":
        print("What is the number of the book you'd like to check out?")
        answerbook=int(input())
        if answerbook in books:
            books.remove(answerbook)
            print("You have checked out",answerbook," successfully. Thank you for your time.")

        elif answerbook in lostbooks:
            print("Unfortunately, that book has been lost. There is no possible way you could be returning it.")
        
        else:
            message=random.randint(0,3)
            if message==0:
                print("You small failure. I can't believe you wanted to check out a nonexistent or taken book. I bet you don't even publicly urinate.")
            if message==1:
                print("I'm sorry small child, this book is not available. Now scram!")
            if message==2:
                print("Excuse me, but who do you think you are, walking in here, trying to check out a NONEXISTENT OR TAKEN BOOK!!!")
            if message==3:
                print("I kindly request you to move your legs in such a fashion that it transports your body outside of the building immediately. Your requested book is missing or nonexistent.")
    elif answer=="return":
        print("What is the number of the book you'd like to return?")
        answerbook=int(input())
        books.append(answerbook)
    elif answer=="I lost a book":

        print("What book have you lost?")

        answerbook=str(input())

        lostbooks.append(answerbook)
        if answerbook in books:
            books.remove(answerbook)
        
        print("You've lost a book?")
        time.sleep(1.5)
        print("Pathetic")
        time.sleep(1.5)
        print("I can't believe you'd let down the organization like this.")
        time.sleep(2.5)
        print("I suppose you're no longer worthy.")
        time.sleep(2.5)
        print("Goodbye.")
        time.sleep(2.5)
        print("You struggle to breath as Sree Sanka's belly enfolds your face. Darkness encloses you...")
        time.sleep(3)
        print("You have no memories. But you must start the cycle of public urination again.")
        time.sleep(2)
