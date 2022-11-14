nums = [int(i) for i in input()]
k=int(input())
l=list((k,))
for i in range(len(nums)):
    l.append((l[i]^nums[i]))
print(l)