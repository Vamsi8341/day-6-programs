from math import factorial
n = int(input("Enter a number of rows:"))
b=int(input("Enter the row number:"))
if(n>0):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print()
    if(b>0):
        a=0
        for i in range(n):
            for j in range(i+1):
                if(i==b-1):
                    a+=factorial(i)//(factorial(j)*factorial(i-j))
        print("Sum of elements in the row:",a)
    else:
        print("INVALID INPUT")
else:
    print("INVALID INPUT")
