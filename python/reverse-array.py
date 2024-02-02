from os import *
from sys import *
from collections import *
from math import *

# def reverseArray(arr, m):
#     # Write your code here.
#     #using extra space and a loop
#     # i=len(arr)-1
#     # temp = []
#     # while i > m:
#     #     temp.append(arr[i])
#     #     i-=1
#     # return arr[:m+1] + temp
#     #reverse array
#     start = m+1
#     end = len(arr)-1
#     while start <= end:
#         arr[start],arr[end] = arr[end],arr[start]
#         start+=1
#         end-=1
#     return arr


#another solution
from typing import *

# def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Write your code here
    # pass


    #solution 1 :
    #use extra space
    # arr = [0]*n
    # for i in range(n-1,-1,-1):
    #     arr[n-i-1] = nums[i]
    # return arr



    # solution 2:

    # start = 0
    # end = n-1
    # while start < end:
    #     nums[start],nums[end] = nums[end], nums[start]
    #     start+=1
    #     end-=1
    # return nums


    #solution 3: 
    #using recursion

def reverseArray(n: int, nums: List[int],start:int = 0,end:int = 0) -> List[int]:
    end = n - 1
    if start < end:
        nums[start], nums[end] = nums[end], nums[start]
        return reverseArray(n-1, nums, start + 1, end - 1)
    return nums
    
