Quick Sort

Quick Sort is a Divide and Conquer sorting algorithm.

It works by selecting a pivot element, placing it in its correct position, and then recursively sorting the elements on the left and right of the pivot.


## Algorithm

1. Choose a pivot element.
2. Partition the array:
   - Place elements smaller than the pivot on the left.
   - Place elements larger than the pivot on the right.
3. Place the pivot in its correct position.
4. Recursively apply Quick Sort to the left subarray.
5. Recursively apply Quick Sort to the right subarray.
6. Stop when the subarray has 0 or 1 element.

## Time Complexity

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n²)

## Space Complexity

- O(log n)
