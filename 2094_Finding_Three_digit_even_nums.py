from collections import Counter
def findevennumbers(digits):
    even_digits = [i for i in digits if i%2 ==0]
    res = []
    max_digit = max(digits)
    for i in range(100,(max_digit+1)*100,2):
        Count = Counter(digits)
        can_form = False
        for j in str(i):
            if int(j) in Count.keys():

                if Count[int(j)] != 0:
                    Count[int(j)] -= 1
                    can_form = True
                else:
                    can_form = False
                    break
            else:
                can_form = False
                break
        if can_form:
            res.append(i)
    return res
    # for i in even_digits:
    #     Count = Counter(digits)
    #     ones = i
    #     Count[i] -= 1
    #     for j in Count.keys():
    #         if Count[j] != 0:
    #             tens = j
    #             Count[j] -= 1
    #         else:
    #             continue
    #         for k in Count.keys():
    #             if Count[k] != 0 and k!= 0:
    #                 hundreds = k
    #                 Count[k] -= 1
    #                 num = (hundreds*100) + (tens*10) + (ones)
    #                 res.append(num)
    #             else:
    #                 continue

    # return res

digits = [2,1,3]
print(findevennumbers(digits))
        