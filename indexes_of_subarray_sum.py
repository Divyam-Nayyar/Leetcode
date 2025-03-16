arr=[19,23,15,6,6,2,28,2]
target=2
# i=0
# j=0
# while i<=j<=len(arr):
#     print(i,j)
#     if j==len(arr):
#         i+=1
#         j=i
#     print(sum(arr[i:j+1]))
#     if sum(arr[i:j+1])==target:
#         print([i+1,j+1])
#         break
#     else:
#         j+=1
    
prefix_sum=[0]*(len(arr)+1)
for i in range(0,len(arr)):
    prefix_sum[i+1]=arr[i]+prefix_sum[i]

j=0
k=0
