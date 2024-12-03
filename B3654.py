L=[]
str_=""
while True:
    a=input("")
    if a=="0":
        break
    if a not in L:  
        L.append(a)  
for i in L:
    str_+=i
print(str_)




















# L = []  
# str_ = ""  

# while True:  
#     a = input("")  
#     if a == "0":  
#         break  
#     # 只有在L中没有这个元素时，才添加它  
#     

# # 拼接列表中的元素  
# for i in L:  
#     str_ += i  

# print(str_)