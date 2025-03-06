nums=[0,0]
right_sum=sum(nums)
left_sum=0
cnt=0
for i in range(len(nums)):
    if i==len(nums)-1:
        break
    left_sum+=nums[i]
    right_sum-=nums[i]
    print(left_sum,right_sum)
    if left_sum>=right_sum:
        cnt+=1
print(cnt)