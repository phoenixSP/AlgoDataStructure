# 🟢 Contains duplicate

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

{% code overflow="wrap" %}
```python
def contains_duplicate(nums):
    '''
    Time complexity: O(n); list traversal once
    Space complexity: O(n); space for set

    Other solutions:
    - Brute force: Compare elements with each other with double for loop; TC O(n^2), SC: O(1)
    - Sorting: Sort list, if same element is present consecutively, then there are duplicates;
    TC: O(nlogn), SC: O(1)
    '''

    if nums is None or len(nums) <= 1:
        return False

    hashset = set()

    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False

```
{% endcode %}
