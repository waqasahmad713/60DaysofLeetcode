class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_1= {}
        for i, num in enumerate(nums):
            if target - num in list_1:
                return ([list_1[target - num ],i])
            elif num not in list_1:
                list_1[num]=i

            




        
    