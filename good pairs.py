nums = [int(i) for i in input()]
k=set(nums)
c=0
for i in range(0,len(nums)):
    for j in range(0,len(nums)):
        if nums[i]==nums[j] and i<j:
            c+=1
print(c)