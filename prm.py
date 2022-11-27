def Find(n):
    eve=0
    odd=0
    prm=0
    for x in range(2,n):
        if n%2==0:
            eve=1
            
            
        else:
            odd=1
            

    else:
        prm=1
    
    if bool(eve):
        if bool(prm):
            return (f"num {n} is Prime Even num")
        else:
            return (f"num {n} is Even num")
    elif bool(odd):
        if bool(prm):
            return (f"num {n} is Prime Odd num")
        else:
            return (f"num {n} is Odd num")
    elif n==0:
        return (f"num {n} is Zero")
    else:
        return (f"num {n} is Even Prime num")
        
