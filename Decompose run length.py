nums = [int(i) for i in input()]
k=[]
for i in range(0,int(len(nums)/2)):
    k.extend(list((nums[(2*i)+1],))*nums[2*i])
print(k)