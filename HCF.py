def hcf(a,b):
    if a>b:
        sma11=b
    else:
        sma11=a
        for i in range(1,sma11+1):
            if((a%i==0)and(b%i==0)):
                hcf=i
        return hcf
    
