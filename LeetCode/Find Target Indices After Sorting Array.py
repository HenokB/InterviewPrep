#question https://leetcode.com/problems/find-target-indices-after-sorting-array/
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        index = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        for i in range(len(nums)):
            if nums[i] == target:
                index.append(i)
        return index
        
