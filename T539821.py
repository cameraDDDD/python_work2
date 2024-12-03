import sys
A,B,C,K=map(int,sys.stdin.readline().split())
if A+B>=K:
    print("Yes")
else:
    print("No")
if A+C>=K:
    print("Yes")
else:
    print("No")
if C+B>=K:
    print("Yes")
else:
    print("No")