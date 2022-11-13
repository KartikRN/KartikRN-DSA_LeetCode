nums=[[1,5],[7,3],[3,5]]
k=[]
for i in nums:
    s=0
    for j in i:
        s+=j
    k.append(s)
print(max(k))