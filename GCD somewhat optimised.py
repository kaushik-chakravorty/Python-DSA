

m=int(input())
n=int(input())
if m>n:
    larger=m
    smaller=n
else:
    larger=n
    smaller=m
l1=[]
l2=[]
for i in range(1,smaller+1):
    if smaller%i==0:
        l1.append(i)
for i in l1:
    if larger%i==0:
        l2.append(i)
print("the GCD for two numbers is", max(l2))
