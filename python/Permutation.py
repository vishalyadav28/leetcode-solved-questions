class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate_permutations(arr, start=0):
            result = []
            if start == len(arr):
                result.append(arr.copy())
            else:
                for i in range(start, len(arr)):
                    arr[start], arr[i] = arr[i], arr[start]
                    result.extend(generate_permutations(arr, start + 1))
                    arr[start], arr[i] = arr[i], arr[start]  # backtrack
            return result
        return generate_permutations(nums)
        
        