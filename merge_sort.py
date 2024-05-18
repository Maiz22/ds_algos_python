def merge_sort(nums:list) -> list:
    """
    Sorting an array by splicing the arrays in subarrays until they
    are of size 1 (sorted by definition) and merge them back 
    create a sorted list.
    """
    if len(nums) < 2:
        return nums
    index = len(nums) // 2
    left_arr = merge_sort(nums[0:index])
    right_arr = merge_sort(nums[index:])
    return merge(left_arr, right_arr)

def merge(nums1:list, nums2:list) -> list:
    """
    Merges 2 sorted arrays:
    """
    j=0
    for num in nums1:
        while j < len(nums2) and nums2[j] < num:
            j+=1
        nums2.insert(j, num)
    return nums2


if __name__ == "__main__":
    nums = [5, 3, 8, 9, 6, 5, 3, 1, 2, 10, 4, 19, 3]
    print(merge_sort(nums))