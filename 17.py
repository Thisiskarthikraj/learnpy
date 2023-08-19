def  add(x,y):
    sum=x+y
    print(sum)
def  dif(x,y):
    sub=x-y
    print(sub)
def  mul(x,y):
    mu=x*y
    print(mu)
def  div(x,y):
    di=x/y
    print(di)

print("1 for sum")
print("2 for sub")
print("3 for mul")
print("4 for div")
   
a=int(input("choose your option "))

if a==1:
    add(10,4)
elif a==2:
    dif(20,3)
elif a==3:
    mul(10,20)
elif a==4:
    div(5,3)
else:print("invalid choice")