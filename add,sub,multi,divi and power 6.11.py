def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def pow(a,b):
    return a**b

print("select operator:")
print("1.+")
print("2.-")
print("3.x")
print("4./")
print("5.^")

while True:
    choice = input("enter choice(1/2/3/4/5):")

    if (choice in ('1','2','3','4','5')):
        a=float(input("enter first number:"))
        b=float(input("enter second number:"))

        if(choice=="1"):
           print(a,"+",b,"=",add(a,b))
        elif(choice=="2"):
           print(a,"-",b,"=",sub(a,b))
        elif(choice=="3"):
           print(a,"x",b,"=",mul(a,b))
        elif(choice=="4"):
           print(a,"/",b,"=",div(a,b))
        elif(choice=="5"):
            print(a,"^",b,"=",pow(a,b))

        next_calculation=input("lets do next calculation?(yes/no):")
        if(next_calculation=="no"):
            break
    else:
        print("invalid input")
