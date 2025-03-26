nums=[0,0,1,1,1,2,2,3,3,4]
l=0
for r in range(1,len(nums)):
    if nums [r]!=nums[l]:
        l+=1
        nums[l]=nums[r]
print(l)
print(nums)
# temp=nums.copy()
# unique=[]

# for i in range(len(temp)):
#     if temp[i] in unique:
#         nums.pop(i)
#         nums.insert(i,"_")
#     else:
#         unique.append(temp[i])

# print(len(unique))