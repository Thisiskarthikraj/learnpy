count=0
c=(input("enter a word  "))
a=c.lower()
b=["a","e","i","o","u"]
i=0
while i<len(a):
    if a[i] in b :
        count+=1
    i+=1
print(count)