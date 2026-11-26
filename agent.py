def __init__(self, start): 
  self.position = start
def perceive(self, goal):
  ax, ay = self.position 
  gx, gy = goal
  dx = gx - ax 
  dy = gy - ay 
  return
   dx, dy 

def decide(self, dx, dy): 
  # Prefer horizontal movement first 
  if dx != 0: 
    return (1 if dx > 0 else -1, 0) 
  elif dy != 0: 
    return (0, 1 if dy > 0 else -1) 
  return (0, 0)

def move(self, direction, grid): 
  new_x = self.position[0] + direction[0] 
  new_y = self.position[1] + direction[1] 
  new_pos = (new_x, new_y) 
  if grid.is_valid(new_pos): 
    self.position = new_pos
