# 🟡 LRU Cache

Design a data structure that follows the constraints of a [**Least Recently Used (LRU) cache**](https://en.wikipedia.org/wiki/Cache\_replacement\_policies#LRU).

Implement the `LRUCache` class:

* `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
* `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
* `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

{% code overflow="wrap" %}
```python
class Node():
    def __init__(self, key=None, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def _insert(self, node):
        node.prev = self.tail.prev 
        node.next = self.tail 
        self.tail.prev.next = node
        self.tail.prev = node
        

    def get(self, key: int) -> int:
        if key in self.map:
            #remove node from ll
            node = self._remove(self.map[key])
            #add node back to ll
            self._insert(node)

            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self._remove(self.map[key])
            node.value = value
        else:
            node = Node(key, value)
        self.map[key] = node
        self._insert(self.map[key]) 

        if len(self.map) > self.capacity:
            # get least used 
            lru = self.head.next
            _ = self._remove(lru)
            del self.map[lru.key]

```
{% endcode %}
