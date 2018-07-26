L1=[1,2,3,4,5,6]
L2=[]
for i in range(1,6,2):
    L2.append(L1[i]) 
    L2.append(L1[i-1])
print(L2)