nums = [int(i) for i in input()]
l=sorted(nums)
print(l)
k=[]
for i in nums:
    k.append(l.index(i))
print(k)