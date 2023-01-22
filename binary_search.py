from typing import List

def binary_search(n: int, nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == n:
            return mid
        elif nums[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
        print(left,right,mid)
    return -1
