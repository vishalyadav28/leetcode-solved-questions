    class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # et = 0
        # at = 0
        # for i in range(0,len(nums)):
        #     et += nums[i]
        # for j in  range(1,len(nums)+1):
        #     at = at + j
        # return at - et
        n = len(nums)+1
        expected_num = n*(n-1) // 2
        total = sum(nums)
        return expected_num - total


        