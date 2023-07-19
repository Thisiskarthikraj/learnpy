maths=int(input("Enter the mark you obtained in maths exam:"))
phy=int(input("Enter the mark you obtained in phy exam:"))
chem=int(input("Enter the mark you obtained in chem exam:"))
total3=maths+phy+chem
total2=maths+phy
if(maths>=65 and phy>=55 and chem>=55):
    if(total3>=190 or total2>=140):print("you are eligible")
    else:print("your not eligible")
    
else:print("you are not eligible")
