def f(i,x,y):
    if i==1:
        return x
    elif i==2:
        return y
    else:
        return f(i-1,x,y)+f(i-2,x,y)
    
n=int(input(""))
for i in range(n):
    a,b,k=map(int,input('').split())
    if f(k,a,b)%2==0:
        print(0)
    else:
        print(1)
