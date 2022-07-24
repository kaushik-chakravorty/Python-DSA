def factorial(n):
    
    if n>0:
        product=n*factorial(n-1)
    else:
        return(1)
    return(product)
n=5
print("factorial value is", factorial(n))

    
