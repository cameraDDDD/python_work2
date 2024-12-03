import sys
def bubble_sort(nums: list[int]):
    """冒泡排序"""
    n = len(nums)
    # 外循环：未排序区间为 [0, i]
    for i in range(n - 1, 0, -1):
        # 内循环：将未排序区间 [0, i] 中的最大元素交换至该区间的最右端
        for j in range(i):
            if nums[j] > nums[j + 1]:
                # 交换 nums[j] 与 nums[j + 1]
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
L=[]
m,n=map(int,input("").split())
a=[0,0,0,0,0]
for i in range(n):
    L=list(map(int,sys.stdin.readline().split()))
    bubble_sort(L)
    index=0
    ke=0
    for i in L:
        
        if m>=i:
            index+=1
            ke+=1
        
        elif m<i:
            if index==0:
                break
            m-=L[index-1]
            a[L[index-1]-1]+=1
            break
        if ke==5:
            a[L[4]-1]+=1
            m-=L[index-1]

print(f"{a[0]} {a[1]} {a[2]} {a[3]} {a[4]} ")
print(m)

    
