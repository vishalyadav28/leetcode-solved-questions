class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:

        #bruteforce
        # longest = 1
        # def linearSearch(nums,num):
        #     for i in nums:
        #         if num == i:
        #             return True
        #     return False
    
        # for i in nums:
        #     x = i
        #     count = 1
        #     while linearSearch(nums,x+1):
        #         count+=1
        #         x+=1
        #     longest = max(longest,count)
        # return longest
        #Better
        n=len(nums)
        if n==0:
            return 0
        nums.sort()
        lastSmaller=float('-inf')
        count = 0
        longest=1
        for i in range(len(nums)):
            if nums[i]-1 == lastSmaller:
                count += 1
                lastSmaller = nums[i]
            elif nums[i] != lastSmaller:
                count = 1
                lastSmaller = nums[i]
            longest = max(count,longest)
        return longest
        