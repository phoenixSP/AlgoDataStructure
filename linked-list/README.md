# Linked List

Linked list is used to represent sequential data. It consists of nodes, which stores the value as well as the address of the next node. A linked list is identified by the start node.&#x20;

**Advantages**

Insertion and deletion of a node in the list (given its location) is O(1) whereas in arrays the following elements will have to be shifted.

**Disadvantages**

Access time is linear because directly accessing elements by its position in the list is not possible (for example, element in position 4 can be accessed using `arr[4`). In case of linked list, the list has to be traversed from the start.&#x20;

Types of Linked list

* Singly linked list: Each node except the last points to the next node
* Doubly linked list: Each node has two pointers, `next` which points to the next node and `prev` which points to the previous node. The `prev` pointer of the first node and the `next` pointer of the last node point to `null`.
* Circular linked list: A linked list where the last node points back to the first node.

### Time complexity <a href="#time-complexity" id="time-complexity"></a>

| Operation | Big-O | Note                                                 |
| --------- | ----- | ---------------------------------------------------- |
| Access    | O(n)  |                                                      |
| Search    | O(n)  |                                                      |
| Insert    | O(1)  | Assumes you have traversed to the insertion position |
| Remove    | O(1)  | Assumes you have traversed to the node to be removed |

### Corner cases <a href="#corner-cases" id="corner-cases"></a>

* Empty linked list (head is `null`)
* Single node
* Two nodes
* Linked list has cycles. **Tip:** Clarify beforehand with the interviewer whether there can be a cycle in the list. Usually the answer is no and you don't have to handle it in the code

## Techniques

* Sentinel/dummy nodes
* Two pointers
* Other linked list operations like truncating a list by setting the next pointer to null, swapping values of nodes instead of next etc.&#x20;
*

