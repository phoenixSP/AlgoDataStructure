# Interval

Interval questions are a subset of array questions where you are given an array of two-element arrays  and the two values represent a start and an end value.&#x20;

## Things to note

* Check if  `[1, 2]` and `[2, 3]` are considered overlapping intervals as it affects how you will write your equality checks
* Check if interval of `[a, b]` will strictly follow `a` < `b`&#x20;

## Corner cases

* No intervals
* Single intervals
* Two intervals
* Non-overlapping intervals
* An interval totally consumed within another interval
* Duplicate intervals (exactly the same start and end)
* Intervals which start right where another interval ends

## Techniques

* Sort the array using its start time
* check if two intervals overlap

```python
def is_overlap(a, b):
  return a[0] < b[1] and b[0] < a[1]
```

* merge overlapping intervals

```python
def merge_overlapping_intervals(a, b):
  return [min(a[0], b[0]), max(a[1], b[1])]
```

