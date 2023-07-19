from datetime import date
dob=int(input ("enter your birth year :"))
today = date.today().year
age=today-dob
print("your age is :" ,age)

a=int(input("Enter your birth year:"))
b=int(input("Enter your birth month:"))
res1=2023-a
res2=7-b
if(res2<0): 
    res=res1-1 
    res3=res2+12
    print("Your current age is " ,res , "year old and",res3 , "month" )
else:
    print("Your current age is " ,res1 , "year old and",res2 , "month" )