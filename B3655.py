n=int(input(""))
L=input("")
L=L.split()
day=1
sum=0
for i in range(n):
    k=int(input(""))
    if k:
        if day<3:
            sum+=int(L[0])
            day+=1
        elif day<7:
            sum+=int(L[1])
            day+=1
        elif day<30:
            sum+=int(L[2])
            day+=1
        elif day<120:
            sum+=int(L[3])
            day+=1
        elif day<365:
            sum+=int(L[4])
            day+=1
        else :
            sum+=int(L[5])
            day+=1
    else:
        day=1
print(sum)