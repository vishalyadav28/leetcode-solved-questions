#Solution #1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            n=target-nums[i]
            if n in result:
                return[i,nums.index(n)]
            result.append(nums[i])

#Solution #2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for key,value in enumerate(nums):
            n = target - value
            if n not in hash:
                hash[value] = key
            else:
                return [hash[n],key]

        