# Arrays and Hashing

## Array&#x20;

#### Introduction

* Subarray - A range of contiguous values within an array.
  * Example: given an array `[2, 3, 6, 1, 5, 4]`, `[3, 6, 1]` is a subarray while `[3, 1, 5]` is not a subarray.
* Subsequence - A sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements.
  * Example: given an array `[2, 3, 6, 1, 5, 4]`, `[3, 1, 5]` is a subsequence but `[3, 5, 1]` is not a subsequence.

#### Time Complexity

<table><thead><tr><th width="264">Operation</th><th width="228">Big-O	</th><th>Note</th></tr></thead><tbody><tr><td>Access</td><td>O(1)</td><td></td></tr><tr><td>Search</td><td>O(n)</td><td></td></tr><tr><td>Sorted search</td><td>O(logn)</td><td></td></tr><tr><td>Insertion</td><td>O(n)</td><td>Insertion would require shifting all the subsequent elements to the right by one and that takes O(n)</td></tr><tr><td>Insert (at the end)</td><td>O(1)</td><td>No element need to be shifted</td></tr><tr><td>Remove/pop using index</td><td>O(n)</td><td>Removal would require shifting all the subsequent elements to the left by one and that takes O(n)</td></tr><tr><td>Remove (at the end)/pop()</td><td>O(1)</td><td>No element need to be shifted</td></tr></tbody></table>

#### Techniques

* Sliding window
* Two pointers
* Sorting the array
* Traversing from the right instead of the left
* Precomputation of subarray operation
* Using a hashmap for the indices
* Traversing the array more than once

#### Gotcha points

* Empty sequence
* Sequence with 1 or 2 elements
* Sequence with repeated elements
* Duplicated values in the sequence
* Be mindful about slicing or concatenating arrays in your code. Typically, slicing and concatenating arrays would take O(n) time. Use start and end indices to demarcate a subarray/range where possible.



## Hashtable

#### Introduction

A hash map is an abstract data structure that can map keys to values. It is the most common example of a space-time tradeoff.

In the case of hash collisions, there are a number of collision resolution techniques that can be used. You will unlikely be asked about details of collision resolution techniques in interviews:

* **Separate chaining** - A linked list is used for each value, so that it stores all the collided items.
* **Open addressing** - All entry records are stored in the bucket array itself. When a new entry has to be inserted, the buckets are examined, starting with the hashed-to slot and proceeding in some probe sequence, until an unoccupied slot is found.

#### Time Complexity

| Operation | Big-O | Notes                                                |
| --------- | ----- | ---------------------------------------------------- |
| Access    | N/A   | Accessing not possible as the hash code is not known |
| Search    | O(1)  | Average case                                         |
| Insert    | O(1)  | Average case                                         |
| Remove    | O(1)  | Average case                                         |
