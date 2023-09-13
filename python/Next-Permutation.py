
#Generate List of permutations=========================================>

# # Python function to print permutations of a given list
# def permutation(lst):
 
#     # If lst is empty then there are no permutations
#     if len(lst) == 0:
#         return []
 
#     # If there is only one element in lst then, only
#     # one permutation is possible
#     if len(lst) == 1:
#         return [lst]
 
#     # Find the permutations for lst if there are
#     # more than 1 characters
 
#     l = [] # empty list that will store current permutation
 
#     # Iterate the input(lst) and calculate the permutation
#     for i in range(len(lst)):
#        m = lst[i]
 
#        # Extract lst[i] or m from the list.  remLst is
#        # remaining list
#        remLst = lst[:i] + lst[i+1:]
 
#        # Generating all permutations where m is first
#        # element
#        for p in permutation(remLst):
#            l.append([m] + p)
#     print (l)
 
 
# permutation([1,2,3])

# Driver program to test above function
# data = [1,2,3]
# for p in permutation(data):
#     print (p)



#================================================>

# arr=[1,2,3]

# i=len(arr)-2

# while arr[i] >= arr[i+1]:
#     i-=1
# if i==-1:
#     print(arr[::-1])
# j=len(arr)-1
# while arr[j]<=arr[i]:
#     j-=1

# arr[i],arr[j]=arr[j],arr[i]

# arr[i+1:] = reversed(arr[i+1:])

# print(arr)
#===================================================>
class Solution:
    def nextPermutation(self, nums: List[int],start=0) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-2

        #find the break point 
        while i>=0 and nums[i] >= nums[i+1]:
            i-=1
        #check i==-1 means last element then need to return first element 
        if i==-1:
            return nums.reverse()
        # else go for the num ie. <=arr[i] then swap
        j=len(nums)-1
        while nums[j]<=nums[i]:
            j-=1

        nums[i],nums[j]=nums[j],nums[i]
        # reversed the num from break point +1 then return
        nums[i+1:] = reversed(nums[i+1:])

        return(nums)

        