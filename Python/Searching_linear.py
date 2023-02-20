def linear_search(arr, x):
    """
    Perform linear search to find x in the given array.
    
    Returns the index of the element if found, else returns -1.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1