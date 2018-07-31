pass

'筛选出L中大于等于50的数，筛选出L2所有的质数，然后把两个筛选结果合并，并从小到大输出'
L = [98, 78, 15, 30, 87, 36, 22, 3, 74, 61, 38, 68, 52, 10, 16, 15, 5, 39, 22, 97]
L2 = [66, 43, 61, 70, 26, 94, 14, 7, 85, 81, 25, 71, 77, 90, 52, 5, 76, 14, 15, 37]
L3=[]
for i in range(0,len(L)):
    if L[i]>=50:
        L3.append(L[i])
print(L3)
for j in L2:
    sign=0
    for k in range(2,j):
        if j%k==0:
            sign=1
            break
    if sign==0:
        L3.append(j)
print(sorted(L3,reverse=False))





