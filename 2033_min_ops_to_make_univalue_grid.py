class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        all_elements=[num for row in grid for num in row]
        if any((num-all_elements[0])%x!=0 for num in all_elements):
            return -1
        all_elements.sort()
        uni_value=all_elements[len(all_elements)//2]
        operations=sum(abs(num-uni_value)//x for num in all_elements)
        return operations
        # for j in range(len(all_elements)):
        #     while all_elements[j]!=uni_value:
        #         operations+=1
        #         if all_elements[j]>uni_value :
        #             all_elements[j]-=x
        #             if all_elements[j]<uni_value:
        #                 return -1
        #         elif all_elements[j]<uni_value:
        #             all_elements[j]+=x
        #             if all_elements[j]>uni_value:
        #                 return -1
        # return operations