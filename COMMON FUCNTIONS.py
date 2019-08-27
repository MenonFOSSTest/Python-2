print("ENTER THE NUMBER CORRESPONDING TO THE COMMAND OF YOUR CHOICE \n1.add \n2.subtract \n3.multiply \n4.divide")
c=int(input("ENTER YOUR CHOICE"))
a=int(input("ENTER FIRST NUMBER:"))
b=int(input("ENTER SECOND NUMBER:"))
def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def mult(x,y):
    print(x*y)
def div(x,y):
    print(x/y)
while c<1 or c>4:
    c=int(input("PLEASE ENTER A VALID CHOICE:"))
if c==1:
    add(a,b)
elif c==2:
    sub(a,b)
elif c==3:
    div(a,b)
else:
    mult(a,b)
