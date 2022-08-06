#def bsearch(l,n):
    #if n%2!=0:
        
    
l=[45,32,56,72,43,56,67,56]
l1=l
l.sort()

#x=float(input())
x=72
while(len(l1)!=0):
    n=len(l1)
    print(l1)
    if n%2!=0:
        i=n//2
        if x>l1[i]:
            l1=l1[i:]
            print(l1)
        elif x==l1[i]:
            print("found it", l1[i])
            break
        elif x<l1[i]:
            l1=l1[0:i]
            print(l1)
    else:
        i=n//2
        if x==l1[i]:
            print("found it", l1[i])
            break
        elif x<l1[i]:
            l1=l1[0:i]
            print(l1)
        elif x>l1[i]:
            l1=l1[i:]
            print(l1)
if l1==[]:
    print("not available")
    

            
