def insertion_sort(arr):
    """
    Perform insertion sort on the given array in-place.
    """
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1