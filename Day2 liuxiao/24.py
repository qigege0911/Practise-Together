f=open('my way.txt','r',encoding='utf-8')
word=f.readlines()
f.close()
f1=open('my way中文.txt','w',encoding='utf-8')
f2=open('my way英文.txt','w',encoding='utf-8')
for i in range(len(word)):
    if i %2==0:
        f2.writelines(word[i])
    else:
        f1.writelines(word[i])
f1.close()
f2.close()