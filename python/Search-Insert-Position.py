class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # solution 1
        # return sorted(nums + [target]).index(target)
        
        # solution 2
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     nums.append(target)
        #     nums.sort()
        # return nums.index(target)

        #solution 3
        # if target in nums:
        #     return(nums.index(target)) 
        # if len(nums) == 1:
        #     if target > nums[0]:
        #         return 1
        #     else:
        #         return 0    
            
        # else:
        #     for i in range(len(nums)-1):
        #         if target < nums[i]:
        #             return (i)
        #         if nums[i] < target and nums[i+1] > target:
        #             return(i+1)
        #     return(len(nums))