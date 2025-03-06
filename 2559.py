def vowelStrings(words, queries):
    res=[]
    vowels="aeiou"
    for i in queries:
        li=i[0]
        ri=i[1]
        count=0
        print(words[li:ri+1])
        for j in range(li,ri+1):
            word=words[j]
            if word[0] and word[-1] in vowels:
                count+=1
                print(word)
        res.append(count)
    return res

words=["bzmxvzjxfddcuznspdcbwiojiqf","mwguoaskvramwgiweogzulcinycosovozppl","uigevazgbrddbcsvrvnngfrvkhmqszjicpieahs","uivcdsboxnraqpokjzaayedf","yalc","bbhlbmpskgxmxosft","vigplemkoni","krdrlctodtmprpxwditvcps","gqjwokkskrb","bslxxpabivbvzkozzvdaykaatzrpe","qwhzcwkchluwdnqjwhabroyyxbtsrsxqjnfpadi","siqbezhkohmgbenbkikcxmvz","ddmaireeouzcvffkcohxus","kjzguljbwsxlrd","gqzuqcljvcpmoqlnrxvzqwoyas","vadguvpsubcwbfbaviedr","nxnorutztxfnpvmukpwuraen","imgvujjeygsiymdxp","rdzkpk","cuap","qcojjumwp","pyqzshwykhtyzdwzakjejqyxbganow","cvxuskhcloxykcu","ul","axzscbjajazvbxffrydajapweci"]
queries=[[7,12]]
print(vowelStrings(words,queries))