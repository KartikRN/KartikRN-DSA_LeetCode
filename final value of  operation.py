import time
start = time.time()
nums = ["--X","X++","X++"]
x=0
for i in nums:
    if "-" in i:
        x-=1
    elif "+" in i:
        x+=1
print(x)
end=time.time()
print(end-start)