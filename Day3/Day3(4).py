i=0
def counter():
    global i
    import time
    a = input()
    t1 = time.time()
    b = input()
    t2 = time.time()
    T = t2 - t1
    i+=1
    return T
while i<=3:
    print(counter())










