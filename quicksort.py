from typing import List

def quicksort(lst: List[int]) -> List[int]:
    if len(lst) < 2:
        return lst
    pivot = lst.pop((len(lst) - 1) // 2)
    left = [el for el in lst if el <= pivot]
    right = [el for el in lst if el > pivot]
    print(pivot, left, right)
    return quicksort(left) + [pivot] + quicksort(right)
