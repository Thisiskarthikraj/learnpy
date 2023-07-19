def new_func():
    t=(1,2,1,2,1,2,1,2,1,2,1,5,1,5,1,5)
    return t

new_var = t = new_func()
new_var
l=list(t)
def new_func1(l):
    l.append("karthik")

def new_func2(t, l, new_func1):
    new_func3(t, l, new_func1)

def new_func3(t, l, new_func1):
    new_func1(l)
    new = new_func4(t, l)
    t3=t+new
    print(t3)

def new_func4(t, l):
    print(t)
    new=tuple(l)
    print(new)
    return new

new_func2(t, l, new_func1)