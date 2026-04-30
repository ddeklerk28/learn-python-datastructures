# Data Structures From First Principles — Python

> Build every data structure by hand. No `collections`, no `heapq`, no shortcuts.

This repository is a structured, self-directed curriculum for implementing core data structures in Python from scratch. The goal is not to produce production-ready libraries — it is to develop a deep, reasoned understanding of how data structures work, why they exist, and what tradeoffs they encode.

Each implementation should be treated as a learning artefact: write it like you'd publish it, test it like you'd ship it.

---

## Rules of Engagement

- **No standard library data structure imports.** `collections`, `heapq`, `queue` and similar modules are off-limits until after you have built the equivalent yourself.
- **Build on your own work.** From Tier 2 onward, use the structures you previously wrote — not Python's built-ins.
- **Test edge cases explicitly.** Empty structure, single element, duplicates, and maximum capacity where applicable.
- **Understand before you implement.** For each structure, be able to answer: *why does this exist, and what problem does it solve that the previous structure couldn't?*
- **Derive complexity, don't look it up.** Trace through operations manually and reason about what scales.

---

## Curriculum

### Tier 1 — Foundational Building Blocks

The ground floor. Everything else is built on top of these. Take your time here — pointer manipulation and memory intuition developed at this stage will pay dividends throughout the rest of the curriculum.

| # | Structure | Key Concepts |
|---|---|---|
| 1 | Dynamic Array | Raw memory via `ctypes`, growth/shrink strategy, amortised cost |
| 2 | Singly Linked List | Node structure, pointer traversal, insert/delete at head and tail |
| 3 | Doubly Linked List | Bidirectional pointers, sentinel/dummy nodes, O(1) delete with reference |

**Tier 1 Checklist**
- [ ] Dynamic Array — allocate a fixed C array, implement `append`, `insert`, `delete`, and automatic resizing (double on growth, halve on shrink at 25% capacity)
- [ ] Singly Linked List — implement `prepend`, `append`, `delete`, `search`, and `reverse`
- [ ] Doubly Linked List — extend above with backward traversal; implement `insert_before` and `insert_after` given a node reference

---

### Tier 2 — Abstract Data Types on Tier 1

These are not new structures so much as *contracts* — well-defined interfaces that can be satisfied by different underlying implementations. Implement each one twice, on different Tier 1 bases, and observe the tradeoffs.

| # | Structure | Built On | Key Concepts |
|---|---|---|---|
| 4 | Stack | Dynamic Array + Linked List | LIFO semantics, call stack intuition |
| 5 | Queue | Dynamic Array + Linked List | FIFO semantics, two-pointer technique |
| 6 | Deque | Doubly Linked List | O(1) operations at both ends |
| 7 | Circular Buffer | Raw Array | Modular indexing, fixed-capacity queue |

**Tier 2 Checklist**
- [ ] Stack (array-backed) — `push`, `pop`, `peek`, `is_empty`
- [ ] Stack (linked list-backed) — same interface, different internals
- [ ] Queue (array-backed) — `enqueue`, `dequeue`, `peek`, `is_empty`
- [ ] Queue (linked list-backed) — same interface, different internals
- [ ] Deque — `push_front`, `push_back`, `pop_front`, `pop_back`
- [ ] Circular Buffer — fixed size, wrap-around indexing, raise on overflow

---

### Tier 3 — Trees

Trees are where the curriculum gets serious. The jump from linear to hierarchical structure is conceptually significant. Implement in order — each structure motivates the next.

| # | Structure | Key Concepts |
|---|---|---|
| 8 | Binary Search Tree | BST invariant, recursive structure, deletion cases |
| 9 | BST Traversals | Inorder, preorder, postorder — recursive and iterative |
| 10 | AVL Tree | Balance factor, left/right rotations, self-balancing on insert and delete |
| 11 | Heap (Min & Max) | Heap property, array representation, `heapify_up`, `heapify_down` |
| 12 | Priority Queue | Thin interface over your heap |

**Tier 3 Checklist**
- [ ] BST — `insert`, `search`, `delete` (handle all three deletion cases: leaf, one child, two children), `min`, `max`
- [ ] BST Traversals — implement all three recursively first, then iteratively using your own Stack
- [ ] AVL Tree — extend BST; implement `_rotate_left`, `_rotate_right`, `_balance_factor`, auto-rebalance on `insert` and `delete`
- [ ] Min Heap — `insert`, `extract_min`, `peek`, `heapify_up`, `heapify_down`; store internally on your Dynamic Array
- [ ] Max Heap — same as above, inverted comparator
- [ ] Priority Queue — wrap your heap with a clean `enqueue(item, priority)` / `dequeue()` interface

---

### Tier 4 — Hashing

Hash maps are among the most practically important structures you will ever use. Implement both collision strategies and understand why each exists.

| # | Structure | Key Concepts |
|---|---|---|
| 13 | Hash Map (Separate Chaining) | Hash function design, bucket array, linked list chains |
| 14 | Hash Map (Open Addressing) | Linear probing, tombstone deletion, load factor |
| 15 | Hash Set | Set semantics on top of your hash map |

**Tier 4 Checklist**
- [ ] Hash Map (Chaining) — implement your own hash function, bucket array on your Dynamic Array, resolve collisions via your Linked List; implement `put`, `get`, `delete`, `contains`, resize on load factor > 0.7
- [ ] Hash Map (Open Addressing) — linear probing, tombstone markers for deletion, same interface as above
- [ ] Hash Set — `add`, `remove`, `contains`, `union`, `intersection`, `difference` — backed by your hash map

---

### Tier 5 — Advanced Trees

| # | Structure | Key Concepts |
|---|---|---|
| 16 | Trie | Character-keyed children, prefix matching, space vs. time tradeoff |
| 17 | Red-Black Tree | Colouring invariants, rotation + recolouring, comparison to AVL |

**Tier 5 Checklist**
- [ ] Trie — `insert`, `search`, `starts_with`, `delete`; implement children as either a fixed array of 26 or your hash map
- [ ] Red-Black Tree — implement the full insertion and deletion rebalancing rules; write a `validate()` method that asserts all invariants hold; note explicitly where RB and AVL make different tradeoffs

> **Note on Red-Black Trees:** This is the hardest implementation in the curriculum. Budget more time here than you think you need. Work through the invariant rules on paper before writing a line of code.

---

### Tier 6 — Graphs

Graphs are the most general structure in this curriculum. Everything before this is, in some sense, a special case of a graph.

| # | Structure | Key Concepts |
|---|---|---|
| 18 | Graph — Adjacency List | Hash map of neighbour lists, directed vs. undirected |
| 19 | Graph — Adjacency Matrix | 2D array representation, when to prefer matrix over list |
| 20 | BFS | Level-order traversal, shortest path in unweighted graph |
| 21 | DFS | Recursive and iterative, discovery/finish times, cycle detection |
| 22 | Union-Find | Disjoint sets, union by rank, path compression |

**Tier 6 Checklist**
- [ ] Graph (Adjacency List) — `add_vertex`, `add_edge`, `remove_edge`, `neighbours`, support directed and undirected; back it with your Hash Map
- [ ] Graph (Adjacency Matrix) — same interface where applicable; implement `has_edge` in O(1)
- [ ] BFS — use your own Queue; return visited order and shortest-hop distances from source
- [ ] DFS — recursive implementation with visited tracking; iterative implementation using your Stack
- [ ] DFS Extensions — cycle detection, topological sort on a DAG
- [ ] Union-Find — `find` with path compression, `union` with rank; implement `connected` and `num_components`

---

### Tier 7 — Composite & Probabilistic Structures

The capstone tier. These structures either compose multiple earlier implementations, or introduce probabilistic and range-based reasoning. Each one is a distinct design problem.

| # | Structure | Key Concepts |
|---|---|---|
| 23 | LRU Cache | Hash map + doubly linked list composition, O(1) get and put |
| 24 | Skip List | Probabilistic balancing, multiple levels of linked lists |
| 25 | Segment Tree | Range queries, recursive decomposition, lazy propagation |
| 26 | Bloom Filter | Probabilistic membership, multiple hash functions, false positive rate |

**Tier 7 Checklist**
- [ ] LRU Cache — `get(key)`, `put(key, value)` both O(1); evict least recently used on capacity breach; compose your Hash Map and Doubly Linked List
- [ ] Skip List — `insert`, `search`, `delete`; implement probabilistic level assignment; compare search performance empirically against your BST
- [ ] Segment Tree — build on an array input; support range sum and range min queries; implement point update
- [ ] Bloom Filter — configurable capacity and false positive rate; derive the optimal number of hash functions from parameters; implement `add` and `might_contain`

---

## Suggested Repo Structure

```
/structures
    /tier_1
        dynamic_array.py
        singly_linked_list.py
        doubly_linked_list.py
    /tier_2
        stack.py
        queue.py
        deque.py
        circular_buffer.py
    /tier_3
        binary_search_tree.py
        avl_tree.py
        heap.py
        priority_queue.py
    /tier_4
        hash_map_chaining.py
        hash_map_open_addressing.py
        hash_set.py
    /tier_5
        trie.py
        red_black_tree.py
    /tier_6
        graph.py
        union_find.py
    /tier_7
        lru_cache.py
        skip_list.py
        segment_tree.py
        bloom_filter.py
/tests
    /tier_1
        test_dynamic_array.py
        ...
```

Each implementation file should include:
- A module-level docstring explaining what the structure is, why it exists, and what problem it solves
- Time complexity annotations on every public method (as docstrings or inline comments)
- A `__repr__` or `__str__` for debuggability

---

## Complexity Reference

Derive these yourself — do not use this table as a substitute for reasoning. Use it only to check your work after the fact.

| Structure | Access | Search | Insert | Delete | Space |
|---|---|---|---|---|---|
| Dynamic Array | O(1) | O(n) | O(1) amortised | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1)* | O(n) |
| Stack / Queue | — | — | O(1) | O(1) | O(n) |
| BST (avg) | — | O(log n) | O(log n) | O(log n) | O(n) |
| BST (worst) | — | O(n) | O(n) | O(n) | O(n) |
| AVL Tree | — | O(log n) | O(log n) | O(log n) | O(n) |
| Heap | O(1) min/max | — | O(log n) | O(log n) | O(n) |
| Hash Map (avg) | — | O(1) | O(1) | O(1) | O(n) |
| Hash Map (worst) | — | O(n) | O(n) | O(n) | O(n) |
| Trie | — | O(m) | O(m) | O(m) | O(n·m) |
| Graph (list) | — | O(V+E) | O(1) | O(E) | O(V+E) |
| Graph (matrix) | O(1) | O(V²) | O(V²) | O(V²) | O(V²) |

*O(1) delete on doubly linked list given a node reference; O(n) on singly linked list.
m = key length, V = vertices, E = edges.

---

## Resources

Reach for these when you are stuck on *why*, not *how*:

- **Introduction to Algorithms (CLRS)** — Cormen et al. The canonical reference. Dense but authoritative.
- **The Algorithm Design Manual** — Skiena. More intuitive, better on tradeoffs and real-world applicability.
- **Crafting Interpreters** — Nystrom. Not directly about data structures, but exceptional on building things from scratch in a principled way.

---

*The goal is not to finish. The goal is to understand deeply enough that you could rebuild any of this from a blank file and a clear head.*