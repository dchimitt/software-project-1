def insertion_sort(arr):
    """Sorts a list using the insertion sort algorithm.

    Args:
        arr: The list to be sorted.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
# Example usage:
data = [12, 11, 13, 5, 6]
insertion_sort(data)
print(data)  # Output: [5, 6, 11, 12, 13]
