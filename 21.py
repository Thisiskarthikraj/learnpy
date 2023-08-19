def sum_of_suares(n):
    i=1
    sq=0
    while i<=n:
        sq+=i*i
        i+=1

    return sq 
n=int(input("enter the limit: "))
print(sum_of_suares(n))