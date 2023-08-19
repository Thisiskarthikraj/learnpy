# a=input("enter a string:  ")
# b="a","e","i","o","u"
# for i in a:
#     if i in b:
#         continue
#     print(i)


a=input("enter a string:  ")
b="a","e","i","o","u"
  
i=0
while i<len(a):
        
    if a[i] in b:
       continue
    print(a[i])
    i+=1
    
    