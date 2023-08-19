s=lambda a,b:a+b
sub=lambda a,b:a-b
m=lambda a,b:a*b
d=lambda a,b:a/b
a=int(input("1 for sum, 2 for sub ,3 for mul , 4 for div :"))
x=int(input("enter the fisrt value "))
y=int(input("enter the fisrt value ")) 
if a==1:print(s(x,y))
if a==2:print(sub(x,y))
if a==3:print(m(x,y))
if a==4:print(d(x,y))