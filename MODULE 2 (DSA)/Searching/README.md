What is Searching?

Searching means:

Finding whether an element exists in a collection, and if it does, finding its position.

Example:

Array = [10, 20, 30, 40, 50]

Target = 30

Output:

Element found at index 2
Types of Searching

There are 2 main searching algorithms:

Linear Search
Binary Search

1. Linear Search
When to use?
Array can be sorted or unsorted.
Simple to implement.
Example
Array = [10, 20, 30, 40, 50]

Target = 40

Start from the first element.

10 == 40 ❌

20 == 40 ❌

30 == 40 ❌

40 == 40 ✅

Found at index 3.


===================================================================================

  "Binary Search"


2. Binary Search
When to use?

✅ Only on a sorted array.

Example:

Array = [10, 20, 30, 40, 50]

Target = 40

Instead of checking every element, Binary Search checks the middle.

Middle:

30

Since:

40 > 30

Ignore the left half.

Search only:

40 50

Middle:

40

Found.
