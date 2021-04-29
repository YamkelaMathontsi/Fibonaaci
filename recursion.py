# defining my fibo function
def fibo(z):
   if z <= 1:
       return z
   else:
       return(fibo(z-1) + fibo(z-2))

# using for loop

for z in range(20):
    print(str(fibo(z)), end=" ")
