list1=[1,2,3,4]
list2=[5,6,7,8]
list3=[]
i=0
j=k=3
while j in range(len(list1) ):
    while k in range (len(list2) ):
        if i % 2 == 0:
            list3.insert(i, list1[j])
            i += 1
            j -= 1
        else:
            list3.insert(i, list2[k])
            i += 1
            k -= 1
print(list3)
