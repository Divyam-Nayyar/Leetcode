from collections import Counter
nums = [-1,1,-6,4,5,-6,1,4,1]
a=Counter(nums)
# lst=list(a.items())
# res=[]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if lst[i][1]>lst[j][1]:
#             lst[i],lst[j]=lst[j],lst[i]
#         if lst[i][1]==lst[j][1]:
#             if lst[i][0]<lst[j][0]:
#                 lst[i],lst[j]=lst[j],lst[i]
# for k in range(len(lst)):
#     for l in range(lst[k][1]):
#         res.append(lst[k][0])
# print(res)


'''Method 2'''
sorted_items = sorted(a.items(), key=lambda x: (x[1], -x[0]))
res=[]
for i,freq in sorted_items:
    for j in range(freq):
        res.insert(i)

print(res)