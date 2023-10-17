from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    # Write your code here.
    #using extra space and a loop
    # i=len(arr)-1
    # temp = []
    # while i > m:
    #     temp.append(arr[i])
    #     i-=1
    # return arr[:m+1] + temp
    #reverse array
    start = m+1
    end = len(arr)-1
    while start <= end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
    return arr
    
