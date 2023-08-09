a=[]
for i in range(1,4):
    b=int(input("enter :"))
    a.append(b)
i=0
sum=0
c=[]                                                          
while i<len(a):
    sum+=a[i]                
    i+=1
avg=sum//len(a)
i=0
while i<len(a):
   if a[i]>avg:
       c.append(a[i])
   i+=1                                                                                                                   
print(c)