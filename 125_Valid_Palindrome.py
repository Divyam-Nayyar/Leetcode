def check_valid_palindrome(s):
    new_s=""
    for i in s:
        i=i.lower()
        if i in "abcdefghijklmnopqrstuvwxyz" or i in "0123456789" :
            new_s+=i
    # new_s=new_s.lower()
    print()
    print(new_s)
    if new_s!=new_s[::-1]:
        return False
    return True
s="A man, a plan, a canal: Panama"
print(check_valid_palindrome(s))