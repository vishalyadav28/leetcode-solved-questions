class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,low,mid,high):
            left=low
            right=mid+1
            temp = []
            while left<=mid and right<=high:
                if arr[left]<=arr[right]:
                    temp.append(arr[left])
                    left+=1
                else:
                    temp.append(arr[right])
                    right+=1

            while left <= mid:
                temp.append(arr[left])
                left+=1
            while right <= high:
                temp.append(arr[right])
                right+=1
            for i in range(low,right):
                arr[i] = temp[i-low]
        def mergeSort(arr,low,high):
            if low >= high:
                return
            mid = (low+high)//2
            mergeSort(arr,low,mid)
            mergeSort(arr,mid+1,high)
            merge(arr,low,mid,high)
        arr=nums
        mergeSort(arr,0,len(nums)-1)
        return arr
        
        
        