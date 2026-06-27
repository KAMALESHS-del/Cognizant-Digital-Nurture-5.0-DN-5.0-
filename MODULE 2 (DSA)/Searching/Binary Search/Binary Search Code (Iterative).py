def binary_search(arr, target):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70]
target = 50

index = binary_search(arr, target)

if index != -1:
    print("Found at index", index)
else:
    print("Not Found")