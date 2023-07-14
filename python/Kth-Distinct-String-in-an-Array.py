# 2053. Kth Distinct String in an Array

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr[:] = list(filter(lambda x : arr.count(x) == 1,arr))
        if k > len(arr):
            return ""
        else:
            return arr[k-1] 