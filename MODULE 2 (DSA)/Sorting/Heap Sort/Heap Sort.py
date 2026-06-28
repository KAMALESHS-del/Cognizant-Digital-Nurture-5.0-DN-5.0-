
def heap(arr, n, i):

    # Assume current node is largest
    largest = i

    # Left child index
    left = 2 * i + 1

    # Right child index
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:

        # Swap
        arr[i], arr[largest] = arr[largest], arr[i]

        # Heapify the affected subtree
        heap(arr, n, largest)


# Heap Sort function
def heap_sort(arr):

    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heap(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):

        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify the reduced heap
        heap(arr, i, 0)


arr = [5, 3, 8, 4, 2]

print("Original:", arr)

heap_sort(arr)

print("Sorted :", arr)
