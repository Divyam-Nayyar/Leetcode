def countSymmetricIntegers(self, low: int, high: int) -> int:
    cnt=0
    for i in range(low,high+1):
        strnum=str(i)
        if (len(strnum)<2) or (len(strnum)%2!=0):
            continue
        strnum1=strnum[0:len(strnum)//2]
        strnum2=strnum[len(strnum)//2:]
        sum_strnum1=sum([int(x) for x in strnum1])
        sum_strnum2=sum([int(y) for y in strnum2])
        if sum_strnum1==sum_strnum2:
            cnt+=1
    return cnt