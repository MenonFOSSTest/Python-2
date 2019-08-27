n=int(input("ENTER A NUMBER:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(n,"IS NOT PRIME")
            break
else:
    print(n,"IS PRIME")
