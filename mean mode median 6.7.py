from statistics import mode
n=int(input("enter the length:"))
num_list = []
for i in range (n):
    c=int(input("enter the elements:"))
    num_list.append(c)
num_sum=sum(num_list)
mean = num_sum / len(num_list)
print(num_list)
num_list.sort()
if len(num_list) % 2 == 0:
   first_median = num_list[len(num_list) // 2]
   second_median = num_list[len(num_list) // 2 - 1]
   median = (first_median + second_median) // 2
else:
   median = num_list[len(num_list) // 2]
print(num_list)
print("median: " ,median)
print("mean: ",mean)
print("mode:",mode(num_list))
