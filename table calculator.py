def calc_add(int1):
    for j in range(1,11):
        product=int1+j
        print(int1,"+",j,"=",product)

def calc_sub(int1
             ):
    for j in range(1,11):
        product=int1-j
        print(int1,"-",j,"=",product)
        
def calc_mult(int1):
    for j in range(1,11):
        product=int1*j
        print(int1,"*",j,"=",product)

def calc_div(int1):
    for j in range(1,11):
        product=int1/j
        print(int1,"/",j,"=",product)

inp=float(input())


print("Here are the math tables for ",inp,".")

print()
calc_add(inp)

print()
calc_sub(inp)

print()
calc_mult(inp)

print()
calc_div(inp)




