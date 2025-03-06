nums=[4,0]

for i in range(0,len(nums)):
    print(nums[0:i])
    left_sum=sum(nums[0:i])
    print(left_sum)
    right_sum=sum(nums[i+1:len(nums)])
    print(right_sum)
    if left_sum==right_sum:
        print(i)
