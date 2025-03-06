a=[1,1,1,1,2,2,3,3,3,4,4,4,4,4,5,5]
st=set(a)
stl=[i for i in st]
extra=[-1]*(len(a)-len(stl))
print(stl+extra)