words=["pay","attention","practice","attend"]
pref="at"
l=len(pref)
count=0
for i in range(len(words)):
    if pref==words[:l]:
        count+=1