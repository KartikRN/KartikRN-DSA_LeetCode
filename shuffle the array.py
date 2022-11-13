import time

nums = [int(i) for i in input()]
m=int(input())
start = time.time()
k=nums[:m]
l=nums[m:]
list3 = [item for sublist in zip(k, l) for item in sublist]
print(list3)
end=time.time()
print(end-start)