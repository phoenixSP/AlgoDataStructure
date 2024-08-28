# Trie

A trie is a tree-like data structure whose nodes store the letters of an alphabet. By structuring the nodes in a particular way, words and strings can be retrieved from the structure by traversing down a branch path of the tree.

| Operation       | Time Complexity | Explanation                                                                                               |
| --------------- | --------------- | --------------------------------------------------------------------------------------------------------- |
| Building a Trie | O(N\*avgk)      | N is the number of strings to be inserted and k is the length of the string                               |
| Insertion       | O(k)            | Since the children array has constant size (size of alphabet), hence insertion has linear time complexity |
| Search          | O(k)            |                                                                                                           |
| Deletion        | O(k)            |                                                                                                           |

## Uses of Tries

* Tries can be used for spell checking and auto complete
* Prefix based searching

## Trie vs HashMap

* There are no collisions in a trie data structure which means a better worst-case time complexity than a hash table that is not implemented properly.
* Hash functions are not used in a Trie data structure because every key can be represented in order (alphabetically), and is uniquely retrievable since every branch path to a string’s value will be unique to _that_ key.
* Searching of a string in a Trie data structure is done in O(k) time complexity. Where k is the number of words in the query string. It may also take less than O(k) time when the query string is not present in the trie
* The downside of a trie is that is takes up a lot of memory and space with empty (`null`) pointers.

## Implementation

Refer to Implement Trie problem

## Advanced: Radix Trees

Radix trees are compressed version of tries to save space. Each internal node has to have two children, otherwise it is compressed together to create one node.
