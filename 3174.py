s="cb34"
# stack=[i for i in s]
# digits="0123456789"
# for j in range (len(s)-1,-1,-1):
#     print(stack)
#     if stack[j] in digits:
        
#         stack[j]=" "
#         for k in range(j-1,-1,-1):
#             if stack[k] not in digits:
#                 stack[k]=" "
#                 break

# print("res is","".join(stack).replace(" ",""))
stack=[]
digits="0123456789"
for i in s:
    if i in digits:
        stack.pop()
    else:
        stack.append(i)
print("".join(stack))
