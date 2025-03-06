class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        all_nums=[]
        res=[]
        missing=0
        for i in grid:
            all_nums+=i
        for j in range(len(all_nums)):
            if all_nums.count(j+1)>1:
                res.append(j+1)
            if j+1 not in all_nums:
                missing=j+1
        res.append(missing)
        return res
        