##convolution of two discrete time signals using python
##let two signals be

import numpy as np
def convolution(fl,rl,n):
    z=[]
    for i in range(n):
        z.append(sum(np.multiply(fl[len(fl)-1-i:],rl[0:i+1])))
    return(z)
l1=[1,2,3]
l2=[1,2,3,4,5]
n=len(l1)+len(l2)-1
for i in range(n-len(l1)):
    l1.append(0)
for i in range(n-len(l2)):
    l2.append(0)
l1.reverse()
fl=l1
rl=l2
z=convolution(fl,rl,n)
print("the result of convolution of two discrete signals are as follows", z)
                 
        
        
        
