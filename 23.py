a="123"
name="karthik"
bal=0
def deposit():
    c=int(input("Enter the amount you want to deposit: "))
    global bal
    bal+=c
    print("Your current blance is",bal)
    l=input("1 for deposit , 2 for withdrew ,3 for checking balance: ")
    if l=="1":
        deposit()
    elif l=="2":
        withdrew()
    elif l=="3":
        balance() 
def withdrew():
    global bal
    d=int(input("Enter the amount you want to withdrew: "))
    if bal>d:
        bal-=d
    else:print("You dont have enough balance")
    print("Your current blance is",bal)
    l=input("1 for deposit , 2 for withdrew ,3 for checking balance ,4 for cancell   ")
    if l=="1":
        deposit()
    elif l=="2":
        withdrew()
    elif l=="3":
        balance()
def balance():
    global bal
    print("Your current blance is",bal)
    l=input("1 for deposit , 2 for withdrew ,3 for checking balance, 4 for cancell :  ")
    if l=="1":
        deposit()
    elif l=="2":
        withdrew()
    elif l=="3":
        balance() 
for i in range(1):
    b=input("Enter your account number: ")
    if b==a:
        l=input("1 for deposit , 2 for withdrew ,3 for checking balance,4 for cancell : ")
        if l=="1":
            deposit() 
        elif l=="2":
            withdrew() 
        elif l=="3":
            balance()
    else:
         b!=a
         b=input("Re-enter your act no: ") 
         if b==a:
            l=input("1 for deposit , 2 for withdrew ,3 for checking balance ,4 for cancell : ") 
            if l=="1":
                deposit()
            elif l=="2":
                withdrew()
            elif l=="3":
                balance()
         else: print("You Entered the maximum limit!!")