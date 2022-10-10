a=float(input("enter the number:"))
b=int(input("enter the num of rows:"))
for i in range(b):
    for j in range(i+1):
        print('%.1f'%a,end=" ")
        a=a+0.1
    print()
