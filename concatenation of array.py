import time
start = time.time()
nums = [int(i) for i in input()]
ans=[]
for i in range(0,len(nums)):
    ans.insert(i,nums[i])
    ans.insert((i+len(nums)),nums[i])
    print(ans)
end=time.time()
print(end-start)