# 🟢 Meeting room I

Problem description

1. We’ll be given a list of intervals (such as `[0, 15]`) where the first number is the start time and the last number is the end time
2. This list of intervals will be sorted by ascending order of the start times
3. We need to check if our person can attend all meetings by seeing if any intervals overlap
4. If they overlap, we should return `False` — if not, we should return `True`

```python
def overlapping_meetings(meetings):
    prev_end = meetings[0][1]
    
    for start, end in meetings[1:]:
        if prev_end > start:
            # previous meeting ends before current meeting starts
            return False
        prev_end = end
    return True
    
print(overlapping_meetings([[1,2],[2,3],[3,4],[1,3]]))
print(overlapping_meetings([[1,2],[1,2],[1,2]]))
print(overlapping_meetings([[1,2],[2,3]]))
```
