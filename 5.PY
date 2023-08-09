li=["abc","a",1,11]
l2=["a",11,150.5]
b=[]
i=0
while i<len(li):
    if li[i] in l2:
        b.append(li[i])
    i+=1                     
print(b)
