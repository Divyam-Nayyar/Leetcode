arr1=[1,3,5]
new_arr=[x%2 for x in arr1]
cnt=new_arr.count(1)
div=3
while div<=len(new_arr):
     ncnt=cnt//div
     cnt+=ncnt
     div+=2
print(cnt)