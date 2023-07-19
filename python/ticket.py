a=int(input("Enter yor age:"))
b=(input("Enter the day of week:"))
c="wednesday"
if(a<12 or a>65) :
    cost=5
    print(cost) 
  
elif(c in b and a>=12 and a<=18  ) :
     cost=4
     print(cost)
else: 
    cost=8
    print(cost)    

