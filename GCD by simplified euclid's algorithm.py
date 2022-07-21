def GCD(m,n):
    #assumption is m>=n
    if m<n:
        (m,n)=(n,m)
    print(m,n)
    if m%n==0:
        return(n)
    else:
        r=m%n 
        return(GCD(n,r))
a=int(input())
b=int(input())
print("GCD by simplifies euclid's algorithm is", GCD(a,b))
