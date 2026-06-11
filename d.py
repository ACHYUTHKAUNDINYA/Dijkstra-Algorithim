import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
print(graph)

distance = {}
for node in graph:
    distance[node] = float('inf')
distance['A'] = 0
print(distance)

came_from = {}
for node in graph:
    came_from[node] = None
print(came_from)

pq = []
heapq.heappush(pq, (0, 'A'))  # <- fix is here

visited = set()

while pq:
    current_cost, current = heapq.heappop(pq)
    if current in visited:
        continue
    visited.add(current)
    print(f"Visiting {current} at cost {current_cost}")
    for neighbor, edge_cost in graph[current]:

        if neighbor in visited:
            continue

        new_cost = current_cost + edge_cost
        print(f"  checking {current} -> {neighbor}, cost would be {new_cost}")
        if new_cost < distance[neighbor]:
            distance[neighbor] = new_cost
            came_from[neighbor] = current
            heapq.heappush(pq, (new_cost, neighbor))
            print(f"  updated {neighbor} to cost {new_cost}")


def get_path(came_from, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


path = get_path(came_from, 'A', 'D')
print(f"\nShortest path: {' -> '.join(path)}")
print(f"Total cost: {distance['D']}")
