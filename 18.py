def new_func(a):
    count=0
    c=0
    b=[]
    for i in a:
      if i.isupper():
       count+=1
      elif i.islower():
        c+=1
    print(count)
    print(c)
a=input("")
new_func(a)

