# question https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        count=0
        for i in nums:
            for j in range(len(nums)):
                if (nums[j]-i)<0:
                    count+=1
            ans.append(count)
            count=0
        return ans
