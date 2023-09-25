from os import *
from sys import *
from collections import *
from math import *
def merge(arr,low,mid,high):
        count=0
        left=low
        right=mid+1
        temp = []
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                count+= mid-left+1
                right+=1

        while left <= mid:
            temp.append(arr[left])
            left+=1
        while right <= high:
            temp.append(arr[right])
            right+=1
        for i in range(low,right):
            arr[i] = temp[i-low]
        return count
def mergeSort(arr,low,high):
        count=0
        if low >= high:
            return count
        mid = (low+high)//2
        count+=mergeSort(arr,low,mid)
        count+=mergeSort(arr,mid+1,high)
        count+=merge(arr,low,mid,high)
        return count
def getInversions(arr, n) :
	# Write your code here.
    # count=0
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if i < j and arr[i] > arr[j]:
    #             count+=1
    # return count

    
    
    return mergeSort(arr,0,n-1)
    
# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))