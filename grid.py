def __init__(self, rows, cols, goal, obstacles): 
  self.rows = rows 
  self.cols = cols 
  self.goal = goal 
  self.obstacles = set(obstacles)
  
  
def is_valid(self, position): 
  x, y = position 
  return ( 
    0 <= x < self.rows and 
    0 <= y < self.cols and 
    position not in self.obstacles 
  ) 
  
def display(self, agent_pos):
  for i in range(self.rows):
    row = ""
    for j in range(self.cols): 
     if (i, j) == agent_pos:
      row += "A " 
     elif (i, j) == self.goal: 
       row += "G " 
     elif (i, j) in self.obstacles:
       row += "X " 
     else: row += ". " 
   print(row) 
print()
