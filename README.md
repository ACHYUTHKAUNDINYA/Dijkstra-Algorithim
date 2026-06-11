# Dijkstra's Algorithm

A Python implementation of Dijkstra's shortest path algorithm.

## How it works

Dijkstra's algorithm finds the shortest path between nodes in a weighted graph. It uses a priority queue (min-heap) to always process the lowest-cost node next.

## Graph

The graph is represented as an adjacency list where each node maps to a list of `(neighbor, cost)` tuples.

```
A --1-- B
|       |
4       2
|       |
C --1-- D
 \     /
  4   5
   \ /
    B
```

## Usage

```bash
python d.py
```

## Example Output

```
Visiting A at cost 0
Visiting B at cost 1
Visiting C at cost 3
Visiting D at cost 4

Shortest path: A -> B -> C -> D
Total cost: 4
```
