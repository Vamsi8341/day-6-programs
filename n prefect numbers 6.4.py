a=float(input("enter n value:"))
f=int(input("enter m value:"))
a=int(a)
if(a<=0):
    print("invalid input")
else:
    b=0
    c=[]
    for n in range(1,10000):
        sum=0
        for i in range(1,n):
            if(n%i==0):
                sum = sum + i 
        if(sum==n and n!=1):
            c.append(n)
            b+=1
        if(b==a):
            break
    print("first",a,"perfect number:",c)
    e=[]
    for m in c:
        d=[]
        f1=0
        for j in range(1,m+1):
            if(m%j==0):
                if(m>=j):
                    f1+=1
                    d.append(j)
                    if(f1==f):
                        e.append(list(d))
                        break
    for i in range(0,a):
        for j in range(0,a):
            if(i==j):
                print("first",f,"factorial number",c[i],":",e[j])
