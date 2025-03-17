from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        Count=Counter(nums)
        for i in Count.values():
            if i%2==1:
                return False
        return True