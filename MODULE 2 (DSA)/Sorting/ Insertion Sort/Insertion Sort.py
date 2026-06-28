# Function to perform Insertion Sort
def insertion_sort(arr):

    # Find the number of elements in the array
    n = len(arr)

    # Start from the second element (index 1)
    # The first element is already considered sorted
    for i in range(1, n):

        # Store the current element
        key = arr[i]

        # Start comparing from the previous element
        j = i - 1

        # Move elements that are greater than 'key'
        # one position to the right
        while j >= 0 and arr[j] > key:

            # Shift the larger element to the right
            arr[j + 1] = arr[j]

            # Move one step to the left
            j -= 1

        # Insert the key into its correct position
        arr[j + 1] = key

    # Return the sorted array
    return arr


# Driver Code
arr = [5, 3, 8, 4, 2]

print("Original Array :", arr)

sorted_arr = insertion_sort(arr)

print("Sorted Array   :", sorted_arr)
