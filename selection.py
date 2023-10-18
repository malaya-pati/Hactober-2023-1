def selection_sort(arr):
    """
    Perform selection sort on the given array.

    Parameters:
    arr (list): An array of elements.

    Returns:
    list: The sorted array.
    """
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Find the minimum element in the unsorted portion of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example usage
unsorted_array = [64, 34, 25, 12, 22, 11, 90]

print("Unsorted array:", unsorted_array)
sorted_array = selection_sort(unsorted_array)
print("Sorted array:", sorted_array)
