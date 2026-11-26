
from collections import deque


class Agent:
    def __init__(self, start):
        self.position = start

    def find_path(self, start, goal, grid):
        queue = deque([[start]])
        visited = {start}

        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        while queue:
            path = queue.popleft()
            current = path[-1]

            if current == goal:
                return path

            for dx, dy in directions:
                neighbor = (
                    current[0] + dx,
                    current[1] + dy
                )

                if neighbor not in visited and grid.is_valid(neighbor):
                    visited.add(neighbor)
                    queue.append(path + [neighbor])

        return None
