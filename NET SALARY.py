def salary(x):
    ta=x*.10
    da=x*.20
    hra=x*.30
    pf=x*.12
    gross=x+ta+da+hra
    net=gross-pf
    print("the basic salary is",x)
    print("ta=",ta)
    print("da=",da)
    print("hra=",hra)
    print("pf=",pf)
    print("gross=",gross)
    print("net salary=",net)
basic=int(input("Enter the basic salary: "))
salary(basic)
