def binary_search(arr:list, target:int) -> int:
    """
    Searching an element in a sorted array using 
    binary search.
    """
    lo, hi = 0, len(arr) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            hi = mid - 1
        elif target > arr[mid]:
            lo = mid + 1

    return -1


if __name__ == "__main__":
    arr1 = [1, 2, 5, 6, 7, 9, 10, 12, 15]
    print(binary_search(arr1,5) == 2)
    print(binary_search(arr1, 4) == -1)
    print(binary_search(arr1, 15) == 8)