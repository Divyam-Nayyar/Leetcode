arr=[-1,-1,1]
k =0
prefix_sum=[0]*(len(arr)+1)
for i in range(len(arr)):
    prefix_sum[i+1]=prefix_sum[i]+arr[i]
print(prefix_sum)
count=0
for j in range(len(prefix_sum)):
    for l in range(j+1,len(prefix_sum)):
        if prefix_sum[l]-prefix_sum[j]==k:
            print(prefix_sum[l],prefix_sum[j])   
            count+=1
            
print(count)