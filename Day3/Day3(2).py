L1 = [53, 40, 10, 37, 91, 97, 87, 45, 15, 12, 29, 21, 73, 77, 91, 55, 46, 64, 37, 29]
L2=sorted(L1)
L3=L2[1:-1]
sum=0
for i in range(0,len(L3)):
    sum+=L3[i]
result_average=sum/(len(L3))
result=round(result_average/10)
print(result)
