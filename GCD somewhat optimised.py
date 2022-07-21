l1=[]
l2=[]
m=int(input())
n=int(input())
"""for i in range(1,min(m,n)+1):
    if m%i==0 and n%i==0:
        l1.append(i)
print("the GCD will be", max(l1))

for i in range(1, min(m,n)+1):
    if m%i==0 and n%i==0:
        x=i
print(x)
"""
x=min(m,n)
while x>0:
    if m%x==0 and n%x==0:
        print("the GCD will be",x)
        break
    else:
        i=i-1

