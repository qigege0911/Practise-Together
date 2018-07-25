dict={'小花':89,'小白':67,'小小':56,'小灰':79,'小哈':97,'小皮':86,'小马':77}
list=sorted(dict,key=lambda x:dict[x],reverse=True)
i=0
while i<3:
    print(list[i])
    i+=1



