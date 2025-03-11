def selection_Sort(array):
    n = len(array)
    for i in range(n):
        min_Index = i
        for j in range(i + 1, n):
            if array[j] < array[min_Index]:
                min_Index = j
        array[i], array[min_Index] = array[min_Index], array[i]
    return array

if __name__ == "__main__":
    test_Cases = [
            [],
            [1],
            [2, 3, 1],
            [3, 5, 4 ,1 ,2],
            [1, 2, 3, 4, 5],
            [1, 6, 7, 3, 8, 0, 0, 0, -6, -2, 4]
    ]
    for i, test in enumerate(test_Cases):
        sorted_Array = selection_Sort(test[:])
        print(f"Test cases {i + 1}: {sorted_Array}")
