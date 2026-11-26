from grid import Grid 
from agent import Agent 
# Grid setup
rows, cols = 5, 5 
start = (0, 0) 
goal = (4, 4) 
obstacles = [(2, 2), (3, 2), (1, 3)] 
grid = Grid(rows, cols, goal, obstacles) 
agent = Agent(start)
#Run agent loop 
while agent.position != goal: 
  grid.display(agent.position) 
  dx, dy = agent.perceive(goal) 
  direction = agent.decide(dx, dy) 
  agent.move(direction, grid) 
  
grid.display(agent.position)
print("🎯 Goal reached!")
