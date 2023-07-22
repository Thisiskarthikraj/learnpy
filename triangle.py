a=int(input("Enter the first side    :"))
b=int(input("Enter the second side   :"))
c=int(input("Enter the  third side   :"))
if(a==b==c):print("Equilateral")
elif(a==b or b==c or a==c):print("isosceles")
else:
    (a!=b and b!=c and c!=a)
    print("Scalence")