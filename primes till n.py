def primestilln(n):
    lprimes=[]
    for i in range(2,n+1):
        count=0
        for j in range(2,i):
            if i%j==0:
                break
            else:
                count=count+1
        if count>0:
            lprimes.append(i)

    return(lprimes)
n=100
print("list of primes till n will be", primestilln(n))


for i in range(1,5):
    print(i)
