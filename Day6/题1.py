

'求出L这个列表的中位数，并输出'

L = [98, 78, 15, 30, 87, 36, 22, 3, 74, 61, 38, 68, 52, 10, 16, 15, 5, 39, 22, 97]
L1=sorted(L)
if len(L1)%2==0:
    result=(L1[len(L1)//2]+L1[len(L1)//2-1])/2
else:
    result=L1[len(L1)//2]
print(result)




