class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #selection sort O(n^2)
        # for i in range(len(nums)-1):
        #     min_index = i
        #     for j in range(i+1,len(nums)):
        #         if nums[min_index] > nums[j]:
        #             min_index = j
        #     nums[i], nums[min_index] = nums[min_index], nums[i]
        # return nums
        left,current,right = 0,0,len(nums)-1
        while current <=right:
            if nums[current ] == 0:
                nums[current],nums[left] = nums[left], nums[current]
                current+=1
                left+=1
            elif nums[current] == 2:
                nums[current], nums[right] = nums[right],nums[current]
                right-=1
            else:
                current+=1
        return nums 
        