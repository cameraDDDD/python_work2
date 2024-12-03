str_list=input("")
str_list=str_list.split()
n=int(str_list[0])
m=int(str_list[1])
p=int(str_list[2])
sum=0
lim=n-m
if n>=m:
    sum+=1
sum+=lim//p
print(sum)