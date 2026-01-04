class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=len(nums)
        
        for i in range(arr):
            for j in range( i + 1, arr):
                if target == nums[i] + nums[j]:
                    return [i , j]