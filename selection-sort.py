from typing import List

def find_min(lst: List[int]) -> int:
    min_index = 0
    min_elem = lst[min_index]

    for idx in range(1, len(lst)):
        if lst[idx] < min_elem:
            min_elem = lst[idx]
            min_index = idx
    return min_index

def selection_sort(lst: List[int]) -> List[int]:
    sorted_list = []
    for _ in range(len(lst)):
        min_elem_idx = find_min(lst)
        sorted_list.append(lst.pop(min_elem_idx))
    return sorted_list

