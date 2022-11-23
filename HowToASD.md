## Table of Contents

1. [Arrays](#Arrays)
   1. [HashTables](#HashTables)

2. [Binary Search](#BinarySearch)


# Arrays

## HashTable

An HashTable is a data structure that maps keys to values for highly efficient lookup. It is a structure that can be implemented with arrays, linked lists, binary search trees (in this case we would have $O(n \log n)$ lookup time. The advantage of this is potentially using less space, since we no longer allocate a large array. We can also iterate through the keys i order, which can be useful sometimes), or hash tables.

```python
HashTable = dict()
```
or if we want to use defaultdict
```python
from collections import defaultdict

HashTable = defaultdict(int)
# a default value of 0 is assigned to all keys
```

## ArrayList & ResizableArray

When you need an array-like data structure that offers dynamic resizing, you would usually use an Arraylist. An Arraylist is an array that resizes itself as needed while still providing $O(1)$ access.

```python
Array = [None] * 1000
# array of 1000 elements, all None
```

# Binary Search

Binary search is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array.

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```





# Stack

The stack data structure is precisely what it sounds like: a stack of data. In certain types of problems, it can be favorable to store data in a stack rather than in an array.

A stack uses LIFO (last-in first-out) ordering. That is, as in a stack of dinner plates, the most recent item added to the stack is the first item to be removed.

It uses the following operations:

- `push(item)`: adds an item to the top of the stack
- `pop()`: removes the top item from the stack
- `peek()`: returns the top of the stack without removing it
- `isEmpty()`: returns true if and only if the stack is empty

Unlike an array, a stack does not offer constant-time access to the ith item. However, it does allow constant-time adds and removes, as it doesn't require shifting elements around.

```python
stack = []

# add to the top of the stack
stack.append(1)
stack.append(2)

# remove from the top of the stack
stack.pop()
```

One case where stacks are often useful is in certain recursive algorithms. Sometimes you need to push temporary data onto a stack as you recurse, but then remove them as you backtrack (for example, because the recursive check failed). A stack offers an intuitive way to do this.

A stack can also be used to implement a recursive algorithm iteratively.

## Queue

A queue is an ordered collection of items where the addition of new items happens at one end, called the "rear," and the removal of existing items occurs at the other end, commonly called the "front." As an element enters the queue it starts at the rear and makes its way toward the front, waiting until that time when it is the next element to be removed.

It uses the following operations:

- `add(item)`: adds an item to the rear of the queue
- `remove()`: removes the front item from the queue
- `peek()`: returns the front of the queue without removing it
- `isEmpty()`: returns true if and only if the queue is empty

```python
from collections import deque

queue = deque() # double-ended queue
```

A queue can also be implemented with a linked list. In fact, they are essentially the same thing, as long as items are added and removed from opposite sides.

One place where queues are often used is in breadth-first search or in implementing a cache. In breadth-first search, for example, we used a queue to store a list of the nodes that we need to process. Each time we process a node, we add its adjacent nodes to the back of the queue. This allows us to process nodes in the order in which they are viewed.




# Linked List

A Linked list is a data structure that represents a sequence of nodes. In as singly linked list, each node points to the next node in the linked list. In a doubly linked list, each node points to the next node and the previous node. In a circular linked list, the tail node points to the head node.

Unlike an array, a linked list does not provide costant access time to a particolar index within the list. This means, that if you'd like to find the kth element in a linked list, you'd have to traverse the list from the head node to the kth node. This is because the nodes in a linked list are not stored in contiguous memory locations.

## Singly Linked List

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```

In this implementation, the head node is the first node in the linked list. The tail node is the last node in the linked list. The tail node's next pointer points to None.

## Techniques

- Slow and Fast Pointer

_This is a technique that is used to solve problems that involve linked list traversal. The slow pointer moves one node at a time, while the fast pointer moves two nodes at a time. This technique is used to find the middle node of a linked list, or to determine if a linked list has a cycle._


- Dummy linked list

```python
dummy = ListNode()
```

- Check if has a cycle

```python
def hasCycle(self, head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

- Reverse a linked list

```python
def reverseList(self, head: ListNode) -> ListNode:
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
```

- Sometimes it's useful to split a linked list into two parts


# Trees

A nice way to understand a tree is with a recursive explanation. A tree is a data structure composed of nodes.

- Each tree has a root node. (Actually, this isn't strictly necessary in graph theory, but it's usually how we use trees in programming)

- The root node has zero or more child nodes.

- Each child node has zero or more child nodes, and so on.

The tree cannot contain cycles. The nodes may or may not be in a particular order, they could have any data type as values, and they may or may not have links back to their parent nodes.

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
```

## Binary Tree

A binary tree is a tree in which each node has up to two children. Not all trees are binary trees. There are occasions when you might have a tree that is not a binary tree. For example, suppose you were using a tree to represent a bunch of phone numbers. In this case, you might use a 10-ary tree, with each node having up to 10 children (one for each digit}.
A node is called a "leaf" node if it has no children.

```python
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

## Binary Search Tree

A binary search tree is a binary tree in which every node fits a specific ordering property: _all left descendents_ $\leq n <$ _all right descendents_. This must be true for each node $n$. Note that this inequality must be true for all of a node's descendents, not just its immediate children

> The definition of a binary search tree can vary slightly with respect to equality. Under some definitions, the tree cannot have duplicate values. In others, the duplicate values will be on the right or can be on either side. All are valid definitions, but you should clarify this with your interviewer.

### Balanced vs Unbalanced

While many trees are balanced, not all are. Note that balancing a tree does not mean the left and right subtrees are exactly the same size (like you see under "perfect binary trees")

One way to think about it is that a "balanced" tree really means something more like "not terribly imbalanced:' It's balanced enough to ensure $O(\log n)$ times for insert and find, but it's not necessarily as balanced as it could be.

### Complete Binary Tree

A complete binary tree is a binary tree in which every level of the tree is fully filled, except for perhaps the last level. lo the extent that the last level is filled, it is filled left to right.

### Full Binary Tree

A full binary tree is a binary tree in which every node has either zero or two children. That is, no nodes have only one child.


### Perfect Binary Tree

A perfect binary tree is one that is both full and complete. All leaf nodes will be at the same level, and this level has the maximum number of nodes.

## Binary Tree Traversal

### In-order Traversal

In-order traversal means to "visit" (often, print) the left branch, then the current node, and finally, the right branch.

```python
def inOrderTraversal(self, root):
    if root:
        self.inOrderTraversal(root.left)
        print(root.val)
        self.inOrderTraversal(root.right)
```

### Pre-order Traversal

Pre-order traversal visits the current node before its child nodes (hence the name "pre-order").

```python
def preOrderTraversal(self, root):
    if root:
        print(root.val)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)
```

### Post-order Traversal

Post-order traversal visits the current node after its child nodes (hence the name "post-order").

```python
def postOrderTraversal(self, root):
    if root:
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print(root.val)
```

### Level-order Traversal

Level-order traversal visits the nodes level by level. You'll often see this done with a queue.

```python
def levelOrderTraversal(self, root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

## Binary Heaps (min-heap and max-heap)

We'll just discuss min-heaps here. Max-heaps are essentially equivalent, but the elements are in descending order rather than ascending order

A min-heap is a complete binary tree (that is, totally filled other than the rightmost elements on the last level) where each node is smaller than its children. The root, therefore, is the minimum element in the tree.

We have two key operations on a min-heap: `insert` and `extract_min`.

### Insert

When we insert into a min-heap, we always start by inserting the element at the bottom. We insert at the rightmost spot so as to maintain the complete tree property.

Then, we "fix" the tree by swapping the new element with its parent, until we find an appropriate spot for the element We essentially bubble up the minimum element.

This takes $O(\log n)$ time, where $n$ is the number of elements in the heap.

### Extract Min

Finding the minimum element of a min-heap is easy: it's always at the top. The trickier part is how to remove it. (In fact, this isn't that tricky.)

First, we remove the minimum element and swap it with the last element in the heap (the bottommost, rightmost element). Then, we bubble down this element, swapping it with one of its children until the min-heap property is restored.

Do we swap it with the left child or the right child? That depends on their values. There's no inherent ordering between the left and right element, but you'll need to take the smaller one in order to maintain the min-heap ordering.

This takes $O(\log n)$ time.

# Tries

A trie (sometimes called a prefix tree} is a funny data structure. It comes up a lot in interview questions, but algorithm textbooks don't spend much time on this data structure.

A trie is a variant of an n-ary tree in which characters are stored at each node. Each path down the tree may represent a word.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
```

The `* nodes` (sometimes called "null nodes") are often used to indicate complete words. For example, the fact that there is a `* node` under `MANY` indicates that `MANY` is a complete word. The existence of the `MA` path
indicates there are words that start with `MA`.

The actual implementation of these `* nodes` might be a special type of child (such as a `TerminatingTrieNode`, which inherits from `TrieNode`. Or, we could use just a boolean flag terminates within the "parent" node.

A node in a trie could have anywhere from 1 through `ALPHABET_SIZE + 1` children (or, `O` through `ALPHABET_SIZE` if a boolean flag is used instead of a `* node`).

Very commonly, a trie is used to store the entire (English) language for quick prefix lookups. While a hash table can quickly look up whether a string is a valid word, it cannot tell us if a string is a prefix of any valid words. A trie can do this very quickly.

> How quickly? A trie can check if a string is a valid prefix in $O(K)$ time, where K is the length of the string. This is actually the same runtime as a hash table will take. Although we often refer to hash table lookups as being $O(1)$ time, this isn't entirely true. A hash table must read through all the characters in the input which takes $O(K)$ time in the case of a word lookup

Many problems involving lists of valid words leverage a trie as an optimization. In situations when we search through the tree on related prefixes repeatedly


# Backtracking

# Graph



# Dynamic Programming

# Greedy

# Intervals

# Bit Manipulation
