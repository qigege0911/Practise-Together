L='abcdefg'
i=input('输入一个数字:')
L1=''
if 2<=int(i)<=len(L):
    L1=L[int(i)-1:]+L[0:(int(i)-1)]
    print(L1)
else:
    print('error')






