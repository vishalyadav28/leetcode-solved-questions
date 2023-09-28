class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_len = 0
        for i in range(len(nums)):
            if nums[i]!= 0:
                count+=1
                max_len = max(count,max_len)
            else:
                count=0
        return max_len
            
        