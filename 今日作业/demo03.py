s="|it's ni-ce to you to-day?|H-ow do y|ou d-o?"
i=0
for i in range(len(s) ):
    if s[i]=="|":
        i+=1
    elif s[i]=="-":
        i+=1
    else:
        print (s[i],end="")
        i+=1