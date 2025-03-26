nums = [1,2,2,3,1,4]
freq=[]
nos=[]
for i in nums:
    if i not in nos:
        freq.append(nums.count(i))
        nos.append(i)
print(freq)
print(max(freq)*freq.count(max(freq)))