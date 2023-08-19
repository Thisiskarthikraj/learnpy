l=[1,2,3,4]
for i in l:
    x=lambda i:i%2==0
    if x(i) is True:
        print(i)