s="abc"
shifts=[[0,1,0],[1,2,1],[0,2,1]]
alphabets="abcdefghijklmnopqrstuvwxyz"
slist=[i for i in s]
for j in shifts:
    a,b,c=j
    for k in range(a,b+1):
        letter=slist[k]
        ind=alphabets.index(letter)
        if c==0:
            ind-=1
            # print(ind)
        elif c==1:
            ind+=1

            if ind>len(alphabets)-1:
                ind=ind%len(alphabets)
            # print(ind)
        letter=alphabets[ind]
        slist[k]=letter
print("".join(slist))