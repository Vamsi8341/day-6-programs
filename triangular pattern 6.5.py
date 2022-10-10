def triangle(n):
    k=n-1
    for i in range(0,n+1):
        for j in range(0,k+1):
            print(end=" ")
        k=k-1
        for j in range(i,0,-1):
            print(j,"", end="")
        print()
n=float(input("Enter no of rows:"))
if(n<=0 or int(n)!=n):
    print("INVALID INPUT")
else:
    triangle(int(n))
