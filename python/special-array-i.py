class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # def check_even_odd(i):
        #     return "even" if nums[i] % 2 == 0 else "odd"
        
        # last = ""
        # if len(nums)<=1:
        #     return True
        # for i in range(len(nums)):
        #     ouput = check_even_odd(i)
        #     if last != ouput:
        #         last = ouput
        #     else:
        #         return False
        # return True

        for i in range(len(nums)-1):
            if (nums[i]%2 == nums[i+1]%2):
                return False
        return True

        
