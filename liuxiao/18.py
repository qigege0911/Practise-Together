L1=[1,2,3,4]
L2=[5,6,7,8]
L3=[]
#for i in reversed(range(0,4)):
for i in range(3,-1,-1):
    L3.append(L1[i])
    L3.append(L2[i])
print(L3)