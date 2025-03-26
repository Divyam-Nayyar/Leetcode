arr=[1,2,3,4,5]
d=2
arr[:d],arr[d:]=arr[d:],arr[:d]
print(arr)