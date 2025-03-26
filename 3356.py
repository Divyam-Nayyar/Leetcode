nums=[2,0,2]
queries=[[0,2,1],[0,2,1],[1,1,3]]
# checker=[k for k in nums]
# k=0
# for i in queries:
#     l,r,val=i
#     for j in range(l,r+1):
#         if nums[j]!=0 and nums[j]-val>=0:
#             nums[j]-=val
#     if nums!=checker:
#         k+=1
#     if nums==[0,0,0]:
#         print(f"Yes {k}")
#         break
# print("No")

if all(num==0 for num in nums):
    print(0)
else:
    non_zero_pos=[i for i,num in enumerate(nums) if num>0]
    current=nums.copy()

    for query_idx,(l,r,val) in enumerate(queries,1):

        i=0
        while i<len(non_zero_pos):
            pos=non_zero_pos[i]
            print(pos)

            if l<=pos<=r:
                current[pos]=max(0,current[pos]-val)

                if current[pos]==0:
                    non_zero_pos.pop(i)
                    i-=1
            i+=1
        
        if not non_zero_pos:
                print(query_idx)

        