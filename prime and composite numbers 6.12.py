startNumber =int(input("enter the starting number"))
endNumber = int(input("enter the ending number number"))
prime = []
composite = []
for i in range(startNumber,endNumber):
        for p in range(2, i):
            if (i % p)==0:
                composite.append(i)
                break
        else:
            prime.append(i)
print("prime: ",prime)
print("composite: ",composite)
