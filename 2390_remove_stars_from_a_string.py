s = "leet**cod*e"
lst=[]
for i in s:
    if i!="*":
        lst.append(i)
    else:
        if len(lst)>0:
            lst.pop(-1)
print("".join(lst)) 