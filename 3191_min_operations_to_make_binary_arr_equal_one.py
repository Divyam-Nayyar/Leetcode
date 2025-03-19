def minOperations(nums):
    cnt=0
    res=[1]*len(nums)
    for i in range(len(nums)-2):
        if nums[i]==0:
            cnt+=1
            for j in range(i,i+3):
                nums[j]=1-nums[j]
    if res==nums:
        return cnt
    else:
        return -1
nums=[0,1,1,1,0,0]
print(minOperations(nums))