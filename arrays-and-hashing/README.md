# Arrays and Hashing

## Introduction

* Subarray - A range of contiguous values within an array.
  * Example: given an array `[2, 3, 6, 1, 5, 4]`, `[3, 6, 1]` is a subarray while `[3, 1, 5]` is not a subarray.
* Subsequence - A sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements.
  * Example: given an array `[2, 3, 6, 1, 5, 4]`, `[3, 1, 5]` is a subsequence but `[3, 5, 1]` is not a subsequence.

## Time Complexity

| Operation                 | Big-O	  | Note                                                                                                 |
| ------------------------- | ------- | ---------------------------------------------------------------------------------------------------- |
| Access                    | O(1)    |                                                                                                      |
| Search                    | O(n)    |                                                                                                      |
| Sorted search             | O(logn) |                                                                                                      |
| Insertion                 | O(n)    | Insertion would require shifting all the subsequent elements to the right by one and that takes O(n) |
| Insert (at the end)       | O(1)    | No element need to be shifted                                                                        |
| Remove/pop using index    | O(n)    | Removal would require shifting all the subsequent elements to the left by one and that takes O(n)    |
| Remove (at the end)/pop() | O(1)    | No element need to be shifted                                                                        |

## Techniques

* Sliding window
* Two pointers
* Sorting the array

## Gotcha points

* Empty sequence
* Sequence with 1 or 2 elements
* Sequence with repeated elements
* Duplicated values in the sequence

