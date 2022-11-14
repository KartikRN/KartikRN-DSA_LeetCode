nums = [int(i) for i in input()]
index = [int(i) for i in input()]
target=[]
for i in range(len(nums)):
    target.insert(index[i], nums[i])
print(target)