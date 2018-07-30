'''
L=input('输入一个字符串')
sign=0
for i in range(0,len(L)//2):
    if L[i]==L[-i-1]:
        sign=1
    else:
        sign=0
if sign==1:
    print('True')
else:
    print('False')
'''


import re
s=re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(s)




