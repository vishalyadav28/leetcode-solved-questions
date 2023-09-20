class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute TLE issue
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]  == nums[j]:
        #             return nums[i]
        # dict = {}
        # for i in nums:
        #     if i not in dict:
        #         dict[i] = 1
        #     else:
        #         return i
        # now cyclic method 
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while fast!=slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
        
        