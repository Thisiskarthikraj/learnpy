a=[1,2,3,4]
b=[]
i=0
while i<len(a):
    if  a[i] not in b:
        b.append(a[i])
        print(str(b))  
    i+=1



