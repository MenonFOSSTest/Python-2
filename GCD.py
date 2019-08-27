d1=int(input("Enter the first number: "))
d2=int(input("Enter the second number: "))
r=d1%d2
while r!=0:
    d1=d2
    d2=r
    r=d1%d2
print(d2)
