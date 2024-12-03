
a=int(input(""))
for i in range(a):
    l=input("")
    t=1
    l=l.split()
    x=int(l[0])
    y=int(l[1])
    
    """if y<=1:
        print(-1)
    else:
        while(x>y):
            x=x-y
            if x>0:
                t+=2
            x+=1
            
        print(t)"""
    n=x//(y-1)
    n*=2
    n-=1