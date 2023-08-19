amt=0
r={id:12,
   'n':"karthik"
}
print("WELCOME TO THE WORLD OF SHOPPING")
print("********************************")
print()
def shirt(i):
    global amt
    amt+=800*i
    print("CURRENT TOTAL IS",amt)
def jeans(i):
    global amt
    amt+=1200*i
    print("CURRENT TOTAL IS",amt)
def others(i):
    global amt
    amt+=500*i
    print("CURRENT TOTAL IS",amt)
def total():
    global amt
    if amt>2000:
        amt-=500   
    print("THE GRAND TOTAL AFTER THE DISCOUNT:", amt)
lid=int(input("Enter Your login id:"))
while True:
        if lid==r[id]:
            b=int(input("CHOICE YOU OPTION:\n 1 FOR SHIRT\n 2 FOR JEANS\n 3 FOR OTHERS\n 4 FOR QUIT  :"))
            if b==4:
                total()
                break
            else:
                if b==1:
                    n=int(input("Enter the no of shirts you want :"))
                    shirt(n)
                elif b==2:
                  n=int(input("Enter te no of jeans you want  :"))
                  jeans(n)
                elif b==3:
                  n=int(input("Enter the no of other items you want :"))
                  others(n)
                else:print("wrong option")
        else:
            lid!=r[id]
            lid=int(input("Re-Enter Your login id:  "))  