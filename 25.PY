# def sample(a):
#     sum=0
#     if a<=10:
#         sum=sum+a
       
#         return a + sample(a-1)
# print(sample(1))


def dis(n):
    if n==1:
        return n
    else:
        return n*dis(n-1)
print(dis(5))
