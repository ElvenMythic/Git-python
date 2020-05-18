import time

#global speed
#global engaged

speed=0
engaged=0
choice=0

def startCar():
    global engaged
    print("Started car. Vroom vroom.")
    engaged=1

def stopCar():
    global engaged
    print("Stopped car.")
    engaged=0

def gasCar(accel):
    global speed
    print("Accelerated car. Vroom vroom!")
    speed=+accel

def brakeCar():
    global speed
    print("Braked the car.")
    speed=0

def parkCar():
    print("Engaged auto-parking system. Please wait.")
    for i in range(0,3):
        print("Beep...")
        time.sleep(1)
    print("Parked successfully!")
    stopCar()

while 1==1:
    time.sleep(1)
    print("What would you like to do?")
    if engaged==0:
        print("- start car")
    elif engaged==1:
        print("- stop car")

    time.sleep(0.2)

    if engaged==1:
        print("- gas car")
        time.sleep(0.2)

        print("- brake car")
        time.sleep(0.2)

        print("- park car")

    time.sleep(0.2)
    if engaged==1:
        print("Current Speed:",speed,"mph")
    
    choice=input()

    if choice=="start car" and engaged==0:
        startCar()
    elif choice=="stop car" and engaged==1:
        stopCar()
    elif choice=="gas car" and engaged==1:
        print("How much to you want to accelerate?")
        accelParam=float(input())
        gasCar(accelParam)
    elif choice=="brake car" and engaged==1:
        brakeCar()
    elif choice=="park car" and engaged==1:
        parkCar()

    if speed>=100:
        print("Your car proceeds to violently explode, unable to handle the high speed you have chosen.")
        time.sleep(5)
        quit()
    
