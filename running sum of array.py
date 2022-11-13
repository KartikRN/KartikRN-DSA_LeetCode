nums = [int(i) for i in input()]
start = time.time()
ans=[]
ans.append(nums[0])
for i in range(1,len(nums)):
    ans.append(nums[i]+ans[i-1])
print(ans)