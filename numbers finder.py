#Print all numbers from a given range through a given increment.

print("Enter a starting point.")
start=int(input())
      
print("Enter an ending point.")
end=int(input())

print("Enter an increment.")
inc=int(input())

for i in range(start,end+1,inc):
    print(i)
