m=int(input())
n=int(input())
l1=[]
l2=[]
if m<n:
    for i in range(1,m+1):
        l1.append(i)
else:
    for i in range(1,n+1):
        l1.append(i)

for i in l1:
    if m%i==0 and n%i==0:
        l2.append(i)
print("the gcd for this program will be",max(l2))
