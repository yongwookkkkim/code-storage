notFound=True
a=[1,2,3,434,1,12,1234,123,12,1123,12,4,125,4,234,1,123,43,125,23414,631445,1346,7,1,1,3,1234,1]
a.sort()
low=0
high=len(a)-1
midpos=0
inp=int(input())
while notFound and low!=high:
    midpos=(low+high)//2
    notFound=False if a[midpos]==inp else True
    if a[midpos]>inp:
        high=midpos-1
    elif a[midpos]<inp:
        low=midpos+1
if high==low and a[low]==inp:
    notFound=False

print("Not Found" if notFound else "Found")
print(midpos)