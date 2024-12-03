import sys
L=list(map(int,sys.stdin.readline().split()))
if L[0]==0:
    print(L[1]+L[2])
if L[0]:
    print(max(L[1]-L[3],0)+max(L[2]-L[4],0))