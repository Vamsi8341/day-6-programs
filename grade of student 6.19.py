print("Enter Marks Obtained in 4 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())

tot = markOne+markTwo+markThree+markFour
avg = tot/4

if avg>=75 and avg<=100:
    print("Distinction")
elif avg>=60 and avg<75:
    print("First Division")
elif avg>=50 and avg<60:
    print("second division")
elif avg>=40 and avg<50:
    print("third division")
else:
    print("fail")
