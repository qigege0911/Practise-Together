L1 = [1,2,3,4,5,6,7]
L2 = []
for i in range(1,len(L1),2):
    L2.append(L1[i])
    L2.append(L1[i-1])
if len(L1)%2==1:
    L2.append(L1[-1])
print(L2)



