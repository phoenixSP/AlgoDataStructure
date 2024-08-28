# 🟡 Course Schedule

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

* For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

**Constraints:**

* `1 <= numCourses <= 2000`
* `0 <= prerequisites.length <= 5000`
* `prerequisites[i].length == 2`
* `0 <= ai, bi < numCourses`
* All the pairs prerequisites\[i] are **unique**.

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        TC: DFS  O(V + E)
        '''
        
        if prerequisites is None or len(prerequisites) == 0:
            return True # there are no prerequisites, so all courses can be finished independently
        
        course_map = {i: [] for i in range(numCourses)}
        for prerequisite in prerequisites:
            if prerequisite[0] not in course_map:
                course_map[prerequisite[0]] = []
            course_map[prerequisite[0]].append(prerequisite[1])

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False # detection of loop

            if course_map[crs] == []:
                return True # no prerequiresite

            visited.add(crs)
            for pre in course_map[crs]:
                if not dfs(pre):
                    return False # if dfs is False for one, then it is false for the child as well

            course_map[crs] = [] # since we found that crs can be completed, thus, we can make the prerequisite empty to reduce the need to recompute again
            visited.remove(crs) # we checked if crs can be completed, now for other courses, we need to make it visited=False again

            return True

        for crs in range(numCourses):
            if not dfs(crs): 
                return False

        return True
```
