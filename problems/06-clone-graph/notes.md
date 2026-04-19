# Clone Graph

## Problem
Given a reference to a node in a connected undirected graph, return a deep copy of the graph. Each node has a value and a list of neighbors.

## Brute Force
A naive DFS without tracking visited nodes would recurse infinitely on any cycle. There's no meaningful brute force — the hash map isn't an optimization, it's a correctness requirement.

## Optimized Approach
DFS with an `oldToNew` hash map that maps original nodes to their clones. Before creating a new clone, check if one already exists in the map. This prevents infinite loops on cycles and ensures each node is cloned exactly once.

- Time: O(V + E) — visit every node and edge once
- Space: O(V) — hash map stores one entry per node

The recursion builds the clone bottom-up: create the node, register it immediately in the map (before visiting neighbors), then populate its neighbor list.

## Reflection
Registering `oldToNew[node] = copy` *before* recursing into neighbors is critical — it's what breaks the cycle. If you waited until after processing neighbors to register, you'd loop forever. This same "mark before recurse" pattern applies broadly to graph traversal problems. The `return dfs(node) if node else None` guard handles the null input case cleanly at the top level.
