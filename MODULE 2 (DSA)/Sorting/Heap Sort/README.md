Heap Sort:
Heap Sort is a comparison-based sorting algorithm that uses a Binary Heap (usually a Max Heap) to sort elements.

It works in 2 phases:
Build a Max Heap from the array.
Repeatedly swap the root (largest element) with the last element, reduce the heap size, and restore the heap.

## Algorithm

1. Build a Max Heap from the array.
2. Swap the root (largest element) with the last element.
3. Reduce the heap size by one.
4. Heapify the root to restore the Max Heap.
5. Repeat steps 2–4 until only one element remains.
6. The array is sorted.

## Time Complexity

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

## Space Complexity

- O(1)
