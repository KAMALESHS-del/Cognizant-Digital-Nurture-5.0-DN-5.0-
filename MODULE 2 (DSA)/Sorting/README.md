Sorting in Data Structures and Algorithms (DSA)

Sorting is the process of arranging data in a particular order, usually:

Ascending order: 10, 20, 30, 40
Descending order: 40, 30, 20, 10


Why do we use Sorting?

Sorting helps in:

Faster searching (Binary Search requires sorted data)
Easy data analysis
Removing duplicates
Finding minimum/maximum quickly
Better organization of records

| Sorting Algorithm  | Where It Is Used                                                  | Why                                            |
| ------------------ | ----------------------------------------------------------------- | ---------------------------------------------- |
| **Bubble Sort**    | Learning, very small datasets                                     | Easy to understand and implement               |
| **Selection Sort** | Small embedded systems, memory-limited devices                    | Performs fewer swaps                           |
| **Insertion Sort** | Nearly sorted data, small arrays                                  | Very fast for almost sorted data               |
| **Merge Sort**     | Databases, external sorting, linked lists                         | Stable and guaranteed O(n log n)               |
| **Quick Sort**     | Programming libraries, operating systems, general-purpose sorting | Very fast average-case performance             |
| **Heap Sort**      | Priority queues, CPU scheduling, task scheduling                  | Guaranteed O(n log n) and in-place             |
| **Counting Sort**  | Student marks, ages, IDs (small integer ranges)                   | Very fast for limited-range integers           |
| **Radix Sort**     | Phone numbers, ZIP codes, employee IDs                            | Efficient for fixed-length integers or strings |


**Sorting Algorithms Complexity Table**
| Algorithm | Best       | Average    | Worst      | Space    |
| --------- | ---------- | ---------- | ---------- | -------- |
| Bubble    | O(n)       | O(n²)      | O(n²)      | O(1)     |
| Selection | O(n²)      | O(n²)      | O(n²)      | O(1)     |
| Insertion | O(n)       | O(n²)      | O(n²)      | O(1)     |
| Merge     | O(n log n) | O(n log n) | O(n log n) | O(n)     |
| Quick     | O(n log n) | O(n log n) | O(n²)      | O(log n) |
| Heap      | O(n log n) | O(n log n) | O(n log n) | O(1)     |
| Counting  | O(n+k)     | O(n+k)     | O(n+k)     | O(n+k)   |
| Radix     | O(d(n+k))  | O(d(n+k))  | O(d(n+k))  | O(n+k)   |

##Memory Tip##
Bubble, Selection, Insertion → Simple but slow (O(n²))
Merge, Quick, Heap → Efficient comparison sorts (O(n log n))
Counting, Radix → Special-purpose linear-time sorts (non-comparison based).

