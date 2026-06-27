def first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            ans = mid
            right = mid - 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return ans


def last_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            ans = mid
            left = mid + 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return ans


def count_occurrences(arr, target):
    first = first_occurrence(arr, target)

    if first == -1:
        return 0

    last = last_occurrence(arr, target)
    "formula for find occurrences"

    return last - first + 1   


arr = [4,4,4,4,7,8]
target = 4

print(count_occurrences(arr, target))