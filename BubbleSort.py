def bubble_sort(numbers):
    length = len(numbers)
    for i in range(length):  # i represents the current pass
        for j in range(length - 1 - i):  # j represents the current index
            if numbers[j] > numbers[j + 1]:
                temp_value = numbers[j]  # Use a temporary variable for swapping
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp_value
    return numbers
