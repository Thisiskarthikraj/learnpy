a=[1 ,2 ,3, 2, 1 ,2 ,3,5 ]
b=[]
i=0
while i<len(a):
      if a[i] not in b:
            b.append(a[i])
      i+=1           
print(b)

      