sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

c=[]
for sentence in sentences:
    word=sentence.split(" ")
    c.append(len(word))
        
print(max(c))
