words=["a","aba","ababa","aa"]
res=[]
cnt=0
for i in range(len(words)):
    l1=len(words[i])
for j in range(i+1,len(words)):
    if words[i]==words[j][:l1] and words[i]==words[j][-l1:]:
        cnt+=1
print(len(res))
