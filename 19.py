d={
    1:'a',
    2:'p',
    3:'a',
    5:'p' ,
    6:'a',
    7:'p',
    8:'a',
    9:'p'
}
def sample(a):
    if a not in d: print("invalid choice")
    elif 'a'==d[a]:print("absent")
    elif 'p'==d[a]:print("present")
    else:print("Thank you")
a=int(input("enter ur rool no: "))
sample(a)
