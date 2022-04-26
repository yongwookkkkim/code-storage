def func(arr, n):
    res=0
    for item in arr:
        res+=item//n
    return res

inp=input().split(" ")
n=int(inp[1])
nums=[]
for _ in range(int(inp[0])):
    nums.append(int(input()))
l=0
r=2147483647

while(l<r):
    mid=(l+r)//2
    if (func(nums, mid)>=n):
        l=mid+1
    else:
        r=mid-1
print(r)