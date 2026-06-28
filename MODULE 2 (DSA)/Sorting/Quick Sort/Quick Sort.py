# Function to partition the array
def partition(arr, low, high):

    # Choose the last element as the pivot
    pivot = arr[high]

    # Index of smaller element
    i = low - 1

    # Compare each element with the pivot
    for j in range(low, high):

        if arr[j] < pivot:
            i += 1

            # Swap smaller element to the left
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# Quick Sort function
def quick_sort(arr, low, high):

    if low < high:

        # Find pivot index
        pi = partition(arr, low, high)

        # Sort left subarray
        quick_sort(arr, low, pi - 1)

        # Sort right subarray
        quick_sort(arr, pi + 1, high)


# Driver Code
arr = [5, 3, 8, 4, 2]

print("Original:", arr)

quick_sort(arr, 0, len(arr) - 1)

print("Sorted :", arr)
