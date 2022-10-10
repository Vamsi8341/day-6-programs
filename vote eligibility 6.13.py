age = int(input("Enter your age: "))

if age >= 18:
    print("he is eligible to vote")
else:
    print("he can cast votes after {} years!".format( 18-age))
