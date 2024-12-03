import sys
k=int(input(""))
for _ in range(k):
    n=int(input(''))-1#索引
    L=list(map(int,sys.stdin.readline().split()))
    p=1
    def f1():
        global p
        p+=1
    def f2():
        global p
        p-=1
    def f3():
        global p
        p+=L[p]
    if L[p]>0:
        f3()
    while(p<n):
        f1()