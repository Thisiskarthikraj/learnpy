act="123"
l=int(input("enter your pin :"))
if l in act:
    a=input(" ENTER 1 FOR DEPOSIT  ENTER 2 FOR WITHDRAW  ENTER 3 FOR BALANCE ")
else : print("Reenter Your pin, Thank You ")

def deposit(c):
    c+=c
c=int(input("enter the amount you want to deposit: "))

def withdrawel(debit):
    debit-=debit
debit=int(input("enter the amount you want to withdraw: "))

def balance(bal):
    bal=c-debit
    print(bal)
if a =="1": deposit(c)
elif a=="2": withdrawel(debit)
elif a=="3" :balance(bal)

        