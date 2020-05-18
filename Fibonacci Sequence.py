import time

x=0
y=1

print(x)
time.sleep(0.5)
print(y)

while True:
    time.sleep(0.5)
    z=x+y
    print(z)
    x=y
    y=z
