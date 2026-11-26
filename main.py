from grid import Grid
from agent import Agent

rows, cols = 5, 5

start = (0, 0)
goal = (4, 4)

obstacles = {
    (2, 2),
    (3, 2),
    (1, 3)
}

grid = Grid(rows, cols, goal, obstacles)
agent = Agent(start)

path = agent.find_path(start, goal, grid)

if path:
    for position in path:
        agent.position = position
        grid.display(agent.position)

    print("🎯 Goal reached!")
    print(f"Total movements: {len(path) - 1}")

else:
    print("No valid path found.")
