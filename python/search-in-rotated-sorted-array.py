def search(nums, target) :
    # Write your code here.
    # pass
    #O(N)
    # def search(arr, target) :
    # n = len(nums)
    
    # # Iterate through the array
    # for i in range(n) :
        
    #     # target is found at ith index
    #     if(nums[i] == target) :
    #         return i

    # # target not found
    # return -1
    
    #O(logn)
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
    