from collections import Counter
s = "bbcbaba"
mid_term=s[0]
hm=Counter(s)
hs=set()
count=0
for i in range(len(s)):
    mid_term=s[i]
    hm[mid_term]=hm[mid_term]-1
    if hm[mid_term]==0:
        del hm[mid_term]
    for j in hs:
        if j in hm:
            # print(hm)
            # print(hs)
            print(j+mid_term+j)
            count+=1
    hs.add(s[i])
print(hs)
print(count)

    
