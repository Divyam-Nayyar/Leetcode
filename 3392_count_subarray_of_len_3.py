def countSubarrays(nums):
        if len(nums)<3:
            return 0
        cnt=0
        for i in range(0,len(nums)-2):
            print(nums[i],nums[i+1],nums[i+2])
            if ((nums[i]+nums[i+2])==(nums[i+1]/2)):
                cnt+=1
        return cnt
print(countSubarrays([2,-7,-6]))