#Display the requested times table.

print("What times table do you want?")
timestable=int(input())

print("Here is the timestable for ",timestable,".")
for j in range(1,13):
    product=j*timestable
    print(timestable,"*",j,"=",product)
