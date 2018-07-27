L1 = [53, 40, 10, 37, 91, 97, 87, 45, 15, 12, 29, 21, 73, 77, 91, 55, 46, 64, 37, 29]
L2=[]
sum=0
L1.sort()
for i in range(1,len(L1)-1):
    L2.append(L1[i])
for i in L2:
    sum+=i#print(sum/len(L2))
if (sum/len(L2))%10>=5:
    print(int((sum/len(L2))//10+1))
else:
    print(int((sum/len(L2))//10))




