nums = [int(i) for i in input()]
n=int(input())
res=[]
for i in nums:
    if (i+n)>=max(nums):
        res.append(True)
    else:
        res.append(False)
print(res)