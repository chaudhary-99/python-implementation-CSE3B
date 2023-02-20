def binary_search(arr, x):
    """
    Perform binary search to find x in the given sorted array.
    
    Returns the index of the element if found, else returns -1.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1