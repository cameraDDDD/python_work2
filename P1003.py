nn = int(input(""))  
a = []  
success=0
num=0
for i in range(nn):  
    # 使用 append 方法向列表中添加元素  
    a.append(input("").split()) #注意是字符串
x,y=input("").split()
x,y=int(x),int(y)
for sq in a:
    num+=1
    m,n,p,q=sq
    m=int(m)
    n=int(n)
    p=int(p)
    q=int(q)
    
    if(x<m or y<n):
        continue#不在点的右上角
    else:
        if(m+p>=x and n+q>=y):
            success=num
        
if(success==False):
    print(-1)
else:
    print(success)







