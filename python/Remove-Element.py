class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # solution 1
        while val in nums: nums.remove(val)
        
        # solution 2
        # nums [:] = (i for i in nums if i!= val)