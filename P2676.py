L=[]
N,B=map(int,input("").split())
n=N
for i in range(N):
    a=int(input(""))
    L.append(a)
#冒泡排序
"""
for k in range(N):   
    for i in range(N-1):
        if L[i]>L[i+1]:
            L[i],L[i+1]=L[i+1],L[i]"""
L.sort()
while B>0:
    B=B-L[N-1]
    N-=1
print(n-N)