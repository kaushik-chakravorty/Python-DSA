l=[34,65,7,2,4,6,7,8,5,4,3,6,24,445,445,76,56]
x=l[0]
for i in range(0,len(l)-1):
    if x<l[i+1]:
        x=l[i+1]
        print(x)
print("maximum value of array will be ", x)
