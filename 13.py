b=[]
count=0
i=0
while True:
    a=input("Enter items: ")
    b.append(a)
    if a in b:
        count+=1
        if count>2:
            break
        print(b)
        i+=1