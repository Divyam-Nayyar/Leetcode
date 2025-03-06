s=["flower","flight","flow"]
st=set(s)
print(st)
mi=set(min(s,key=len))
print(mi.intersection(s))